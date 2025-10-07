# 🥗 Consultor de Alimentos com LangChain# 🥗 Consultor de Alimentos MCP



Um sistema inteligente de consultoria nutricional que utiliza **LangChain** e **Google Gemini** para analisar tipos de alimentação, recomendar alimentos e calcular valores nutricionais.Um servidor MCP (Model Context Protocol) especializado em nutrição e orientação dietética. Este consultor fornece informações nutricionais, cálculos calóricos, sugestões de dieta e comparações entre alimentos.



## 🚀 Funcionalidades## 🚀 Instalação



### 1. **Recomendação Inteligente de Alimentação** 🎯1. **Instale as dependências:**

- Analisa tipos de dieta (vegetariana, low carb, ganho de massa, etc.)```bash

- Recomenda alimentos específicos da base de dadospip install -r requirements.txt

- Fornece dicas nutricionais personalizadas```

- Usa IA para análise contextual

2. **Para instalar o MCP framework:**

### 2. **Busca de Informações Nutricionais** 🔍```bash

- Busca detalhada por nome de alimentopip install mcp

- Informações completas: calorias, macros, vitaminas```

- Benefícios para a saúde

- Índice glicêmico## 🛠️ Uso



### 3. **Calculadora de Refeições** 🧮### Como Servidor MCP

- Calcula valores nutricionais totais

- Suporte a múltiplos alimentos e porçõesPara executar como servidor MCP (para integração com clientes MCP):

- Breakdown detalhado por alimento```bash

- Totais de macronutrientespython mcp.py --server

```

### 4. **Análise de Deficiências Nutricionais** 🩺

- Analisa sintomas e necessidades### Teste Rápido

- Sugere alimentos terapêuticos

- Recomendações baseadas em IAPara testes rápidos das funcionalidades:

- Plano alimentar personalizado```bash

python mcp.py

### 5. **Busca por Categoria** 📂```

- Filtra alimentos por tipo (frutas, vegetais, proteínas, etc.)

- Listagem organizada### Cliente de Teste

- Informações rápidas

Para testar todas as funcionalidades automaticamente:

## 📋 Pré-requisitos```bash

python cliente_teste.py

- Python 3.8+```

- Chave API do Google Gemini

- Conexão com internetPara modo interativo:

```bash

## ⚙️ Instalaçãopython cliente_teste.py --interactive

```

1. **Clone/baixe os arquivos:**

```bash## 🔧 Ferramentas Disponíveis

cd /caminho/para/projeto

```### 1. `buscar_info_alimento`

Busca informações nutricionais detalhadas de um alimento específico.

2. **Instale as dependências:**

```bash**Exemplo:**

pip install -r requirements.txt```json

```{

  "alimento": "banana"

3. **Configure a API Key:**}

Edite o arquivo `.env` e adicione sua chave do Google:```

```bash

GOOGLE_API_KEY="sua_chave_aqui"### 2. `calcular_calorias_refeicao`

```Calcula calorias e nutrientes totais de uma refeição com múltiplos alimentos.



## 🎮 Como Usar**Exemplo:**

```json

### Modo Interativo Completo{

```bash  "alimentos": [

python teste_consultor.py    {"alimento": "arroz", "porcao_gramas": 150},

```    {"alimento": "frango", "porcao_gramas": 100}

  ]

### Modo de Testes Diretos}

```bash```

python mcpAlimentos.py

```### 3. `sugerir_dieta`

Sugere uma dieta baseada no objetivo do usuário.

### Uso Programático

**Objetivos disponíveis:**

```python- `perda_peso`: Dieta para perda de peso

from mcpAlimentos import (- `ganho_massa`: Dieta para ganho de massa muscular

    get_recomendacao_alimentacao,- `saude_geral`: Dieta equilibrada para saúde geral

    buscar_alimento_info,

    calcular_refeicao**Exemplo:**

)```json

{

# Exemplo 1: Recomendação de dieta  "objetivo": "perda_peso"

resultado = get_recomendacao_alimentacao("dieta vegana")}

print(resultado)```



# Exemplo 2: Buscar alimento### 4. `listar_alimentos_categoria`

info = buscar_alimento_info("banana")Lista alimentos disponíveis por categoria.

print(info)

**Categorias disponíveis:**

# Exemplo 3: Calcular refeição- `fruta`

refeicao = [- `vegetal`

    {"alimento": "arroz", "porcao_gramas": 150},- `proteina`

    {"alimento": "frango", "porcao_gramas": 100}- `cereal`

]- `todas`

calc = calcular_refeicao(refeicao)

print(calc)**Exemplo:**

``````json

{

## 📊 Base de Dados  "categoria": "fruta"

}

O sistema inclui **28+ alimentos** organizados em categorias:```



- 🍎 **Frutas**: banana, maçã, laranja, morango, abacate### 5. `comparar_alimentos`

- 🥬 **Vegetais**: brócolis, espinafre, cenoura, tomate, batata-doce  Compara valores nutricionais entre dois alimentos.

- 🥩 **Proteínas**: frango, salmão, ovo, tofu, feijão preto

- 🌾 **Cereais**: arroz integral, aveia, quinoa, pão integral, macarrão integral**Exemplo:**

- 🥛 **Laticínios**: leite desnatado, iogurte grego, queijo cottage```json

- 🥜 **Oleaginosas**: amêndoa, castanha-do-brasil, nozes{

- 🌱 **Sementes**: chia, linhaça  "alimento1": "banana",

  "alimento2": "maçã"

### Informações por Alimento:}

- ✅ Calorias por 100g```

- ✅ Proteínas, carboidratos, fibras, gorduras

- ✅ Açúcar e sódio## 📊 Base de Dados

- ✅ Vitaminas e minerais

- ✅ Benefícios para saúdeO servidor inclui informações nutricionais para os seguintes alimentos:

- ✅ Índice glicêmico

- ✅ Categoria- **Frutas:** Banana

- **Vegetais:** Brócolis

## 🔧 Funções Principais- **Proteínas:** Frango

- **Cereais:** Arroz, Aveia

### `get_recomendacao_alimentacao(tipo_alimentacao: str)`

Analisa um tipo de alimentação e retorna recomendações inteligentes.### Informações incluídas:

- Calorias por 100g

**Exemplo:**- Proteínas (g)

```python- Carboidratos (g)

resultado = get_recomendacao_alimentacao("dieta mediterrânea")- Fibras (g)

# Retorna análise detalhada, alimentos recomendados, dicas, etc.- Gorduras (g)

```- Vitaminas e minerais

- Benefícios para a saúde

### `buscar_alimento_info(term: str)`- Categoria do alimento

Busca informações completas de um alimento específico.

## 🎯 Exemplos de Uso

**Exemplo:**

```python### Consulta Simples

info = buscar_alimento_info("aveia")```python

# Retorna dados nutricionais completos# Buscar informações da banana

```resultado = await session.call_tool("buscar_info_alimento", {"alimento": "banana"})

```

### `calcular_refeicao(alimentos_porcoes: List[Dict])`

Calcula valores nutricionais de uma refeição completa.### Calcular Refeição

```python

**Exemplo:**# Calcular calorias de uma refeição completa

```pythonresultado = await session.call_tool("calcular_calorias_refeicao", {

refeicao = [    "alimentos": [

    {"alimento": "quinoa", "porcao_gramas": 100},        {"alimento": "arroz", "porcao_gramas": 150},

    {"alimento": "salmao", "porcao_gramas": 120},        {"alimento": "frango", "porcao_gramas": 120},

    {"alimento": "brocolis", "porcao_gramas": 80}        {"alimento": "brócolis", "porcao_gramas": 80}

]    ]

resultado = calcular_refeicao(refeicao)})

# Retorna totais e breakdown por alimento```

```

### Plano Dietético

### `analisar_deficiencia_nutricional(sintomas: str)````python

Analisa sintomas e sugere alimentos terapêuticos.# Obter sugestões para ganho de massa

resultado = await session.call_tool("sugerir_dieta", {"objetivo": "ganho_massa"})

**Exemplo:**```

```python

analise = analisar_deficiencia_nutricional("fadiga e queda de cabelo")## 🔍 Funcionalidades

# Retorna possíveis deficiências e alimentos recomendados

```- ✅ **Informações Nutricionais Completas**

- ✅ **Cálculo de Calorias por Refeição**

## 💡 Exemplos de Consultas- ✅ **Sugestões de Dieta Personalizadas**

- ✅ **Comparação entre Alimentos**

### Tipos de Alimentação Suportados:- ✅ **Busca por Categoria**

- "dieta vegetariana balanceada"- ✅ **Interface Console Amigável**

- "dieta para ganho de massa muscular"- ✅ **Compatibilidade com MCP**

- "dieta para perda de peso"

- "dieta mediterrânea"## 🚀 Extensibilidade

- "dieta low carb"

- "dieta para diabéticos"Para adicionar novos alimentos, edite a variável `ALIMENTOS_DB` no arquivo `mcp.py`:

- "dieta anti-inflamatória"

- "alimentação pós-treino"```python

- "dieta vegana"ALIMENTOS_DB = {

    "novo_alimento": {

### Sintomas para Análise:        "calorias_por_100g": 100,

- "fadiga e cansaço constante"        "proteinas": 5.0,

- "queda de cabelo"        "carboidratos": 20.0,

- "anemia"        "fibras": 3.0,

- "dificuldade para dormir"        "gorduras": 1.0,

- "pele ressecada"        "vitaminas": ["Vitamina C"],

- "baixa imunidade"        "beneficios": ["Rico em nutrientes"],

        "categoria": "fruta"

## 🔄 Fluxo de Funcionamento    }

}

1. **Entrada do usuário** → Tipo de alimentação ou sintoma```

2. **Carregamento da base** → Lê alimentos do JSON

3. **Processamento IA** → LangChain + Gemini analisam## 📝 Notas

4. **Recomendações** → Alimentos específicos da base

5. **Formatação** → Resposta estruturada em JSON- Este é um sistema de demonstração com dados limitados

- Em produção, considere integrar com APIs de nutrição reais

## 🎯 Casos de Uso- O servidor suporta expansão para incluir mais alimentos e funcionalidades

- Compatível com qualquer cliente MCP

- **Nutricionistas**: Análise rápida e recomendações baseadas em IA

- **Pessoas em dieta**: Orientações personalizadas## 🤝 Contribuições

- **Atletas**: Planejamento nutricional para performance

- **Educação**: Aprendizado sobre nutriçãoSinta-se à vontade para expandir a base de dados de alimentos ou adicionar novas funcionalidades!
- **Desenvolvimento**: Base para apps de nutrição

## 🔧 Tecnologias

- **LangChain**: Framework para aplicações com LLM
- **Google Gemini**: Modelo de linguagem para análises
- **Python**: Linguagem principal
- **JSON**: Armazenamento da base de dados
- **dotenv**: Gerenciamento de variáveis de ambiente

## 📈 Próximas Funcionalidades

- [ ] Integração com APIs de nutrição reais
- [ ] Histórico de consultas
- [ ] Gráficos nutricionais
- [ ] Exportação de relatórios
- [ ] Mais alimentos na base
- [ ] Suporte a múltiplos idiomas

## 🤝 Contribuições

Para adicionar novos alimentos, edite `alimentos.json`:

```json
{
  "categoria": {
    "novo_alimento": {
      "calorias_por_100g": 100,
      "proteinas": 5.0,
      "carboidratos": 20.0,
      "fibras": 3.0,
      "gorduras": 1.0,
      "acucar": 2.0,
      "sodio": 10,
      "vitaminas": ["Vitamina C"],
      "beneficios": ["Rico em nutrientes"],
      "categoria": "categoria",
      "indice_glicemico": 30
    }
  }
}
```

## 📞 Suporte

Este é um projeto educacional demonstrando integração de LangChain com bases de dados nutricionais. 

---

**🥗 Consultor de Alimentos - Nutrição Inteligente com IA** 🤖# mcp-alimentos
