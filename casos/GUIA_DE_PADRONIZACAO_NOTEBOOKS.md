# Guia de Padronização — Notebooks Jupyter

## Fenômenos de Transporte: Fundamentos e Modelagem Computacional

**Versão:** 2.0
**Data:** Agosto de 2026
**Autor:** Jader Lugon Junior
**Contato:** 22 98124-7054 — jlugonjr@gmail.com — www.ambhidro.iff.edu.br

\---

## Sumário

1. [Objetivo e Escopo](#1-objetivo-e-escopo)
2. [Estrutura Obrigatória do Notebook](#2-estrutura-obrigatória-do-notebook)
3. [Cabeçalho](#3-cabeçalho)
4. [Diretrizes de Formatação](#4-diretrizes-de-formatação)
5. [Diretrizes de Rigor Técnico](#5-diretrizes-de-rigor-técnico)
6. [Diretrizes Pedagógicas](#6-diretrizes-pedagógicas)
7. [Navegação](#7-navegação)
8. [Nomenclatura de Arquivos](#8-nomenclatura-de-arquivos)
9. [Checklist de Revisão](#9-checklist-de-revisão)
10. [Bibliografia de Referência](#10-bibliografia-de-referência)
11. [Exemplo de Referência](#11-exemplo-de-referência)
12. [Conteúdo Programático por Capítulo](#12-conteúdo-programático-por-capítulo)

\---

## 1\. Objetivo e Escopo

Este documento define a estrutura, a formatação e os requisitos técnicos mínimos para **todos** os estudos de caso computacionais (notebooks Jupyter) que compõem a coleção do livro *Fenômenos de Transporte: Fundamentos e Modelagem Computacional*.

### 1.1 Princípio Central

O leitor deve ter uma **experiência de navegação idêntica** em todos os casos, independentemente do tema (hidrodinâmica, dispersão de poluentes, qualidade da água, transferência de calor, etc.), mantendo sempre o mesmo nível de rigor técnico e a mesma jornada pedagógica:

> \*\*Contextualizar → Formular → Verificar → Implementar → Visualizar → Analisar → Discutir\*\*

### 1.2 Domínios de Aplicação

|Domínio|Descrição|
|-|-|
|**Poluição hídrica**|Estudo de rios, lagos, estuários e oceanos|
|**Contaminação do solo**|Transporte de poluentes em meio poroso|
|**Poluição atmosférica**|Estudo de bacias aéreas|
|**Hidrodinâmica**|Canais abertos, reservatórios, redes de drenagem|

### 1.3 Público-Alvo

* Estudantes de pós-graduação em Engenharia Ambiental, Civil, Sanitária e áreas afins
* Pesquisadores em modelagem computacional ambiental
* Profissionais que buscam formação em ferramentas numéricas aplicadas ao meio ambiente

\---

## 2\. Estrutura Obrigatória do Notebook

Todo notebook deve conter **exatamente** as seções abaixo, na ordem indicada. A numeração e os ícones são **fixos** e não devem ser alterados.

|#|Seção|Ícone|Tipo de Célula|Conteúdo Obrigatório|
|-|-|-|-|-|
|—|Cabeçalho|—|Markdown|Título, metadados, resumo, objetivos|
|0|Configuração Inicial|⚙️|Código|Importação de bibliotecas, estilo de gráficos|
|1|Parâmetros|🌊 / ⚙️|Markdown + Código|Tabela de parâmetros + definição no código|
|2|Verificação / Validação|🔬|Markdown + Código|Verificação prévia (Manning, balanço, solução conhecida)|
|3|Formulação Matemática|📐|Markdown|Equações governantes, condições de contorno/inicial|
|4|Estabilidade / Critério Numérico|⚡|Markdown + Código|CFL, número de Peclet, número de Courant, etc.|
|5|Forçamento / Condição de Entrada|🌪️|Markdown + Código|Hidrograma, carga, condição de contorno variável|
|6|Implementação Numérica|🧮|Código|Esquemas numéricos (explícito e/ou implícito)|
|7|Visualização|📊|Código + Markdown|Gráficos com interpretação|
|8|Análise Quantitativa|📈|Código + Markdown|Métricas, tabela comparativa|
|9|Sensibilidade / Convergência|🔍|Código + Markdown|Variação de Δt, Δx, parâmetros|
|10|Discussão|💡|Markdown|Interpretação, limitações, aplicações práticas|
|11|Navegação|🔄|Markdown|Links para capítulo, outros casos, repositório|

### 2.1 Regras de Ordem

* As seções **não podem ser reordenadas**.
* Seções podem ser **subdivididas** (ex.: 6.1 Esquema Explícito, 6.2 Esquema Implícito).
* Se uma seção não se aplicar ao caso específico (ex.: não há análise de sensibilidade temporal), ela deve ser **mantida** com uma nota explicativa: *"Neste caso, a sensibilidade espacial não se aplica porque..."*
* **Nunca** misturar seções diferentes na mesma célula.

\---

## 3\. Cabeçalho

O cabeçalho é a **primeira célula markdown** do notebook e deve conter obrigatoriamente:

```markdown
# Estudo de Caso X.Y — \[Título Descritivo]

| Campo | Detalhe |
|:------|:--------|
| \*\*Capítulo Associado\*\* | Capítulo N — \[Título] |
| \*\*Nível\*\* | Graduação / Pós-Graduação |
| \*\*Tempo estimado\*\* | NN minutos |
| \*\*Autor\*\* | \[Nome completo] |
| \*\*Método numérico\*\* | \[Ex.: Diferenças Finitas — Explícito e Implícito] |
| \*\*Bibliografia\*\* | \[Referências principais com página/seção] |

---

## 📋 Resumo

\[2-3 frases situando o problema físico, o método numérico e o resultado esperado.
Deve mencionar: o fenômeno modelado, a equação governante, o esquema numérico
utilizado e a principal métrica de resultado.]

---

## 🎯 Objetivos de Aprendizagem

Ao final deste estudo de caso, o leitor será capaz de:

1. \[Verbo de ação] + \[conteúdo específico]
2. \[Verbo de ação] + \[conteúdo específico]
3. \[Verbo de ação] + \[conteúdo específico]
4. \[Verbo de ação] + \[conteúdo específico]
5. \[Verbo de ação] + \[conteúdo específico]
\[Entre 5 e 7 objetivos]
```

### 3.1 Regras do Cabeçalho

* O título deve seguir o formato: `Estudo de Caso X.Y — \[Tema]: \[Subtema]`
* O nível deve ser um dos valores: `Graduação`, `Pós-Graduação`, `Ambos`
* O tempo estimado deve ser um múltiplo de 15 minutos
* Os objetivos devem usar **verbos de ação** da taxonomia de Bloom:

  * *Aplicar, implementar, resolver, comparar, analisar, interpretar, avaliar, formular, verificar, calcular, modelar, simular*
* Os objetivos devem ser **verificáveis**: o leitor deve conseguir demonstrar que atingiu cada um ao final do notebook

\---

## 4\. Diretrizes de Formatação

### 4.1 Células Markdown

|Regra|Exemplo|
|-|-|
|Uma seção por célula|Não misturar Seção 1 e Seção 2|
|Títulos com ícone e numeração|`## 🌊 Seção 1: Parâmetros do Rio Macaé`|
|Equações em LaTeX (display)|`$$\\frac{\\partial C}{\\partial t} + u\\frac{\\partial C}{\\partial x} = E\\frac{\\partial^2 C}{\\partial x^2}$$`|
|Equações em LaTeX (inline)|`$c\_k = \\frac{5}{3}u$`|
|Observações pedagógicas|`> 💡 \*\*Observação:\*\* A onda se propaga de montante para jusante...`|
|Referências bibliográficas|`> 📖 \*\*Referência:\*\* Gobbi (s.d.), Seção 5.1.1; Lugon Junior et al. (2026), Cap. 5.`|
|Fórmulas com unidades|Sempre indicar unidades: `\[m³/s]`, `\[m²/s]`, `\[s/m^(1/3)]`|

### 4.2 Células de Código

#### 4.2.1 Separadores Visuais

Todo bloco de código deve iniciar com um separador:

```python
# ============================================================
# TÍTULO DO BLOCO
# ============================================================
```

#### 4.2.2 Comentários

* Comentários em **português**
* Explicar a **física**, não apenas o código
* Cada variável deve ter comentário com unidade

```python
B = 42.2            # Largura média do canal \[m]
h0 = 0.71           # Profundidade inicial (regime uniforme) \[m]
S0 = 1.0e-4         # Declividade do fundo \[m/m]
n\_manning = 0.035   # Coeficiente de rugosidade de Manning \[s/m^(1/3)]
```

#### 4.2.3 Funções

Toda função deve ter docstring no padrão NumPy:

```python
def hidrograma\_entrada(t\_horas):
    """
    Define o hidrograma de entrada Q(0, t).

    Parameters
    ----------
    t\_horas : float
        Tempo em horas.

    Returns
    -------
    float
        Vazão em m³/s.

    Notes
    -----
    Pico de 12.0 m³/s entre 2h e 6h, com rampas de 1.5h a 2h e 6h a 6.5h.
    """
```

#### 4.2.4 Vetorização

* **Usar operações NumPy vetorizadas** sempre que possível
* **Evitar loops Python puros** sobre arrays
* Exceção: montagem de matrizes tridiagonais (loop sobre nós é aceitável)

```python
# ✅ CORRETO (vetorizado)
h\_new\[1:] = h\[1:] - (dt / (dx \* B)) \* (Q\[1:] - Q\[:-1])

# ❌ INCORRETO (loop Python)
for i in range(1, N):
    h\_new\[i] = h\[i] - (dt / (dx \* B)) \* (Q\[i] - Q\[i-1])
```

#### 4.2.5 Prints Formatados

Resultados devem ser impressos com emojis e formatação:

```python
print("=" \* 60)
print(" RESULTADOS DA SIMULAÇÃO")
print("=" \* 60)
print(f"\\n📊 Atenuação de Pico:")
print(f"  • Explícito: {atenuacao\_exp:.1f}%")
print(f"  • Implícito: {atenuacao\_imp:.1f}%")
print(f"\\n⏱️ Desempenho Computacional:")
print(f"  • Explícito: {passos\_exp} passos, {tempo\_exp:.4f} s")
print(f"  • Implícito: {passos\_imp} passos, {tempo\_imp:.4f} s")
print(f"\\n✅ Simulação concluída com sucesso!")
```

### 4.3 Gráficos

|Requisito|Especificação|
|-|-|
|Estilo|`plt.style.use('seaborn-v0\_8-whitegrid')`|
|Título|`fontweight='bold'`, tamanho 14|
|Eixos|Rotulados com unidades: `'Distância \[km]'`|
|Legenda|Sempre presente quando houver múltiplas curvas|
|Grade|`alpha=0.3`|
|Tamanho padrão|`figsize=(12, 6)` simples; `(14, 10)` subplots|
|Após cada gráfico|Incluir observação pedagógica em markdown|

#### Exemplo de gráfico padronizado:

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(x/1000, Q\_exp, 'b-', label='Explícito (Δt=30s)', linewidth=2)
ax.plot(x/1000, Q\_imp, 'r--', label='Implícito (Δt=150s)', linewidth=2)
ax.set\_xlabel('Distância \[km]', fontsize=12)
ax.set\_ylabel('Vazão \[m³/s]', fontsize=12)
ax.set\_title('Hidrograma na Seção de Jusante', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight\_layout()
plt.show()
```

### 4.4 Tabelas

* **Tabelas comparativas**: gerar com `pandas.DataFrame.to\_markdown()` e exibir com `IPython.display.Markdown`
* **Tabelas de parâmetros**: em markdown na seção de parâmetros
* Sempre incluir **unidades** nas colunas
* Usar `display(Markdown(df.to\_markdown(index=False)))` para renderização

### 4.5 Equações

Toda equação governante deve ser apresentada em LaTeX com:

1. A equação em si
2. A definição de cada variável
3. As unidades de cada variável
4. A referência bibliográfica

Exemplo:

```markdown
A equação de onda cinemática para escoamento unidimensional é:

$$\\frac{\\partial h}{\\partial t} + \\frac{1}{B}\\frac{\\partial Q}{\\partial x} = 0$$

onde:
- $h$ = lâmina d'água \[m]
- $Q$ = vazão \[m³/s]
- $B$ = largura do canal \[m]
- $t$ = tempo \[s]
- $x$ = distância longitudinal \[m]

> 📖 \*\*Referência:\*\* Gobbi (s.d.), Seção 5.1.1, Eqs. 5.4–5.7.
```

\---

## 5\. Diretrizes de Rigor Técnico

### 5.1 Verificação Prévia (Obrigatória)

Todo estudo de caso deve incluir **pelo menos uma** verificação antes da simulação principal:

|Tipo de Verificação|Exemplo|
|-|-|
|Comparação com solução analítica|Manning, solução de decaimento exponencial|
|Balanço de massa|Regime permanente: entrada = saída|
|Consistência de parâmetros|$Q\_{\\text{Manning}} \\approx Q\_{\\text{ref}}$|
|Comparação com dados de campo|Vazão medida vs. calculada|
|Solução conhecida|Decaimento radioativo, difusão 1D|

#### Exemplo de verificação com Manning:

```python
# Verificação: Q\_Manning deve ser ≈ Q\_ref
Q\_Manning = (B / n\_manning) \* h0 \*\* (5.0 / 3.0) \* np.sqrt(S0)
erro = abs(Q\_Manning - Q\_ref) / Q\_ref \* 100
assert erro < 5.0, f"Erro de {erro:.1f}% na verificação com Manning"
```

### 5.2 Esquemas Numéricos

|Requisito|Detalhe|
|-|-|
|Dois esquemas (quando aplicável)|Explícito e implícito para comparação|
|CFL calculado e impresso|Antes da simulação explícita|
|Montagem do sistema linear|Mostrar diagonais para o implícito|
|Solução tridiagonal|Usar `scipy.linalg.solve\_banded`|
|Condições de contorno|Declaradas e justificadas|
|Condição inicial|Explicitada fisicamente|

#### Esquema Explícito (Upwind):

$$h\_i^{n+1} = h\_i^n - \\frac{\\Delta t}{\\Delta x \\cdot B}\\left(Q\_i^n - Q\_{i-1}^n\\right)$$

#### Esquema Implícito (Upwind com linearização):

$$h\_i^{n+1} + \\frac{\\Delta t}{\\Delta x \\cdot B}\\left(Q\_i^{n+1} - Q\_{i-1}^{n+1}\\right) = h\_i^n$$

Linearização: $Q^{n+1} \\approx Q^n + \\left.\\frac{dQ}{dh}\\right|^n (h^{n+1} - h^n)$

### 5.3 Condição CFL

A condição CFL deve ser **calculada e impressa** antes de qualquer simulação explícita:

$$\\text{CFL} = \\frac{c\_k \\cdot \\Delta t}{\\Delta x} \\leq 1$$

O código deve incluir:

```python
ck\_max = np.max(celeridade(h))
cfl = (ck\_max \* dt) / dx
print(f"CFL = {cfl:.4f}")
assert cfl <= 1.0, "CFL > 1: simulação instável!"
```

### 5.4 Métricas de Desempenho

Todo estudo de caso deve reportar:

|Métrica|Como Calcular|
|-|-|
|Tempo de CPU|`time.time()` antes e depois|
|Número de passos|Contador no loop temporal|
|CFL máximo|`max(ck \* dt / dx)`|
|Métricas físicas|Atenuação, tempo de trânsito, erro relativo|

### 5.5 Tabela Comparativa

Quando houver dois ou mais esquemas/cenários, incluir tabela comparativa com:

|Característica|Esquema A|Esquema B|
|-|-|-|
|Passo de tempo|...|...|
|Número de passos|...|...|
|Tempo de CPU|...|...|
|Estabilidade|...|...|
|Atenuação de pico|...|...|
|Indicação de uso|...|...|

### 5.6 Análise de Sensibilidade (Obrigatória)

Todo estudo de caso deve incluir **pelo menos uma** das seguintes análises:

|Tipo|Exemplo|
|-|-|
|Variação de Δt|15 s, 30 s, 60 s (explícito); 60 s, 150 s, 300 s (implícito)|
|Variação de Δx|50 m, 100 m, 200 m|
|Variação de parâmetro físico|Rugosidade, coeficiente de dispersão|
|Convergência|Comparação com solução refinada|

Resultados devem ser apresentados em **tabela** e **gráfico**.

### 5.7 Condições de Contorno

As condições de contorno devem ser:

1. **Declaradas** na formulação matemática (Seção 3)
2. **Implementadas** no código com comentário
3. **Justificadas** fisicamente

|Tipo|Quando Usar|Justificativa|
|-|-|-|
|Dirichlet (valor prescrito)|Montante com hidrograma conhecido|Vazão medida ou sintética|
|Neumann (gradiente nulo)|Jusante em onda cinemática|Informação só se propaga para jusante|
|Periódica|Domínio circular|Simetria|

\---

## 6\. Diretrizes Pedagógicas

### 6.1 Objetivos de Aprendizagem

* Entre **5 e 7** objetivos
* Verbos de ação da taxonomia de Bloom
* Objetivos verificáveis

### 6.2 Progressão do Notebook

A progressão deve seguir **rigorosamente** esta ordem:

```
1. Contextualização física (o que é o problema, por que é importante)
2. Formulação matemática (equações, condições de contorno/inicial)
3. Verificação (os parâmetros são consistentes?)
4. Implementação (código comentado)
5. Visualização (gráficos com interpretação)
6. Análise quantitativa (métricas, tabelas)
7. Sensibilidade (a solução converge?)
8. Discussão (o que os resultados significam, limitações, aplicações)
```

### 6.3 Observações Pedagógicas

Após **cada gráfico** ou resultado importante, incluir uma observação:

```markdown
> 💡 \*\*Observação:\*\*
> - A onda se propaga de montante (esquerda) para jusante (direita)
> - O pico de vazão diminui ao longo do rio (atenuação)
> - A frente da onda se alarga (dispersão numérica)
```

### 6.4 Discussão Final (Obrigatória)

A seção de discussão deve conter **obrigatoriamente**:

1. **Interpretação física** dos resultados principais (mínimo 3 pontos)
2. **Limitações do modelo** (mínimo 3 limitações)
3. **Aplicações práticas** (mínimo 2 aplicações)
4. **Conexão com a teoria** (referência às equações e conceitos do capítulo)

#### Exemplo de limitações:

```markdown
### Limitações do Modelo

- \*\*Onda cinemática:\*\* Despreza termos de inércia e gradiente de pressão.
  Para escoamentos com aceleração significativa, usar equações completas.
- \*\*Dispersão numérica:\*\* O esquema upwind de primeira ordem introduz
  difusão artificial. Esquemas de ordem superior reduzem esse efeito.
- \*\*Geometria simplificada:\*\* O modelo assume seção retangular constante.
  Rios naturais têm geometria variável.
```

#### Exemplo de aplicações práticas:

```markdown
### Aplicações Práticas

- \*\*Sistemas de alerta:\*\* O tempo de trânsito permite prever quando a
  cheia chegará a pontos críticos.
- \*\*Dimensionamento de estruturas:\*\* A variação de lâmina d'água define
  a altura mínima de margens e diques.
```

\---

## 7\. Navegação

### 7.1 Bloco de Navegação (Última Célula Markdown)

```markdown
---

## 🔄 Navegação

- \[📚 Voltar ao Capítulo N](../notebooks/NN\_Nome\_do\_Capitulo.ipynb)
- \[📂 Outros Estudos de Caso](README.md)
- \[🏠 Repositório Principal](../README.md)

---

<div align="center">

Estudo de Caso X.Y
Parte da coleção \*"Fenômenos de Transporte: Fundamentos e Modelagem Computacional"\*

</div>
```

### 7.2 Links Relativos

* Links para capítulos: `../notebooks/NN\_Titulo.ipynb`
* Links para outros casos: `README.md` (na pasta de casos)
* Link para repositório: `../README.md`

\---

## 8\. Nomenclatura de Arquivos

### 8.1 Notebooks

```
EC\_CC\_NN\_Tema\_Principal.ipynb
```

Onde:

* `EC` = Estudo de Caso
* `CC` = Número do capítulo (2 dígitos)
* `NN` = Número sequencial dentro do capítulo (2 dígitos)
* `Tema\_Principal` = Nome descritivo sem espaços (underscores)

### 8.2 Exemplos

|Arquivo|Descrição|
|-|-|
|`EC\_05\_01\_Rio\_Macae\_Hidrodinamica.ipynb`|Hidrodinâmica do Rio Macaé|
|`EC\_05\_02\_Dispersao\_Poluente\_Rio.ipynb`|Dispersão de poluente em rio|
|`EC\_06\_01\_Transferencia\_Calor\_Reservatorio.ipynb`|Transferência de calor|
|`EC\_07\_01\_Qualidade\_Agua\_Eutrofizacao.ipynb`|Eutrofização|
|`EC\_03\_01\_Balanco\_Massa\_Reator.ipynb`|Balanço de massa em reator|

### 8.3 Estrutura de Pastas

```
livro/
├── README.md
├── GUIA\_DE\_PADRONIZACAO\_NOTEBOOKS.md
├── notebooks/
│   ├── 01\_Fundamentos\_Modelagem.ipynb
│   ├── 02\_Fenomenos\_Transporte.ipynb
│   ├── 03\_Balancos\_Massa.ipynb
│   ├── 04\_Metodos\_Numericos.ipynb
│   ├── 05\_Hidrodinamica\_Canais\_Abertos.ipynb
│   ├── 06\_Poluicao\_Hidrica.ipynb
│   └── 07\_Qualidade\_Agua.ipynb
├── estudos\_de\_caso/
│   ├── README.md
│   ├── EC\_05\_01\_Rio\_Macae\_Hidrodinamica.ipynb
│   ├── EC\_05\_02\_Dispersao\_Poluente\_Rio.ipynb
│   └── ...
└── imagens/
    └── ...
```

\---

## 9\. Checklist de Revisão

Antes de publicar um estudo de caso, verificar **todos** os itens:

### 9.1 Formatação

* \[ ] Cabeçalho com tabela de metadados completa
* \[ ] Seções numeradas com ícones na ordem correta
* \[ ] Equações em LaTeX com definição de variáveis e unidades
* \[ ] Observações pedagógicas após gráficos
* \[ ] Referências bibliográficas nas seções teóricas
* \[ ] Bloco de navegação no final
* \[ ] Separadores visuais no código
* \[ ] Comentários em português no código
* \[ ] Docstrings em todas as funções

### 9.2 Rigor Técnico

* \[ ] Verificação prévia incluída e aprovada
* \[ ] Condição CFL calculada e impressa (se esquema explícito)
* \[ ] Dois esquemas numéricos (quando aplicável)
* \[ ] Código vetorizado (sem loops Python puros sobre arrays)
* \[ ] Métricas de desempenho reportadas (CPU, passos, CFL)
* \[ ] Tabela comparativa incluída
* \[ ] Análise de sensibilidade incluída
* \[ ] Condições de contorno declaradas e justificadas
* \[ ] Condição inicial explicitada

### 9.3 Pedagógico

* \[ ] 5 a 7 objetivos de aprendizagem com verbos de ação
* \[ ] Progressão: contexto → formulação → verificação → implementação → visualização → análise → sensibilidade → discussão
* \[ ] Discussão com interpretação, limitações (≥3) e aplicações (≥2)
* \[ ] Conexão com a teoria do capítulo
* \[ ] Observações pedagógicas após cada gráfico

### 9.4 Execução

* \[ ] Notebook executa sem erros do início ao fim
* \[ ] Todas as células de código produzem saída
* \[ ] Gráficos estão legíveis (títulos, eixos, legendas)
* \[ ] Tabelas estão formatadas corretamente
* \[ ] Não há células vazias ou com código comentado
* \[ ] Tempo de execução total < 5 minutos

\---

## 10\. Bibliografia de Referência

Os estudos de caso devem referenciar, quando aplicável:

|#|Referência|Uso Principal|
|-|-|-|
|1|**Schnoor, J. L.** *Environmental Modeling: Fate and Transport of Pollutants in Water, Air, and Soil.* Wiley-Interscience, 1996. ISBN 0-471-12436-2.|Fundamentos de transporte de poluentes|
|2|**Lugon Junior, J.; Telles, W.; Rodrigues, P. P.; Silva Neto, A. J.** *Inverse Problems in the Environmental Modelling of Rivers and Estuaries.* Springer Nature, 2026. ISBN 3032099366.|Modelagem de rios e estuários|
|3|**Gobbi, M. F.** *Introdução à Modelagem da Poluição Ambiental.* UFPR.|Conservação, transporte, processos físicos/químicos/biológicos, poluição hídrica|
|4|**Fisher, H. B. et al.** *Mixing in Inland and Coastal Waters.* Academic Press, 1979.|Mistura em rios e águas costeiras|
|5|**Brutsaert, W.** *Evaporation into the Atmosphere.* D. Reidel, 1982.|Evaporação e balanço de energia|

### 10.1 Formato de Citação nos Notebooks

```markdown
> 📖 \*\*Referência:\*\* Gobbi (s.d.), Cap. 5, Seção 5.1.1, Eqs. 5.4–5.7.
> 📖 \*\*Referência:\*\* Lugon Junior et al. (2026), Cap. 5.
> 📖 \*\*Referência:\*\* Schnoor (1996), Cap. 3.
```

\---

## 11\. Exemplo de Referência

O estudo de caso **EC\_05\_06\_Rio\_Macae\_Hidrodinamica.ipynb** serve como **modelo de referência** para todos os demais notebooks da coleção. Ele implementa todos os requisitos deste guia:

* Cabeçalho completo com metadados
* 11 seções na ordem correta com ícones
* Verificação com Manning
* Dois esquemas (explícito e implícito)
* Código vetorizado
* CFL calculado e impresso
* Tabela comparativa
* Análise de sensibilidade temporal
* Discussão com limitações e aplicações
* Navegação no rodapé

\---

## 12\. Conteúdo Programático por Capítulo

### Capítulo 1: Fundamentos e Motivação

**Conceitos-chave:**

* O que é um modelo matemático: `ENTRADAS → \[MODELO] → SAÍDAS`
* Aplicações ambientais (poluição hídrica, contaminação do solo, poluição atmosférica)
* Balanços de massa: `Acúmulo = Entrada - Saída ± Reações`
* Volume de controle
* Equação diferencial de crescimento populacional: $\\frac{\\partial y}{\\partial t} = cy$

**Referência:** Modelagem1 (Aula 1); Gobbi, Cap. 1

### Capítulo 2: Fenômenos de Transporte — Dispersão e Advecção

**Conceitos-chave:**

* Difusão molecular (cinética molecular, $D$)
* Difusão turbulenta (turbulência em microescala, $\\varepsilon\_m$)
* Dispersão (gradiente de velocidade, $E$)
* Ordem de grandeza: $D \\ll \\varepsilon\_m \\ll E$
* Advecção: $J = uCA = QC$
* Primeira Lei de Fick: $J\_m = -DA\\frac{dC}{dx}$
* Segunda Lei de Fick: $\\frac{\\partial C}{\\partial t} = D\\frac{\\partial^2 C}{\\partial x^2}$
* Equação de dispersão-advecção
* Coeficientes de dispersão (Liu, Elder)
* Comprimento de mistura (Barbosa, 2005)
* Número de Peclet: $Pe = \\frac{uL}{E}$

**Referência:** Modelagem2 (Aula 2); Gobbi, Cap. 2, Seções 2.3

### Capítulo 3: Conservação e Transporte

**Conceitos-chave:**

* Teorema do transporte de Reynolds
* Conservação da massa de um soluto
* Conservação da quantidade de movimento (Navier-Stokes)
* Conservação da energia
* Equação de estado
* Redução de dimensão (3D → 2D → 1D → 0D)
* Equações integradas na seção transversal
* Cargas (pontuais, distribuídas, instantâneas)

**Referência:** Gobbi, Cap. 2

### Capítulo 4: Método de Volumes Finitos

**Conceitos-chave:**

* Discretização do domínio
* Integração da equação diferencial no volume de controle
* Montagem do sistema $Ax = b$
* Coeficientes $a\_N, a\_S, a\_E, a\_W, a\_P$
* Esquemas explícito ($\\theta = t$) e implícito ($\\theta = t + \\Delta t$)
* Upwind (UDS): $c\_e = c\_P$, $c\_w = c\_W$
* Condições de contorno na montagem da matriz

**Referência:** Modelagem3 (Aula 3)

### Capítulo 5: Hidrodinâmica de Canais Abertos

**Conceitos-chave:**

* Equações de Saint-Venant
* Modelo de onda cinemática: $Q = \\frac{B}{n}h^{5/3}S\_0^{1/2}$
* Celeridade da onda cinemática: $c\_k = \\frac{5}{3}u$
* Condição CFL: $\\frac{c\_k \\Delta t}{\\Delta x} \\leq 1$
* Esquemas explícito e implícito
* Número de Froude: $Fr = \\frac{u}{\\sqrt{gh}}$
* Regime fluvial ($Fr < 1$) vs. torrencial ($Fr > 1$)

**Referência:** Gobbi, Cap. 5, Seção 5.1; Lugon Junior et al. (2026), Cap. 5

### Capítulo 6: Poluição Hídrica

**Conceitos-chave:**

* Rios e canais: transporte longitudinal, mistura transversal, mistura vertical
* Lagos e reservatórios: tempo de residência, estratificação, penetração convectiva, mistura por vento
* Estuários: mistura por cisalhamento da maré, maré aprisionada, intrusão salina
* Águas subterrâneas: fluxo de Darcy, condutividade hidráulica, equação de transporte em meio poroso

**Referência:** Gobbi, Cap. 5

### Capítulo 7: Processos Físicos, Químicos e Biológicos

**Conceitos-chave:**

* Radiação e balanço de energia
* Estratificação vertical e freqüência de Brunt-Väisälä
* Sedimentação (decantação, ressuspensão)
* Reações químicas (lei de Guldberg e Waage, ordem de reações)
* Equilíbrio químico (pH, oxidação-redução)
* Oxigênio dissolvido e DBO
* Nitrogênio, fósforo e algas
* Eutrofização

**Referência:** Gobbi, Cap. 3

\---

## 13\. Glossário de Ícones

|Ícone|Significado|Uso|
|-|-|-|
|📋|Resumo|Cabeçalho|
|🎯|Objetivos|Cabeçalho|
|🌊|Parâmetros / Água|Seção 1|
|⚙️|Configuração|Seção 0|
|🔬|Verificação|Seção 2|
|📐|Formulação|Seção 3|
|⚡|Estabilidade / CFL|Seção 4|
|🌪️|Forçamento|Seção 5|
|🧮|Implementação|Seção 6|
|📊|Visualização|Seção 7|
|📈|Análise|Seção 8|
|🔍|Sensibilidade|Seção 9|
|💡|Discussão|Seção 10|
|🔄|Navegação|Seção 11|
|📖|Referência|Ao longo do texto|
|✅|Sucesso|Em prints|
|❌|Erro / Instável|Em prints|
|⚠️|Atenção|Em prints|
|📦|Pacote|Em prints de configuração|
|⏱️|Tempo|Em prints de desempenho|
|📏|Dimensão|Em prints de verificação|

\---

## 14\. Versões e Atualizações

|Versão|Data|Alterações|
|-|-|-|
|1.0|Ago/2026|Versão inicial|
|2.0|Ago/2026|Inclusão do conteúdo programático, glossário de ícones, estrutura de pastas, exemplos detalhados|

\---

*Este guia pode ser atualizado à medida que novos tipos de estudos de caso forem incorporados à coleção. Alterações devem ser versionadas e comunicadas a todos os colaboradores.*

\---

<div align="center">

**Fenômenos de Transporte: Fundamentos e Modelagem Computacional**
Guia de Padronização de Notebooks — Versão 2.0

</div>

