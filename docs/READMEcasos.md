# Índice de Estudos de Caso

> **Coleção de problemas aplicados de engenharia**
> **Repositório:** github.com/JaderLugon/fenomenos-transporte-livro

---

## Sobre os Estudos de Caso

Esta pasta contém **estudos de caso aplicados** que complementam os capítulos
do livro *Fenômenos de Transporte: Fundamentos e Modelagem Computacional*.
Cada caso é um **Jupyter Notebook independente** que resolve um problema real
de engenharia usando os conceitos e ferramentas apresentados no capítulo
correspondente.

### Características dos casos

- **Autocontidos:** podem ser executados independentemente dos notebooks principais.
- **Documentados:** seguem um template padronizado com objetivos, dados, solução e discussão.
- **Reprodutíveis:** todos os dados e códigos estão incluídos.
- **Didáticos:** incluem interpretações físicas e análises de sensibilidade.
- **Extensíveis:** professores podem adaptar e criar novos casos.

### Estatísticas

| Indicador | Valor |
|:---|:---|
| Total de casos | 23 |
| Capítulos cobertos | 10 de 11 |
| Nível Graduação | 10 casos |
| Nível Pós-Graduação | 13 casos |
| Tempo médio de execução | 30 a 120 minutos |

---

## Convenção de Numeração

Os estudos de caso seguem duas regras de nomenclatura, conforme a sua origem.

### Casos publicados no livro

Casos que já constam no livro impresso recebem o número do capítulo e o número
da seção onde estão localizados. O formato é:

    EC_Capitulo_Secao_TemaPrincipal.ipynb

Exemplo: EC_05_06_Rio_Macae_Hidrodinamica.ipynb (Capítulo 5, Seção 5.6).

### Casos novos (contribuições da comunidade)

Casos novos, submetidos por colaboradores e ainda não publicados no livro,
recebem o número do capítulo, a letra X e um número sequencial crescente.
O formato é:

    EC_Capitulo_X_Sequencial_TemaPrincipal.ipynb

Exemplo: EC_05_X1_Profundidade_Normal_Canal_Trapezoidal.ipynb
(Capítulo 5, 1º caso adicional).

A letra **X** indica que o caso é um complemento aberto, não atrelado a uma
seção específica do livro impresso. O número sequencial cresce dentro de cada
capítulo.

### Regras importantes

- Nunca reutilizar um número sequencial, mesmo que um caso seja removido.
- Consultar este índice antes de criar um caso novo para verificar o próximo X disponível.
- Quando um caso X for incorporado ao livro, ele é renumerado para o formato de seção.
- O número do capítulo deve sempre ter 2 dígitos (04, 07, 11).

---

## Lista Completa de Estudos de Caso

### Capítulo 2 — Fundamentos dos Fluidos e Viscosidade

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 2.X1 | Classificador de Fluidos Não-Newtonianos | Graduação | 30 min | Ajuste de dados reológicos ao modelo de Lei de Potência (Ostwald-de Waele) |

### Capítulo 3 — Modelagem Matemática do Escoamento

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 3.X1 | Balanço de Massa em Reator CSTR | Graduação | 45 min | Resolução de EDO de primeira ordem com termo fonte |
| 3.X2 | Calculadora de Números Adimensionais | Graduação | 30 min | Cálculo de Re, Pe, Pr, Sc com classificação de regimes |

### Capítulo 4 — Escoamento em Tubulações e Bombeamento

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 4.7 | Sistema de Bombeamento em Prédio Residencial | Graduação | 60 min | Cálculo de perda de carga, seleção de bomba, análise de NPSH |
| 4.8 | Sistema Hidráulico para Elevação de Carga Pesada | Pós-Graduação | 90 min | Dimensionamento de circuito hidráulico industrial com sincronismo |
| 4.X1 | Solver Colebrook-White | Pós-Graduação | 45 min | Newton-Raphson para equação não-linear implícita |

### Capítulo 5 — Hidrodinâmica de Canais Abertos

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 5.6 | Hidrodinâmica do Rio Macaé | Pós-Graduação | 120 min | Simulação de onda de cheia com equações de Saint-Venant |
| 5.X1 | Profundidade Normal em Canal Trapezoidal | Graduação | 45 min | Resolução numérica da equação de Manning |

### Capítulo 6 — Percolação em Meio Poroso

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 6.6 | Percolação em Terreno com Textura Conhecida | Pós-Graduação | 90 min | Cálculo de perfil de potencial matricial com van Genuchten |
| 6.X1 | Curva de Retenção de van Genuchten | Graduação | 45 min | Comparação de curvas de retenção para diferentes texturas |

### Capítulo 7 — Fundamentos de Transferência de Calor

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 7.8 | Isolamento Térmico de Forno de Padaria | Graduação | 60 min | Dimensionamento de isolamento com convecção e radiação |
| 7.X1 | Circuito Térmico de Parede Composta | Graduação | 45 min | Analogia elétrica para paredes multicamadas |

### Capítulo 8 — Transferência de Calor em Solos

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 8.8 | Perfil Térmico Diurno em Solo | Pós-Graduação | 90 min | Solução numérica da equação de calor com k variável |
| 8.X1 | Estabilidade Numérica de Diferenças Finitas | Pós-Graduação | 60 min | Comparação de esquemas explícito, implícito e Crank-Nicolson |
| 8.X2 | Simulação Acoplada Calor-Umidade em Solo | Pós-Graduação | 60 min | Modelo acoplado de transporte de calor e umidade |

### Capítulo 9 — Trocadores de Calor

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 9.5 | Resfriamento de Óleo Hidráulico em Hidrelétrica | Graduação | 60 min | Dimensionamento de trocador de placas óleo-água |
| 9.6 | Condensador de Vapor para UTE 100 MW | Pós-Graduação | 120 min | Projeto completo de condensador casco-tubo com análise ambiental |
| 9.7 | Caldeira Industrial para Geração de Vapor | Pós-Graduação | 90 min | Dimensionamento de caldeira flamotubular com NR13 |

### Capítulo 10 — Aletas e Superfícies Estendidas

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 10.5 | Condensador a Ar (ACC) com Tubos Aletados | Pós-Graduação | 120 min | Projeto de condensador seco para regiões áridas |
| 10.6 | Dissipador Térmico para Processador | Graduação | 60 min | Dimensionamento de heat sink para CPU de computador |
| 10.7 | Análise Térmica de Aleta por Diferenças Finitas | Pós-Graduação | 90 min | Solução numérica da equação da aleta com refinamento de malha |

### Capítulo 11 — Transporte de Calor e Massa em Corpos Hídricos

| Num | Título | Nível | Tempo | Descrição |
|:---|:---|:---|:---|:---|
| 11.5 | Dispersão de Poluentes no Rio Macaé | Pós-Graduação | 120 min | Modelagem de transporte com coeficientes de Liu e Elder |
| 11.X1 | Difusão Artificial em Esquemas Upwind | Pós-Graduação | 60 min | Análise de erro numérico em esquemas de primeira ordem |

---

## Como Usar os Estudos de Caso

### Para estudantes

1. Escolha um caso relacionado ao capítulo que você está estudando.
2. Leia o resumo no início do notebook para entender o problema.
3. Execute as células sequencialmente (Shift+Enter).
4. Modifique os parâmetros para explorar diferentes cenários.
5. Resolva os exercícios propostos ao final do notebook.

### Para professores

1. Selecione casos adequados ao nível da sua turma.
2. Adapte os parâmetros para contextualizar com sua região ou indústria.
3. Use como base para listas de exercícios ou projetos.
4. Incentive os alunos a criarem seus próprios casos.

---

## Contribuindo com Novos Casos

Você é professor, pesquisador ou profissional e desenvolveu um estudo de caso
interessante? Contribua com o repositório!

### Passo a passo

1. Faça um **fork** deste repositório.
2. **Consulte a numeração:** verifique acima o próximo X disponível no capítulo desejado.
3. **Leia o guia completo** em docs/GUIA_COMPLETO_NOTEBOOKS.md.
4. **Crie seu notebook** seguindo a nomenclatura:

       EC_Capitulo_X_Sequencial_TemaPrincipal.ipynb

   Onde:
   - Capitulo = número do capítulo (2 dígitos, ex.: 04)
   - X = marcador literal de caso complementar
   - Sequencial = número crescente dentro do capítulo (ex.: 1, 2, 3)
   - TemaPrincipal = descrição clara e concisa

5. **Preencha a documentação** seguindo o template do guia.
6. **Adicione o link** neste arquivo (READMEcasos.md), na tabela do capítulo correspondente.
7. **Abra um Pull Request** descrevendo o caso.

### Checklist antes de submeter

- O notebook executa sem erros do início ao fim.
- Todos os parâmetros estão documentados com unidades.
- As unidades estão consistentes (preferencialmente SI).
- Os gráficos possuem legendas e rótulos claros.
- O código segue PEP 8 e possui docstrings.
- As referências estão completas.
- O tempo estimado de execução está correto.
- O nível (Graduação/Pós-Graduação) está claramente indicado.
- O nome do arquivo segue a convenção de numeração.

---

## Template Básico de um Estudo de Caso

Ao criar um novo caso, use a estrutura abaixo como ponto de partida.
O template completo e detalhado está em docs/GUIA_COMPLETO_NOTEBOOKS.md.

    # Estudo de Caso CC.XN — Título do Caso

    | Campo | Detalhe |
    |:------|:--------|
    | Capítulo Associado | Capítulo CC — Nome do Capítulo |
    | Nível | Graduação / Pós-Graduação |
    | Tempo estimado | NN minutos |
    | Autor | Seu Nome |
    | Método numérico | Método utilizado |
    | Bibliografia | Referências principais |

    ---

    ## Resumo
    Duas ou três frases descrevendo o problema, o método e o resultado esperado.

    ## Objetivos de Aprendizagem
    1. Objetivo 1
    2. Objetivo 2
    3. Objetivo 3
    4. Objetivo 4
    5. Objetivo 5

    ## Seção 0: Configuração Inicial
    ## Seção 1: Parâmetros do Problema
    ## Seção 2: Verificação Prévia
    ## Seção 3: Formulação Matemática
    ## Seção 4: Critério de Estabilidade
    ## Seção 5: Condições de Entrada
    ## Seção 6: Implementação Numérica
    ## Seção 7: Visualização dos Resultados
    ## Seção 8: Análise Quantitativa
    ## Seção 9: Análise de Sensibilidade
    ## Seção 10: Discussão
    ## Seção 11: Navegação

---

## Navegação

- Voltar ao Repositório Principal: ../README.md
- Guia Completo de Notebooks: ../docs/GUIA_COMPLETO_NOTEBOOKS.md
- Guia do Professor: ../docs/Guia_professor.md
- Guia de Contribuição: ../docs/Contribuindo.md

---

Coleção "Fenômenos de Transporte: Fundamentos e Modelagem Computacional"