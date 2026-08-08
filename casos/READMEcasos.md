
---

## 📄 Arquivo 2: `casos/READMEcasos.md`

```markdown
# 🔬 Índice de Estudos de Caso

> **Coleção de problemas aplicados de engenharia**  
> **Repositório:** [github.com/JaderLugon/fenomenos-transporte-livro](https://github.com/JaderLugon/fenomenos-transporte-livro)

---

## 📖 Sobre os Estudos de Caso

Esta pasta contém **estudos de caso aplicados** que complementam os capítulos do livro. Cada caso é um **Jupyter Notebook independente** que resolve um problema real de engenharia usando os conceitos e ferramentas apresentados no capítulo correspondente.

### 🎯 Características dos casos:

- ✅ **Autocontidos**: podem ser executados independentemente dos notebooks principais
- ✅ **Documentados**: seguem um template padronizado com objetivos, dados, solução e discussão
- ✅ **Reprodutíveis**: todos os dados e códigos estão incluídos
- ✅ **Didáticos**: incluem interpretações físicas e análises de sensibilidade
- ✅ **Extensíveis**: professores podem adaptar e criar novos casos

### 📊 Estatísticas:

- **Total de casos:** 19
- **Capítulos cobertos:** 9 de 11
- **Níveis:** Graduação (12) e Pós-Graduação (7)
- **Tempo médio de execução:** 30–90 minutos

---

## 📋 Lista Completa de Estudos de Caso

### Capítulo 2 — Fundamentos dos Fluidos e Viscosidade

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 2.X1 | [Classificador de Fluidos Não-Newtonianos](EC_02_X1_Classificador_Fluidos_Nao_Newtonianos) | Graduação | 30 min | Ajuste de dados reológicos ao modelo de Lei de Potência (Ostwald-de Waele) |

---

### Capítulo 3 — Modelagem Matemática do Escoamento

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 3.X1 | [Balanço de Massa em Reator CSTR](EC_03_X1_Balanco_Massa_Reator_CSTR) | Graduação | 45 min | Resolução de EDO de primeira ordem com termo fonte |
| 3.X2 | [Calculadora de Números Adimensionais](EC_03_X2_Calculadora_Numeros_Adimensionais.ipynb) | Graduação | 30 min | Cálculo de Re, Pe, Pr, Sc com classificação de regimes |

---

### Capítulo 4 — Escoamento em Tubulações e Bombeamento

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 4.7 | [Sistema de Bombeamento em Prédio Residencial](EC_04_07_Bombeamento_Predio_Residencial.ipynb) | Graduação | 60 min | Cálculo de perda de carga, seleção de bomba, análise de NPSH |
| 4.8 | [Sistema Hidráulico para Elevação de Carga Pesada](EC_04_08_Elevador_Carga_Hidraulico.ipynb) | Pós-Graduação | 90 min | Dimensionamento de circuito hidráulico industrial com sincronismo |
| 4.X1 | [Solver Colebrook White](EC_04_X1_Solver_Colebrook_White.ipynb) | Pós-Graduação | 45 min | Newton-Raphson para equação não-linear implícita |


---

### Capítulo 5 — Hidrodinâmica de Canais Abertos

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 5.6 | [Hidrodinâmica do Rio Macaé](EC_05_06_Rio_Macae_Hidrodinamica.ipynb) | Pós-Graduação | 120 min | Simulação de onda de cheia com equações de Saint-Venant |
| 5.X1 | [Profundidade Normal em Canal Trapezoidal](EC_05_X1_Profundidade_Normal_Canal_Trapezoidal.ipynb) | Graduação | 45 min | Resolução numérica da equação de Manning |

---

### Capítulo 6 — Percolação em Meio Poroso

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 6.6 | [Percolação em Terreno com Textura Conhecida](EC_06_06_Percolacao_Terreno_Textura_Conhecida.ipynb) | Pós-Graduação | 90 min | Cálculo de perfil de potencial matricial com van Genuchten |
| 6.X1 | [Curva de Retenção de van Genuchten](EC_06_X1_Curva_Retencao_van_Genuchten.ipynb) | Graduação | 45 min | Comparação de curvas de retenção para diferentes texturas |

---

### Capítulo 7 — Fundamentos de Transferência de Calor

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 7.8 | [Isolamento Térmico de Forno de Padaria](EC_07_08_Isolamento_Forno_Padaria.ipynb) | Graduação | 60 min | Dimensionamento de isolamento com convecção e radiação |
| 7.X1 | [Circuito Térmico de Parede Composta](EC_07_X1_Circuito_Termico_Parede_Composta.ipynb) | Graduação | 45 min | Analogia elétrica para paredes multicamadas |

---

### Capítulo 8 — Transferência de Calor em Solos

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 8.8 | [Perfil Térmico Diurno em Solo](EC_08_08_Perfil_Termico_Diurno_Solo.ipynb) | Pós-Graduação | 90 min | Solução numérica da equação de calor com k(θ) variável |
| 8.X1 | [Estabilidade Numérica de Diferenças Finitas](EC_08_X1_Estabilidade_Numerica_Diferencas_Finitas.ipynb) | Pós-Graduação | 60 min | Comparação de esquemas explícito, implícito e Crank-Nicolson |
| 8.X2 | [Simulacao Acoplada Calor Umidade Solo](EC_08_X2_Simulacao_Acoplada_Calor_Umidade_Solo.ipynb) | Pós-Graduação | 60 min | Comparação de esquemas explícito, implícito e Crank-Nicolson |


---

### Capítulo 9 — Trocadores de Calor

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 9.5 | [Resfriamento de Óleo Hidráulico em Hidrelétrica](EC_09_05_Resfriamento_Oleo_Hidraulico.ipynb) | Graduação | 60 min | Dimensionamento de trocador de placas óleo-água |
| 9.6 | [Condensador de Vapor para UTE 100 MW](EC_09_06_Condensador_Vapor_UTE.ipynb) | Pós-Graduação | 120 min | Projeto completo de condensador casco-tubo com análise ambiental |
| 9.7 | [Caldeira Industrial para Geração de Vapor](EC_09_07_Caldeira_Industrial.ipynb) | Pós-Graduação | 90 min | Dimensionamento de caldeira flamotubular com NR13 |

---

### Capítulo 10 — Aletas e Superfícies Estendidas

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 10.5 | [Condensador a Ar (ACC) com Tubos Aletados](EC_10_05_Condensador_ACC_Tubos_Aletados.ipynb) | Pós-Graduação | 120 min | Projeto de condensador seco para regiões áridas |
| 10.6 | [Dissipador Térmico para Processador](EC_10_06_Dissipador_Termico_Processador.ipynb) | Graduação | 60 min | Dimensionamento de heat sink para CPU de computador |
| 10.7 | [Análise Térmica de Aleta por Diferenças Finitas](EC_10_07_Analise_Termica_Aleta_MDF.ipynb) | Pós-Graduação | 90 min | Solução numérica da equação da aleta com refinamento de malha |

---

### Capítulo 11 — Transporte de Calor e Massa em Corpos Hídricos

| # | Título | Nível | Tempo | Descrição |
|---|--------|-------|-------|-----------|
| 11.5 | [Dispersão de Poluentes no Rio Macaé](EC_10_05_Condensador_ACC_Tubos_Aletados.ipynb) | Pós-Graduação | 120 min | Modelagem de transporte com coeficientes de Liu e Elder |
| 11.X1 | [Difusão Artificial em Esquemas Upwind](EC_11_X1_Difusao_Artificial_Upwind.ipynb) | Pós-Graduação | 60 min | Análise de erro numérico em esquemas de primeira ordem |

---

## 🎓 Como Usar os Estudos de Caso

### Para estudantes:

1. **Escolha um caso** relacionado ao capítulo que você está estudando
2. **Leia o resumo** no início do notebook para entender o problema
3. **Execute as células** sequencialmente (Shift+Enter)
4. **Modifique os parâmetros** para explorar diferentes cenários
5. **Resolva os exercícios** propostos ao final do notebook

### Para professores:

1. **Selecione casos** adequados ao nível da sua turma
2. **Adapte os parâmetros** para contextualizar com sua região/indústria
3. **Use como base** para listas de exercícios ou projetos
4. **Incentive os alunos** a criarem seus próprios casos

---

## 🤝 Contribuindo com Novos Casos

Você é professor, pesquisador ou profissional e desenvolveu um estudo de caso interessante? **Contribua com o repositório!**

### 📝 Passo a passo:

1. **Fork** este repositório
2. **Copie o template** em [`../docs/template_estudo_caso.md`](../docs/template_estudo_caso.md)
3. **Crie seu notebook** seguindo a nomenclatura: `NN_X_Nome_Do_Caso.ipynb`
   - `NN` = número do capítulo (ex: 04)
   - `X` = número sequencial do caso naquele capítulo (ex: 3)
   - `Nome_Do_Caso` = descrição clara e concisa
4. **Preencha a documentação** seguindo o template
5. **Adicione o link** neste arquivo (`READMEcasos.md`)
6. **Abra um Pull Request** descrevendo o caso

### 📋 Template básico de um estudo de caso:

```markdown
# Estudo de Caso NN.X — Título do Caso

**Capítulo Associado:** Capítulo NN — Nome do Capítulo  
**Nível:** Graduação / Pós-Graduação  
**Tempo estimado:** X minutos  
**Autor:** Seu Nome  

---

## 📋 Resumo
[2-3 parágrafos descrevendo o problema]

## 🎯 Objetivos de Aprendizagem
- [Objetivo 1]
- [Objetivo 2]

## 🔧 Requisitos
- Bibliotecas: numpy, scipy, matplotlib
- Dados de entrada: [descrever]
- Pré-requisitos: [capítulos/conceitos]

## 📊 Descrição do Problema
### Contexto
[Descrição do cenário real]

### Dados do Problema
| Parâmetro | Símbolo | Valor | Unidade |
|-----------|---------|-------|---------|
| ...       | ...     | ...   | ...     |

### Equações Governantes
[Apresentar as equações principais]

## 💻 Solução
[Código Python com comentários]

## 📈 Resultados
[Figuras, tabelas, valores-chave]

## 🔍 Discussão
### Interpretação Física
[Análise dos resultados]

### Limitações
[Simplificações assumidas]

### Aplicações Práticas
[Onde esse modelo é usado]

## 📚 Referências
1. [Referência ao livro]
2. [Artigos, normas técnicas]

## 🔄 Navegação
- [Voltar ao Capítulo NN](../notebooks/NN_nome_capitulo.ipynb)
- [Índice de Casos](READMEcasos.md)
- [Repositório Principal](../README.md)