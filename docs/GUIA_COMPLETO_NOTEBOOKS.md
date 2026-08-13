# Guia Completo de Estudos de Caso — Notebooks Jupyter
**Coleção: Fenômenos de Transporte — Fundamentos e Modelagem Computacional**

| Campo | Informação |
|:---|:---|
| **Versão** | 3.0 |
| **Data** | Agosto de 2026 |
| **Autor** | Jader Lugon Junior |
| **Instituição** | Instituto Federal Fluminense — Campus Macaé |
| **Contato** | jlugonjr@gmail.com — www.ambhidro.iff.edu.br |
| **Licença** | CC-BY-SA-4.0 (estudos de caso) / MIT (código) |

---

## Sumário

1. Objetivo e Escopo
2. Convenção de Numeração
3. Nomenclatura de Arquivos e Estrutura de Pastas
4. Estrutura Obrigatória do Notebook
5. Cabeçalho Padrão
6. Diretrizes de Formatação
7. Diretrizes de Rigor Técnico
8. Diretrizes Pedagógicas
9. Domínios de Aplicação
10. Conteúdo Programático por Capítulo
11. Checklist de Qualidade
12. Template Completo para Copiar
13. Navegação
14. Bibliografia de Referência
15. Glossário de Ícones
16. Histórico de Versões

---

## 1. Objetivo e Escopo

Este documento define a estrutura, a formatação, a nomenclatura e os requisitos
técnicos mínimos para todos os estudos de caso computacionais (notebooks
Jupyter) que compõem o repositório do livro "Fenômenos de Transporte:
Fundamentos e Modelagem Computacional".

### 1.1 Princípio Central

O leitor deve ter uma experiência de navegação idêntica em todos os casos,
independentemente do tema (hidrodinâmica, dispersão de poluentes, qualidade da
água, transferência de calor, escoamento em tubulações, etc.), mantendo sempre
o mesmo nível de rigor técnico e a mesma jornada pedagógica:

> Contextualizar → Formular → Verificar → Implementar → Visualizar → Analisar → Discutir

### 1.2 Público-Alvo

- Estudantes de graduação e pós-graduação em Engenharia Ambiental, Civil,
  Sanitária, Mecânica e áreas afins.
- Pesquisadores em modelagem computacional aplicada ao meio ambiente.
- Profissionais que buscam formação em ferramentas numéricas.
- Professores que desejam adaptar ou criar novos estudos de caso.

### 1.3 Documentos Relacionados

| Arquivo | Finalidade |
|:---|:---|
| docs/GUIA_COMPLETO_NOTEBOOKS.md | Este guia — padronização técnica e pedagógica |
| casos/READMEcasos.md | Índice de todos os estudos de caso |
| docs/Guia_professor.md | Sugestões de uso didático em sala de aula |
| docs/Contribuindo.md | Fluxo de contribuição e submissão de casos |

---

## 2. Convenção de Numeração

Os estudos de caso recebem identificadores que indicam a qual capítulo do
livro estão associados e a sua posição dentro daquele capítulo.

### 2.1 Casos Publicados no Livro

Casos que já constam no livro impresso recebem o número do capítulo e o número
da seção onde estão localizados. O formato do nome de arquivo é:

    EC_Capitulo_Secao_TemaPrincipal.ipynb

Onde:

- EC = prefixo fixo (Estudo de Caso)
- Capitulo = número do capítulo (2 dígitos)
- Secao = número da seção do livro (1 ou 2 dígitos)
- TemaPrincipal = nome descritivo, sem espaços, usando underscores

Exemplos:

| Arquivo | Significado |
|:---|:---|
| EC_04_07_Bombeamento_Predio_Residencial.ipynb | Capítulo 4, Seção 4.7 |
| EC_05_06_Rio_Macae_Hidrodinamica.ipynb | Capítulo 5, Seção 5.6 |
| EC_09_05_Resfriamento_Oleo_Hidraulico.ipynb | Capítulo 9, Seção 9.5 |
| EC_11_05_Dispersao_Poluentes_Rio_Macae.ipynb | Capítulo 11, Seção 11.5 |

### 2.2 Casos Novos (Contribuições da Comunidade)

Casos novos, submetidos por colaboradores e ainda não publicados no livro,
recebem o número do capítulo, a letra X e um número sequencial crescente.
O formato do nome de arquivo é:

    EC_Capitulo_X_Sequencial_TemaPrincipal.ipynb

Onde:

- Capitulo = número do capítulo ao qual o caso está associado (2 dígitos)
- X = marcador literal indicando caso complementar
- Sequencial = número crescente dentro do capítulo (1, 2, 3, ...)

Exemplos:

| Arquivo | Significado |
|:---|:---|
| EC_04_X1_Solver_Colebrook_White.ipynb | Capítulo 4, 1º caso adicional |
| EC_05_X1_Profundidade_Normal_Canal_Trapezoidal.ipynb | Capítulo 5, 1º caso adicional |
| EC_07_X1_Circuito_Termico_Parede_Composta.ipynb | Capítulo 7, 1º caso adicional |
| EC_11_X1_Difusao_Artificial_Upwind.ipynb | Capítulo 11, 1º caso adicional |

### 2.3 Regras da Numeração

1. Nunca reutilizar um número sequencial, mesmo que um caso seja removido.
2. Consultar o arquivo casos/READMEcasos.md antes de criar um caso novo para
   verificar o próximo X disponível no capítulo.
3. Quando um caso X for incorporado ao livro, ele é renumerado para o formato
   de seção.
4. Não misturar os dois formatos em um mesmo caso.
5. O número do capítulo deve sempre ter 2 dígitos (04, 07, 11).

---

## 3. Nomenclatura de Arquivos e Estrutura de Pastas

### 3.1 Regras Gerais

- Nomes de arquivo sem acentos ou caracteres especiais.
- Palavras separadas por underscores (_), sem espaços.
- Extensão .ipynb para notebooks.
- Sempre iniciar com o prefixo EC_ para estudos de caso.

### 3.2 Estrutura de Pastas do Repositório

    fenomenos-transporte-livro/
    |
    +-- README.md
    +-- requirements.txt
    +-- LICENSE
    +-- CONTRIBUTORS.md
    |
    +-- notebooks/
    |   +-- 01_Introducao_Analogias.ipynb
    |   +-- 02_Fundamentos_Fluidos.ipynb
    |   +-- 03_Modelagem_Matematica.ipynb
    |   +-- 04_Escoamento_Tubulacoes.ipynb
    |   +-- 05_Hidrodinamica_Canais.ipynb
    |   +-- 06_Percolacao_Meio_Poroso.ipynb
    |   +-- 07_Transferencia_Calor.ipynb
    |   +-- 08_Calor_em_Solos.ipynb
    |   +-- 09_Trocadores_Calor.ipynb
    |   +-- 10_Aletas_Superficies.ipynb
    |   +-- 11_Transporte_Calor_Massa.ipynb
    |
    +-- casos/
    |   +-- READMEcasos.md
    |   +-- EC_04_07_Bombeamento_Predio_Residencial.ipynb
    |   +-- EC_05_06_Rio_Macae_Hidrodinamica.ipynb
    |   +-- EC_05_X1_Profundidade_Normal_Canal_Trapezoidal.ipynb
    |   +-- EC_07_X1_Circuito_Termico_Parede_Composta.ipynb
    |   +-- dados/
    |       +-- exemplo_vazoes.csv
    |
    +-- src/
    |   +-- __init__.py
    |   +-- hidrodinamica.py
    |   +-- transferencia_calor.py
    |   +-- transporte_massa.py
    |
    +-- docs/
    |   +-- GUIA_COMPLETO_NOTEBOOKS.md
    |   +-- Guia_professor.md
    |   +-- Contribuindo.md
    |
    +-- imagens/
        +-- ...

---

## 4. Estrutura Obrigatória do Notebook

Todo notebook deve conter exatamente as seções abaixo, na ordem indicada.
A numeração e os ícones são fixos e não devem ser alterados.

| Nº | Seção | Ícone | Tipo de Célula | Conteúdo Obrigatório |
|:---:|:---|:---:|:---|:---|
| — | Cabeçalho | — | Markdown | Título, metadados, resumo, objetivos |
| 0 | Configuração Inicial | ⚙️ | Código | Importação de bibliotecas, estilo |
| 1 | Parâmetros | 🌊 | Markdown + Código | Tabela de parâmetros + código |
| 2 | Verificação / Validação | 🔬 | Markdown + Código | Verificação prévia |
| 3 | Formulação Matemática | 📐 | Markdown | Equações, condições de contorno |
| 4 | Estabilidade / Critério | ⚡ | Markdown + Código | CFL, Peclet, Courant |
| 5 | Forçamento / Entrada | 🌪️ | Markdown + Código | Hidrograma, carga, contorno |
| 6 | Implementação Numérica | 🧮 | Código | Esquemas numéricos |
| 7 | Visualização | 📊 | Código + Markdown | Gráficos com interpretação |
| 8 | Análise Quantitativa | 📈 | Código + Markdown | Métricas, tabela comparativa |
| 9 | Sensibilidade / Convergência | 🔍 | Código + Markdown | Variação de Δt, Δx, parâmetros |
| 10 | Discussão | 💡 | Markdown | Interpretação, limitações, aplicações |
| 11 | Navegação | 🔄 | Markdown | Links para capítulo e repositório |

### 4.1 Regras de Ordem

- As seções não podem ser reordenadas.
- Seções podem ser subdivididas (ex.: 6.1 Esquema Explícito, 6.2 Implícito).
- Se uma seção não se aplicar, ela deve ser mantida com nota explicativa.
- Nunca misturar seções diferentes na mesma célula.

---

## 5. Cabeçalho Padrão

O cabeçalho é a primeira célula markdown do notebook e deve conter:

    # Estudo de Caso X.Y — Título Descritivo

    | Campo | Detalhe |
    |:------|:--------|
    | Capítulo Associado | Capítulo N — Título |
    | Nível | Graduação / Pós-Graduação / Ambos |
    | Tempo estimado | NN minutos |
    | Autor | Nome completo |
    | Método numérico | Ex.: Diferenças Finitas — Explícito e Implícito |
    | Bibliografia | Referências principais com página/seção |

    ---

    ## Resumo
    Duas ou três frases situando o problema físico, o método numérico e o
    resultado esperado. Deve mencionar: o fenômeno modelado, a equação
    governante, o esquema numérico utilizado e a principal métrica de resultado.

    ---

    ## Objetivos de Aprendizagem
    Ao final deste estudo de caso, o leitor será capaz de:

    1. Verbo de ação + conteúdo específico
    2. Verbo de ação + conteúdo específico
    3. Verbo de ação + conteúdo específico
    4. Verbo de ação + conteúdo específico
    5. Verbo de ação + conteúdo específico

### 5.1 Regras do Cabeçalho

- Título no formato: Estudo de Caso X.Y — Tema: Subtema, onde X.Y segue a
  convenção de numeração (Seção 2).
- Nível: um dos valores Graduação, Pós-Graduação ou Ambos.
- Tempo estimado: múltiplo de 15 minutos (30, 45, 60, 90, 120).
- Objetivos: entre 5 e 7 objetivos, usando verbos de ação da taxonomia de
  Bloom: aplicar, implementar, resolver, comparar, analisar, interpretar,
  avaliar, formular, verificar, calcular, modelar, simular, dimensionar.
- Os objetivos devem ser verificáveis.

---

## 6. Diretrizes de Formatação

### 6.1 Células Markdown

| Regra | Descrição |
|:---|:---|
| Uma seção por célula | Não misturar Seção 1 e Seção 2 |
| Títulos com ícone e numeração | Ex.: "Seção 1: Parâmetros do Rio Macaé" |
| Equações em LaTeX | Display e inline |
| Observações pedagógicas | Bloco de citação com ícone de lâmpada |
| Referências bibliográficas | Bloco de citação com ícone de livro |
| Unidades sempre presentes | Ex.: m³/s, m²/s, W/m·K |

### 6.2 Células de Código

#### 6.2.1 Separadores Visuais

Todo bloco de código deve iniciar com um separador:

    # ============================================================
    # TÍTULO DO BLOCO
    # ============================================================

#### 6.2.2 Comentários

- Comentários em português.
- Explicar a física, não apenas o código.
- Cada variável deve ter comentário com unidade.

Exemplo:

    B = 42.2            # Largura média do canal [m]
    h0 = 0.71           # Profundidade inicial (regime uniforme) [m]
    S0 = 1.0e-4         # Declividade do fundo [m/m]
    n_manning = 0.035   # Coeficiente de rugosidade de Manning [s/m^(1/3)]

#### 6.2.3 Funções

Toda função deve ter docstring no padrão NumPy:

    def manning_vazao(n, A, Rh, S0):
        """
        Calcula a vazão pela equação de Manning (SI).

        Parâmetros
        ----------
        n : float
            Coeficiente de rugosidade de Manning [s/m^(1/3)].
        A : float
            Área molhada [m²].
        Rh : float
            Raio hidráulico [m].
        S0 : float
            Declividade do fundo [m/m].

        Retorna
        -------
        float
            Vazão [m³/s].

        Exemplo
        -------
        >>> manning_vazao(0.035, 30.0, 0.71, 1e-4)
        6.80
        """
        return (1.0 / n) * A * (Rh ** (2.0 / 3.0)) * (S0 ** 0.5)

#### 6.2.4 Vetorização

- Usar operações NumPy vetorizadas sempre que possível.
- Evitar loops Python puros sobre arrays.
- Exceção: montagem de matrizes tridiagonais (loop sobre nós é aceitável).

    # CORRETO (vetorizado)
    h_new[1:] = h[1:] - (dt / (dx * B)) * (Q[1:] - Q[:-1])

    # INCORRETO (loop Python puro)
    for i in range(1, N):
        h_new[i] = h[i] - (dt / (dx * B)) * (Q[i] - Q[i-1])

#### 6.2.5 Prints Formatados

Resultados devem ser impressos com emojis e formatação:

    print("=" * 60)
    print(" RESULTADOS DA SIMULAÇÃO")
    print("=" * 60)
    print(f"\n📊 Atenuação de Pico:")
    print(f"  • Explícito: {atenuacao_exp:.1f}%")
    print(f"  • Implícito: {atenuacao_imp:.1f}%")
    print(f"\n⏱️ Desempenho Computacional:")
    print(f"  • Explícito: {passos_exp} passos, {tempo_exp:.4f} s")
    print(f"  • Implícito: {passos_imp} passos, {tempo_imp:.4f} s")
    print(f"\n✅ Simulação concluída com sucesso!")

### 6.3 Gráficos

| Requisito | Especificação |
|:---|:---|
| Estilo | plt.style.use('seaborn-v0_8-whitegrid') |
| Título | fontweight='bold', tamanho 14 |
| Eixos | Rotulados com unidades |
| Legenda | Sempre presente com múltiplas curvas |
| Grade | alpha=0.3 |
| Tamanho padrão | figsize=(12, 6) simples; (14, 10) subplots |
| Após cada gráfico | Incluir observação pedagógica em markdown |

Exemplo de gráfico padronizado:

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x/1000, Q_exp, 'b-', label='Explícito (dt=30s)', linewidth=2)
    ax.plot(x/1000, Q_imp, 'r--', label='Implícito (dt=150s)', linewidth=2)
    ax.set_xlabel('Distância [km]', fontsize=12)
    ax.set_ylabel('Vazão [m³/s]', fontsize=12)
    ax.set_title('Hidrograma na Seção de Jusante', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

### 6.4 Tabelas

- Tabelas comparativas: gerar com pandas.DataFrame.to_markdown() e exibir com
  IPython.display.Markdown.
- Tabelas de parâmetros: em markdown na seção de parâmetros.
- Sempre incluir unidades nas colunas.
- Usar display(Markdown(df.to_markdown(index=False))) para renderização.

### 6.5 Equações

Toda equação governante deve ser apresentada em LaTeX com:

1. A equação em si.
2. A definição de cada variável.
3. As unidades de cada variável.
4. A referência bibliográfica.

Exemplo:

A equação de onda cinemática para escoamento unidimensional é:

    dh/dt + (1/B) * dQ/dx = 0

onde:

- h = lâmina d'água [m]
- Q = vazão [m³/s]
- B = largura do canal [m]
- t = tempo [s]
- x = distância longitudinal [m]

> Referência: Gobbi (s.d.), Seção 5.1.1, Eqs. 5.4–5.7.

---

## 7. Diretrizes de Rigor Técnico

### 7.1 Verificação Prévia (Obrigatória)

Todo estudo de caso deve incluir pelo menos uma verificação antes da simulação
principal:

| Tipo de Verificação | Exemplo |
|:---|:---|
| Comparação com solução analítica | Manning, decaimento exponencial |
| Balanço de massa | Regime permanente: entrada = saída |
| Consistência de parâmetros | Q_Manning ≈ Q_ref |
| Comparação com dados de campo | Vazão medida vs. calculada |
| Solução conhecida | Decaimento radioativo, difusão 1D |

Exemplo de verificação com Manning:

    # Verificação: Q_Manning deve ser aproximadamente igual a Q_ref
    Q_Manning = (B / n_manning) * h0 ** (5.0 / 3.0) * np.sqrt(S0)
    erro = abs(Q_Manning - Q_ref) / Q_ref * 100
    assert erro < 5.0, f"Erro de {erro:.1f}% na verificação com Manning"

### 7.2 Esquemas Numéricos

| Requisito | Detalhe |
|:---|:---|
| Dois esquemas (quando aplicável) | Explícito e implícito para comparação |
| CFL calculado e impresso | Antes da simulação explícita |
| Montagem do sistema linear | Mostrar diagonais para o implícito |
| Solução tridiagonal | Usar scipy.linalg.solve_banded |
| Condições de contorno | Declaradas e justificadas |
| Condição inicial | Explicitada fisicamente |

Esquema Explícito (Upwind):

    h_i(n+1) = h_i(n) - (dt / (dx * B)) * (Q_i(n) - Q_(i-1)(n))

Esquema Implícito (Upwind com linearização):

    h_i(n+1) + (dt / (dx * B)) * (Q_i(n+1) - Q_(i-1)(n+1)) = h_i(n)

Linearização:

    Q(n+1) ≈ Q(n) + (dQ/dh)_n * (h(n+1) - h(n))

### 7.3 Condição CFL

A condição CFL deve ser calculada e impressa antes de qualquer simulação
explícita:

    CFL = (c_k * dt) / dx <= 1

O código deve incluir:

    ck_max = np.max(celeridade(h))
    cfl = (ck_max * dt) / dx
    print(f"CFL = {cfl:.4f}")
    assert cfl <= 1.0, "CFL > 1: simulação instável!"

### 7.4 Métricas de Desempenho

Todo estudo de caso deve reportar:

| Métrica | Como Calcular |
|:---|:---|
| Tempo de CPU | time.time() antes e depois |
| Número de passos | Contador no loop temporal |
| CFL máximo | max(ck * dt / dx) |
| Métricas físicas | Atenuação, tempo de trânsito, erro relativo |

### 7.5 Tabela Comparativa

Quando houver dois ou mais esquemas/cenários, incluir tabela comparativa com:

| Característica | Esquema A | Esquema B |
|:---|:---|:---|
| Passo de tempo | ... | ... |
| Número de passos | ... | ... |
| Tempo de CPU | ... | ... |
| Estabilidade | ... | ... |
| Atenuação de pico | ... | ... |
| Indicação de uso | ... | ... |

### 7.6 Análise de Sensibilidade (Obrigatória)

Todo estudo de caso deve incluir pelo menos uma das seguintes análises:

| Tipo | Exemplo |
|:---|:---|
| Variação de dt | 15 s, 30 s, 60 s (explícito); 60 s, 150 s, 300 s (implícito) |
| Variação de dx | 50 m, 100 m, 200 m |
| Variação de parâmetro físico | Rugosidade, coeficiente de dispersão |
| Convergência | Comparação com solução refinada |

Resultados devem ser apresentados em tabela e gráfico.

### 7.7 Condições de Contorno

As condições de contorno devem ser declaradas na formulação matemática (Seção
3), implementadas no código com comentário e justificadas fisicamente.

| Tipo | Quando Usar | Justificativa |
|:---|:---|:---|
| Dirichlet (valor prescrito) | Montante com hidrograma conhecido | Vazão medida ou sintética |
| Neumann (gradiente nulo) | Jusante em onda cinemática | Informação só se propaga para jusante |
| Periódica | Domínio circular | Simetria |

---

## 8. Diretrizes Pedagógicas

### 8.1 Objetivos de Aprendizagem

- Entre 5 e 7 objetivos.
- Verbos de ação da taxonomia de Bloom.
- Objetivos verificáveis.

### 8.2 Progressão do Notebook

A progressão deve seguir rigorosamente esta ordem:

1. Contextualização física (o que é o problema, por que é importante)
2. Formulação matemática (equações, condições de contorno/inicial)
3. Verificação (os parâmetros são consistentes?)
4. Implementação (código comentado)
5. Visualização (gráficos com interpretação)
6. Análise quantitativa (métricas, tabelas)
7. Sensibilidade (a solução converge?)
8. Discussão (o que os resultados significam, limitações, aplicações)

### 8.3 Observações Pedagógicas

Após cada gráfico ou resultado importante, incluir uma observação:

> Observação:
> - A onda se propaga de montante (esquerda) para jusante (direita)
> - O pico de vazão diminui ao longo do rio (atenuação)
> - A frente da onda se alarga (dispersão numérica)

### 8.4 Discussão Final (Obrigatória)

A seção de discussão deve conter obrigatoriamente:

- Interpretação física dos resultados principais (mínimo 3 pontos).
- Limitações do modelo (mínimo 3 limitações).
- Aplicações práticas (mínimo 2 aplicações).
- Conexão com a teoria (referência às equações e conceitos do capítulo).

Exemplo de limitações:

    Limitações do Modelo
    - Onda cinemática: Despreza termos de inércia e gradiente de pressão.
      Para escoamentos com aceleração significativa, usar equações completas.
    - Dispersão numérica: O esquema upwind de primeira ordem introduz
      difusão artificial. Esquemas de ordem superior reduzem esse efeito.
    - Geometria simplificada: O modelo assume seção retangular constante.
      Rios naturais têm geometria variável.

Exemplo de aplicações práticas:

    Aplicações Práticas
    - Sistemas de alerta: O tempo de trânsito permite prever quando a
      cheia chegará a pontos críticos.
    - Dimensionamento de estruturas: A variação de lâmina d'água define
      a altura mínima de margens e diques.

---

## 9. Domínios de Aplicação

O livro abrange fenômenos de transporte em múltiplos meios. Os estudos de caso
podem se enquadrar nos seguintes domínios:

| Domínio | Descrição | Exemplos |
|:---|:---|:---|
| Poluição hídrica | Estudo de rios, lagos, estuários e oceanos | Dispersão de poluentes, DBO/OD, eutrofização |
| Contaminação do solo | Transporte de poluentes em meio poroso | Percolação, fluxo de Darcy, pluma de contaminação |
| Poluição atmosférica | Estudo de bacias aéreas | Dispersão de gases, camadas limite |
| Hidrodinâmica | Canais abertos, reservatórios, drenagem | Onda de cheia, Saint-Venant, onda cinemática |
| Transferência de calor | Condução, convecção, radiação | Trocadores, aletas, isolamento térmico |
| Mecânica dos fluidos | Escoamento em tubulações e bombeamento | Perda de carga, NPSH, sistemas hidráulicos |

---

## 10. Conteúdo Programático por Capítulo

Esta seção orienta a associação de novos casos ao capítulo correto.

### Capítulo 1 — Introdução às Analogias / Fundamentos e Motivação

Conceitos-chave:

- O que é um modelo matemático: ENTRADAS → MODELO → SAÍDAS
- Aplicações ambientais (poluição hídrica, solo, atmosfera)
- Balanços de massa: Acúmulo = Entrada − Saída ± Reações
- Volume de controle
- Equação diferencial de crescimento populacional: dy/dt = c*y

> Referência: Modelagem1 (Aula 1); Gobbi, Cap. 1.

### Capítulo 2 — Fundamentos dos Fluidos e Viscosidade

Conceitos-chave:

- Propriedades dos fluidos, viscosidade dinâmica e cinemática
- Fluidos newtonianos e não-newtonianos (Lei de Potência de Ostwald-de Waele)
- Reologia e ajuste de dados experimentais

### Capítulo 3 — Modelagem Matemática do Escoamento

Conceitos-chave:

- Teorema do transporte de Reynolds
- Conservação da massa de um soluto
- Conservação da quantidade de movimento (Navier-Stokes)
- Conservação da energia
- Equação de estado
- Redução de dimensão (3D → 2D → 1D → 0D)
- Equações integradas na seção transversal
- Cargas (pontuais, distribuídas, instantâneas)
- Números adimensionais (Re, Pe, Pr, Sc)

> Referência: Gobbi, Cap. 2; Modelagem1 (Aula 1).

### Capítulo 4 — Escoamento em Tubulações e Bombeamento

Conceitos-chave:

- Perda de carga distribuída (Darcy-Weisbach) e localizada
- Equação de Colebrook-White e fator de atrito
- Seleção de bombas, curva do sistema, NPSH
- Sistemas hidráulicos industriais

### Capítulo 5 — Hidrodinâmica de Canais Abertos

Conceitos-chave:

- Equações de Saint-Venant (continuidade e quantidade de movimento)
- Modelo de onda cinemática: Q = (B/n) * h^(5/3) * S0^(1/2)
- Celeridade da onda cinemática: c_k = (5/3) * u
- Condição CFL: (c_k * dt) / dx <= 1
- Esquemas explícito e implícito
- Número de Froude: Fr = u / sqrt(g*h)
- Regime fluvial (Fr < 1) vs. torrencial (Fr > 1)
- Profundidade normal (Manning)

> Referência: Gobbi, Cap. 5, Seção 5.1; Lugon Junior et al. (2026), Cap. 5.

### Capítulo 6 — Percolação em Meio Poroso

Conceitos-chave:

- Fluxo de Darcy: q = -K * grad(h)
- Condutividade hidráulica e carga hidráulica
- Curva de retenção de van Genuchten
- Zona saturada e não-saturada, franja capilar
- Equação de transporte em meio poroso
- Coeficientes de dispersão (Saffman), número de Peclet

> Referência: Gobbi, Cap. 5, Seção 5.4.

### Capítulo 7 — Fundamentos de Transferência de Calor

Conceitos-chave:

- Condução (Lei de Fourier), convecção (Lei de Newton), radiação
  (Stefan-Boltzmann)
- Analogia elétrica para paredes multicamadas
- Resistência térmica, isolamento
- Balanço de energia em superfícies

> Referência: Gobbi, Cap. 3, Seção 3.1–3.2; Incropera.

### Capítulo 8 — Transferência de Calor em Solos

Conceitos-chave:

- Equação do calor com condutividade variável k(theta)
- Esquemas explícito, implícito e Crank-Nicolson
- Estabilidade numérica
- Simulação acoplada calor-umidade

### Capítulo 9 — Trocadores de Calor

Conceitos-chave:

- Coeficiente global de transferência de calor (U)
- Diferença de temperatura média logarítmica (LMTD)
- Método NTU-efetividade
- Trocadores casco-tubo, placas, caldeiras, condensadores

### Capítulo 10 — Aletas e Superfícies Estendidas

Conceitos-chave:

- Equação da aleta (diferenças finitas e volumes finitos)
- Eficiência e efetividade de aletas
- Refinamento de malha e convergência
- Dissipadores térmicos e condensadores a ar

### Capítulo 11 — Transporte de Calor e Massa em Corpos Hídricos

Conceitos-chave:

- Equação de dispersão-advecção
- Coeficientes de dispersão longitudinal (Liu), transversal (Elder),
  vertical (Jobson-Sayre, Csanady)
- Número de Peclet: Pe = u*L/E
- Comprimento de mistura (Barbosa, 2005)
- Método de Volumes Finitos: montagem do sistema Ax=b
- Coeficientes a_N, a_S, a_E, a_W, a_P
- Esquemas explícito (theta=t) e implícito (theta=t+dt)
- Upwind (UDS): c_e = c_P, c_w = c_W

> Referência: Modelagem2, Modelagem3; Gobbi, Cap. 2.3 e Cap. 5.

---

## 11. Checklist de Qualidade

Antes de publicar um estudo de caso, verificar todos os itens.

### 11.1 Formatação

- [ ] Cabeçalho com tabela de metadados completa
- [ ] Seções numeradas com ícones na ordem correta
- [ ] Equações em LaTeX com definição de variáveis e unidades
- [ ] Observações pedagógicas após gráficos
- [ ] Referências bibliográficas nas seções teóricas
- [ ] Bloco de navegação no final
- [ ] Separadores visuais no código
- [ ] Comentários em português no código
- [ ] Docstrings em todas as funções

### 11.2 Rigor Técnico

- [ ] Verificação prévia incluída e aprovada
- [ ] Condição CFL calculada e impressa (se esquema explícito)
- [ ] Dois esquemas numéricos (quando aplicável)
- [ ] Código vetorizado (sem loops Python puros sobre arrays)
- [ ] Métricas de desempenho reportadas (CPU, passos, CFL)
- [ ] Tabela comparativa incluída
- [ ] Análise de sensibilidade incluída
- [ ] Condições de contorno declaradas e justificadas
- [ ] Condição inicial explicitada

### 11.3 Pedagógico

- [ ] 5 a 7 objetivos de aprendizagem com verbos de ação
- [ ] Progressão: contexto → formulação → verificação → implementação →
      visualização → análise → sensibilidade → discussão
- [ ] Discussão com interpretação, limitações (3 ou mais) e aplicações (2 ou mais)
- [ ] Conexão com a teoria do capítulo
- [ ] Observações pedagógicas após cada gráfico

### 11.4 Execução

- [ ] Notebook executa sem erros do início ao fim
- [ ] Todas as células de código produzem saída
- [ ] Gráficos estão legíveis (títulos, eixos, legendas)
- [ ] Tabelas estão formatadas corretamente
- [ ] Não há células vazias ou com código comentado
- [ ] Tempo de execução total menor que 5 minutos

---

## 12. Template Completo para Copiar

Ao criar um novo estudo de caso, copie a estrutura abaixo e preencha.

### 12.1 Metadados (início do notebook)

    # Estudo de Caso CC.XN — Título Descritivo

    | Campo | Detalhe |
    |:------|:--------|
    | Capítulo Associado | Capítulo CC — Título |
    | Nível | Graduação / Pós-Graduação |
    | Tempo estimado | 60 minutos |
    | Autor | Seu Nome |
    | Instituição | Sua Instituição |
    | Data de criação | AAAA-MM-DD |
    | Método numérico | Método |
    | Licença | CC-BY-SA-4.0 |

### 12.2 Objetivos

    ## Objetivos de Aprendizagem
    1. Calcular grandeza a partir de dados
    2. Implementar método numérico em Python
    3. Comparar esquema A com esquema B
    4. Analisar a influência de parâmetro
    5. Interpretar fisicamente os resultados

### 12.3 Estrutura de Seções

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

### 12.4 Bloco de Navegação Final

    ---
    ## Navegação
    - Voltar ao Capítulo N: ../notebooks/NN_Titulo.ipynb
    - Outros Estudos de Caso: READMEcasos.md
    - Repositório Principal: ../README.md

    ---
    Estudo de Caso CC.XN
    Coleção "Fenômenos de Transporte: Fundamentos e Modelagem Computacional"

---

## 13. Navegação

### 13.1 Bloco de Navegação (Última Célula Markdown)

    ---
    ## Navegação
    - Voltar ao Capítulo N
    - Outros Estudos de Caso
    - Repositório Principal
    ---

### 13.2 Links Relativos

- Links para capítulos: ../notebooks/NN_Titulo.ipynb
- Links para outros casos: READMEcasos.md (na pasta de casos)
- Link para repositório: ../README.md

---

## 14. Bibliografia de Referência

Os estudos de caso devem referenciar, quando aplicável:

| Nº | Referência | Uso Principal |
|:---:|:---|:---|
| 1 | Schnoor, J. L. Environmental Modeling: Fate and Transport of Pollutants in Water, Air, and Soil. Wiley-Interscience, 1996. ISBN 0-471-12436-2. | Fundamentos de transporte de poluentes |
| 2 | Lugon Junior, J.; Telles, W.; Rodrigues, P. P.; Silva Neto, A. J. Inverse Problems in the Environmental Modelling of Rivers and Estuaries. Springer Nature, 2026. ISBN 3032099366. | Modelagem de rios e estuários |
| 3 | Gobbi, M. F. Introdução à Modelagem da Poluição Ambiental. UFPR. | Conservação, transporte, processos físicos/químicos/biológicos, poluição hídrica |
| 4 | Fisher, H. B. et al. Mixing in Inland and Coastal Waters. Academic Press, 1979. | Mistura em rios e águas costeiras |
| 5 | Incropera, F. P. et al. Fundamentos de Transferência de Calor e de Massa. LTC. | Calor e massa |
| 6 | Çengel, Y. A.; Cimbala, J. M. Mecânica dos Fluidos. McGraw-Hill. | Fluidos |

### 14.1 Formato de Citação nos Notebooks

> Referência: Gobbi (s.d.), Cap. 5, Seção 5.1.1, Eqs. 5.4–5.7.
> Referência: Lugon Junior et al. (2026), Cap. 5.
> Referência: Schnoor (1996), Cap. 3.
> Referência: Incropera et al. (2017), Cap. 3.

---

## 15. Glossário de Ícones

| Ícone | Significado | Uso |
|:---:|:---|:---|
| 📋 | Resumo | Cabeçalho |
| 🎯 | Objetivos | Cabeçalho |
| 🌊 | Parâmetros / Água | Seção 1 |
| ⚙️ | Configuração | Seção 0 |
| 🔬 | Verificação | Seção 2 |
| 📐 | Formulação | Seção 3 |
| ⚡ | Estabilidade / CFL | Seção 4 |
| 🌪️ | Forçamento | Seção 5 |
| 🧮 | Implementação | Seção 6 |
| 📊 | Visualização | Seção 7 |
| 📈 | Análise | Seção 8 |
| 🔍 | Sensibilidade | Seção 9 |
| 💡 | Discussão | Seção 10 |
| 🔄 | Navegação | Seção 11 |
| 📖 | Referência | Ao longo do texto |
| ✅ | Sucesso | Em prints |
| ❌ | Erro / Instável | Em prints |
| ⚠️ | Atenção | Em prints |
| 📦 | Pacote | Em prints de configuração |
| ⏱️ | Tempo | Em prints de desempenho |
| 📏 | Dimensão | Em prints de verificação |

---

## 16. Histórico de Versões

| Versão | Data | Alterações |
|:---:|:---:|:---|
| 1.0 | Ago/2026 | Versão inicial |
| 2.0 | Ago/2026 | Conteúdo programático, glossário de ícones, estrutura de pastas |
| 3.0 | Ago/2026 | Unificação com template; convenção de numeração X para casos novos; domínios de aplicação ampliados; checklist consolidado |

---

Este guia pode ser atualizado à medida que novos tipos de estudos de caso
forem incorporados à coleção. Alterações devem ser versionadas e comunicadas a
todos os colaboradores.

---

Fenômenos de Transporte: Fundamentos e Modelagem Computacional
Guia Completo de Notebooks — Versão 3.0 — Agosto de 2026