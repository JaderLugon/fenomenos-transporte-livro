# Guia do Professor

**Bem-vindo(a)!** Este guia apresenta sugestões de como utilizar os materiais
deste repositório em suas disciplinas, aproveitando ao máximo a integração com
o livro "Fenômenos de Transporte: Fundamentos e Modelagem Computacional".

---

## Sumário

1. Visão Geral do Material
2. Estratégias Pedagógicas
3. Trilhas de Aprendizagem
4. Recursos Técnicos
5. Avaliação de Alunos
6. Criando Seus Próprios Estudos de Caso
7. Comunidade e Colaboração
8. Referências Pedagógicas

---

## 1. Visão Geral do Material

### 1.1 Estrutura do Repositório

| Pasta | Conteúdo | Uso Principal |
|:---|:---|:---|
| notebooks/ | 11 notebooks principais (um por capítulo) | Material de referência, QR Codes do livro |
| casos/ | Estudos de caso aplicados | Exercícios práticos, projetos, demonstrações |
| src/ | Módulos Python reutilizáveis | Código limpo para importação nos notebooks |
| docs/ | Documentação (guia unificado, guia do professor, contribuição) | Referência para uso e contribuição |

### 1.2 Integração com o Livro

Cada capítulo do livro possui um QR Code que direciona o aluno para o notebook
correspondente no repositório. Essa integração permite:

- **Acesso imediato** a códigos executáveis durante a leitura.
- **Reprodutibilidade** dos exemplos apresentados no livro.
- **Extensão prática** dos conceitos teóricos.

### 1.3 Convenção de Numeração dos Casos

Os estudos de caso seguem duas regras de nomenclatura, conforme a sua origem.

#### Casos publicados no livro

Recebem o número do capítulo e da seção onde estão localizados:

    EC_Capitulo_Secao_TemaPrincipal.ipynb

Exemplo: EC_05_06_Rio_Macae_Hidrodinamica.ipynb (Capítulo 5, Seção 5.6).

#### Casos novos (contribuições da comunidade)

Recebem o número do capítulo, a letra X e um número sequencial crescente:

    EC_Capitulo_X_Sequencial_TemaPrincipal.ipynb

Exemplo: EC_05_X1_Profundidade_Normal_Canal_Trapezoidal.ipynb
(Capítulo 5, 1º caso adicional).

A letra X indica que o caso é um complemento aberto, não atrelado a uma seção
específica do livro impresso.

### 1.4 Domínios de Aplicação

O livro abrange fenômenos de transporte em múltiplos meios:

| Domínio | Descrição | Exemplos |
|:---|:---|:---|
| Poluição hídrica | Estudo de rios, lagos, estuários e oceanos | Dispersão de poluentes, DBO/OD, eutrofização |
| Contaminação do solo | Transporte de poluentes em meio poroso | Percolação, fluxo de Darcy, pluma de contaminação |
| Poluição atmosférica | Estudo de bacias aéreas | Dispersão de gases, camadas limite |
| Hidrodinâmica | Canais abertos, reservatórios, drenagem | Onda de cheia, Saint-Venant, onda cinemática |
| Transferência de calor | Condução, convecção, radiação | Trocadores, aletas, isolamento térmico |
| Mecânica dos fluidos | Escoamento em tubulações e bombeamento | Perda de carga, NPSH, sistemas hidráulicos |

---

## 2. Estratégias Pedagógicas

### 2.1 Demonstração em Sala de Aula

**Objetivo:** Ilustrar conceitos teóricos com exemplos computacionais.

**Como fazer:**

1. Projete o notebook em tela compartilhada.
2. Execute as células passo a passo, explicando cada etapa.
3. Modifique parâmetros em tempo real para explorar diferentes cenários.
4. Peça aos alunos para prever resultados antes da execução.

**Exemplo:** No Capítulo 4 (Escoamento em Tubulações), demonstre como a perda
de carga varia com o diâmetro usando o caso
EC_04_07_Bombeamento_Predio_Residencial.ipynb.

### 2.2 Exercício Guiado

**Objetivo:** Consolidar conceitos através da prática.

**Como fazer:**

1. Forneça o notebook com algumas células em branco.
2. Oriente os alunos a preencherem as lacunas.
3. Discuta as soluções em plenária.
4. Compare diferentes abordagens.

**Dica:** Use o guia docs/GUIA_COMPLETO_NOTEBOOKS.md para criar exercícios
estruturados seguindo o mesmo template.

### 2.3 Projeto Semestral

**Objetivo:** Desenvolver competências de modelagem computacional.

**Sugestões de projetos:**

| Nível | Tema | Complexidade |
|:---|:---|:---|
| Graduação | Dimensionamento de sistema de abastecimento predial | Média |
| Graduação | Análise térmica de dissipador de CPU | Média |
| Pós-Graduação | Calibração de modelo de dispersão em rio | Alta |
| Pós-Graduação | Estimação de parâmetros por problema inverso | Alta |

### 2.4 Aula Invertida (Flipped Classroom)

**Objetivo:** Maximizar o tempo de interação em sala.

**Como fazer:**

1. **Antes da aula:** Alunos estudam o capítulo do livro e executam o notebook.
2. **Em sala:** Discutam dúvidas e resolvem problemas avançados.
3. **Pós-aula:** Alunos criam variações do estudo de caso.

---

## 3. Trilhas de Aprendizagem

### 3.1 Trilha de Graduação

**Foco:** Aplicação direta de fórmulas consolidadas e interpretação física.

**Capítulos recomendados (ordem sugerida):**

1. Capítulo 1 — Introdução às Analogias
2. Capítulo 2 — Fundamentos dos Fluidos
3. Capítulo 4 — Escoamento em Tubulações
4. Capítulo 5 — Hidrodinâmica de Canais
5. Capítulo 7 — Fundamentos de Transferência de Calor
6. Capítulo 9 — Trocadores de Calor
7. Capítulo 10 — Aletas e Superfícies Estendidas

### 3.2 Trilha de Pós-Graduação

**Foco:** Derivação teórica, análise numérica e problemas inversos.

**Capítulos recomendados:**

1. Capítulo 3 — Modelagem Matemática
2. Capítulo 6 — Percolação em Meio Poroso
3. Capítulo 8 — Calor em Solos
4. Capítulo 11 — Transporte de Calor e Massa

**Projetos sugeridos:**

- Implementação de esquemas numéricos (Diferenças Finitas, Volumes Finitos).
- Calibração de parâmetros por problemas inversos (Levenberg-Marquardt).
- Análise de sensibilidade e incerteza.

### 3.3 Conteúdo Programático de Apoio

Para cada capítulo, o guia docs/GUIA_COMPLETO_NOTEBOOKS.md apresenta uma seção
com o conteúdo programático, conceitos-chave e referências. Utilize essa seção
para planejar suas aulas e selecionar os casos mais adequados ao seu curso.

Exemplo: para o Capítulo 5 (Hidrodinâmica de Canais Abertos), os conceitos-chave
incluem:

- Equações de Saint-Venant.
- Modelo de onda cinemática.
- Celeridade da onda cinemática.
- Condição CFL.
- Esquemas explícito e implícito.
- Número de Froude.
- Regime fluvial vs. torrencial.

---

## 4. Recursos Técnicos

### 4.1 Instalação do Ambiente

Forneça aos alunos as seguintes instruções:

    # Clone o repositório
    git clone https://github.com/JaderLugon/fenomenos-transporte-livro.git
    cd fenomenos-transporte-livro

    # Crie ambiente virtual
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # ou: venv\Scripts\activate  # Windows

    # Instale dependências
    pip install -r requirements.txt

    # Inicie o Jupyter
    jupyter notebook

### 4.2 Dependências Mínimas

    numpy>=1.21.0
    scipy>=1.7.0
    matplotlib>=3.4.0
    pandas>=1.3.0
    jupyter>=1.0.0

### 4.3 Alternativas Online

Para alunos sem ambiente local, recomende:

- **Google Colab:** Acesse os notebooks diretamente pelo link no QR Code.
- **JupyterHub:** Se sua instituição possuir servidor.
- **Binder:** Para execução em nuvem (requer configuração).

### 4.4 Módulos Python Reutilizáveis

Os módulos em src/ fornecem funções consolidadas:

    from src import hidrodinamica, transferencia_calor

    # Exemplo: calcular profundidade normal
    hn = hidrodinamica.profundidade_normal(Q=6.7, n=0.035, b=42.2, m=0, S0=1e-4)

    # Exemplo: calcular LMTD
    lmtd = transferencia_calor.lmtd(Th_in=90, Th_out=60, Tc_in=20, Tc_out=50)

---

## 5. Avaliação de Alunos

### 5.1 Rubrica de Avaliação

| Critério | Peso | Descrição |
|:---|:---:|:---|
| Correção técnica | 30% | Resultados numéricos corretos e dimensionalmente consistentes |
| Interpretação física | 25% | Discussão coerente dos resultados |
| Qualidade do código | 20% | Código limpo, comentado e seguindo PEP 8 |
| Visualizações | 15% | Gráficos claros, com legendas e rótulos |
| Referências | 10% | Citações adequadas ao livro e literatura |

### 5.2 Tipos de Avaliação

- **Relatório técnico:** Aluno entrega relatório em PDF com análise do caso.
- **Apresentação oral:** Seminário de 10-15 minutos sobre o estudo de caso.
- **Código comentado:** Notebook com células adicionais de análise.
- **Variação do caso:** Aluno modifica parâmetros e compara resultados.

### 5.3 Avaliação por Nível

| Nível | Ênfase na Avaliação |
|:---|:---|
| Graduação | Aplicação correta de fórmulas, interpretação física básica, código funcional |
| Pós-Graduação | Derivação teórica, análise de sensibilidade, discussão crítica, extensões |

---

## 6. Criando Seus Próprios Estudos de Caso

### 6.1 Quando Criar um Novo Caso

- Você desenvolveu uma aplicação real em sua pesquisa.
- Identificou um problema relevante para sua região ou indústria.
- Deseja compartilhar uma abordagem didática inovadora.

### 6.2 Como Criar

1. **Leia o guia completo:** docs/GUIA_COMPLETO_NOTEBOOKS.md.
2. **Consulte a numeração:** verifique o próximo X disponível em casos/READMEcasos.md.
3. **Crie o notebook** seguindo a nomenclatura EC_Capitulo_X_Sequencial_TemaPrincipal.ipynb.
4. **Preencha as seções:** siga o template do guia (12 seções obrigatórias).
5. **Teste o notebook:** execute do início ao fim em ambiente limpo.
6. **Submeta um Pull Request:** veja docs/Contribuindo.md.

### 6.3 Boas Práticas

- **Seja específico:** dados reais aumentam o engajamento dos alunos.
- **Documente bem:** suponha que outro professor usará seu caso.
- **Teste em múltiplos ambientes:** Windows, Linux, Mac.
- **Inclua dados sintéticos:** caso dados reais não possam ser compartilhados.
- **Siga a jornada pedagógica:** Contextualizar, Formular, Verificar,
  Implementar, Visualizar, Analisar, Discutir.

### 6.4 Checklist do Caso Novo

Antes de submeter, confirme que seu caso possui:

- [ ] Cabeçalho com metadados completos (capítulo, nível, tempo, autor).
- [ ] 5 a 7 objetivos de aprendizagem com verbos de ação.
- [ ] Todas as 12 seções na ordem correta (0 a 11).
- [ ] Verificação prévia incluída e aprovada.
- [ ] Equações em LaTeX com definição de variáveis e unidades.
- [ ] Código vetorizado e comentado em português.
- [ ] Gráficos com títulos, eixos, legendas e observações pedagógicas.
- [ ] Análise de sensibilidade incluída.
- [ ] Discussão com interpretação, limitações (mínimo 3) e aplicações (mínimo 2).
- [ ] Bloco de navegação no final.
- [ ] Execução sem erros do início ao fim.
- [ ] Adição do link em casos/READMEcasos.md.

---

## 7. Comunidade e Colaboração

### 7.1 Como Participar

- **Reporte bugs:** Abra uma Issue no GitHub.
- **Sugira melhorias:** Discuta ideias nas Issues.
- **Contribua com código:** Siga o guia em docs/Contribuindo.md.
- **Compartilhe experiências:** Entre em contato com o autor.

### 7.2 Contato

Prof. Jader Lugon Junior
Instituto Federal Fluminense — Campus Macaé

- Email: jlugonjr@gmail.com
- Web: www.ambhidro.iff.edu.br
- Telefone: 22 98124-7054

### 7.3 Citação Acadêmica

Se você utilizar este material em pesquisa ou ensino, cite como:

    @book{lugon2026fenomenos,
      title={Fenômenos de Transporte: Fundamentos e Modelagem Computacional},
      author={Lugon Junior, Jader},
      year={2026},
      publisher={Repositório GitHub},
      url={https://github.com/JaderLugon/fenomenos-transporte-livro}
    }

---

## 8. Referências Pedagógicas

Para aprofundamento em metodologias ativas:

- MAZUR, E. Peer Instruction: A User's Manual. Prentice Hall, 1997.
- BERGMANN, J.; SAMS, A. Flip Your Classroom. ISTE, 2012.
- FREEMAN, S. et al. Active learning increases student performance in science,
  engineering, and mathematics. PNAS, 111(23), 8410-8415, 2014.

---

**Bom trabalho e boa aula!**

Juntos, formamos uma comunidade acadêmica mais forte.

---

Coleção "Fenômenos de Transporte: Fundamentos e Modelagem Computacional"
Guia do Professor — Versão 2.0 — Agosto de 2026