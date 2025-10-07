import json
import os
import unicodedata
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv
from json_repair import repair_json
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# ======================================
# CONFIGURAÇÃO INICIAL
# ======================================
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, max_tokens=8196)

BASE = Path(__file__).parent
ARQ = BASE / "alimentos.json"


def _sem_acento(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def _carregar_itens() -> Dict[str, Any]:
    if not ARQ.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {ARQ}")
    with open(ARQ, "r", encoding="utf-8") as f:
        return json.load(f)


# ======================================
# FUNÇÕES DO BOT
# ======================================


def buscar_alimento_info(term: str) -> str:
    alimentos_db = _carregar_itens()
    termo = _sem_acento(term or "").lower().strip()
    if not termo:
        return "Nenhum termo fornecido."

    for categoria, alimentos in alimentos_db.items():
        for nome, dados in alimentos.items():
            if termo in _sem_acento(nome).lower():
                calorias = dados.get("calorias_por_100g", "N/A")
                proteina = dados.get("proteinas", "N/A")
                carboidratos = dados.get("carboidratos", "N/A")
                gordura = dados.get("gorduras", "N/A")
                return (
                    f"O alimento '{nome}' pertence à categoria '{categoria}'. "
                    f"Possui aproximadamente {calorias} kcal, {proteina}g de proteína, "
                    f"{carboidratos}g de carboidratos e {gordura}g de gordura."
                )

    return f"Não encontrei informações sobre '{term}'."


def get_recomendacao_alimentacao(tipo_alimentacao: str) -> str:
    alimentos_db = _carregar_itens()
    alimentos_disponiveis = []
    for categoria, alimentos in alimentos_db.items():
        for nome, dados in alimentos.items():
            alimentos_disponiveis.append(
                {"nome": nome, "categoria": categoria, **dados}
            )

    template = """
    Você é um nutricionista. Analise o tipo de alimentação "{tipo_alimentacao}"
    e recomende alimentos da base abaixo:
    {alimentos_json}

    Retorne uma resposta textual simples e direta (sem JSON),
    explicando brevemente quais alimentos são recomendados,
    quais devem ser evitados e por quê.
    """
    prompt = PromptTemplate(
        input_variables=["tipo_alimentacao", "alimentos_json"], template=template
    )

    formatted_prompt = prompt.format(
        tipo_alimentacao=tipo_alimentacao,
        alimentos_json=json.dumps(alimentos_disponiveis, ensure_ascii=False),
    )

    resposta = llm.invoke([HumanMessage(content=formatted_prompt)])
    return resposta.content.strip()


# ======================================
# CHATBOT PRINCIPAL
# ======================================


def chatbot_console():
    print("🤖 NutriMCP — Chatbot Inteligente de Nutrição")
    print("=" * 60)
    print("Converse comigo sobre alimentação, dietas e nutrientes.")
    print("Digite 'sair' para encerrar.")
    print("=" * 60)

    historico = [SystemMessage(content="Você é um assistente MCP de nutrição.")]

    while True:
        user_input = input("\n🗣️ Você: ").strip()
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("👋 Até logo!")
            break

        historico.append(HumanMessage(content=user_input))

        decisor_prompt = f"""
        Você é o MCP, um controlador que decide qual função do sistema executar.
        Entrada do usuário: "{user_input}"

        Funções disponíveis:
        1. buscar_alimento_info(term)
        2. get_recomendacao_alimentacao(tipo_alimentacao)

        Retorne um JSON com:
        {{
            "acao": "buscar_alimento_info" ou "get_recomendacao_alimentacao",
            "parametro": "<texto extraído da frase>"
        }}
        """
        decisao = llm.invoke([HumanMessage(content=decisor_prompt)]).content
        try:
            if decisao.startswith("```json"):
                decisao = decisao.removeprefix("```json").strip()
            if decisao.endswith("```"):
                decisao = decisao.removesuffix("```").strip()

            decisao = repair_json(decisao)
            acao = json.loads(decisao)
        except:
            print("⚠️ Não entendi, tente reformular sua pergunta.")
            continue

        if acao.get("acao") == "buscar_alimento_info":
            resultado = buscar_alimento_info(acao.get("parametro", ""))
            print(f"📊 {resultado}")

        elif acao.get("acao") == "get_recomendacao_alimentacao":
            resultado = get_recomendacao_alimentacao(acao.get("parametro", ""))
            print(f"🍎 {resultado}")

        else:
            print("🤔 Não consegui identificar a intenção da sua pergunta.")


if __name__ == "__main__":
    chatbot_console()
