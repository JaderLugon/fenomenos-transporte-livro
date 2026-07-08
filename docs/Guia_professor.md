\# 👨‍🏫 Guia do Professor

> \*\*Bem-vindo(a)!\*\* Este guia apresenta sugestões de como utilizar os materiais deste repositório em suas disciplinas, aproveitando ao máximo a integração com o livro \*Fenômenos de Transporte: Fundamentos e Modelagem Computacional\*.

\---

\## 📖 1. Visão Geral do Material

\### 1.1 Estrutura do Repositório

| Pasta | Conteúdo | Uso Principal |

|-------|----------|---------------|

| `notebooks/` | 11 notebooks principais (um por capítulo) | Material de referência, QR Codes do livro |

| `casos/` | Estudos de caso aplicados | Exercícios práticos, projetos, demonstrações |

| `src/` | Módulos Python reutilizáveis | Código limpo para importação nos notebooks |

| `docs/` | Documentação (este guia, template, contribuição) | Referência para uso e contribuição |


\### 1.2 Integração com o Livro


Cada capítulo do livro possui um \*\*QR Code\*\* que direciona o aluno para o notebook correspondente no repositório. Essa integração permite:


\- \*\*Acesso imediato\*\* a códigos executáveis durante a leitura

\- \*\*Reprodutibilidade\*\* dos exemplos apresentados no livro

\- \*\*Extensão prática\*\* dos conceitos teóricos


\---


\## 🎓 2. Estratégias Pedagógicas


\### 2.1 Demonstração em Sala de Aula


\*\*Objetivo:\*\* Ilustrar conceitos teóricos com exemplos computacionais.


\*\*Como fazer:\*\*

1\. Projete o notebook em tela compartilhada

2\. Execute as células passo a passo, explicando cada etapa

3\. Modifique parâmetros em tempo real para explorar diferentes cenários

4\. Peça aos alunos para prever resultados antes da execução


\*\*Exemplo:\*\* No Capítulo 4 (Escoamento em Tubulações), demonstre como a perda de carga varia com o diâmetro usando o caso `04\_1\_Bombeamento\_Predio\_Residencial.ipynb`.


\### 2.2 Exercício Guiado


\*\*Objetivo:\*\* Consolidar conceitos através da prática.


\*\*Como fazer:\*\*

1\. Forneça o notebook com algumas células em branco

2\. Oriente os alunos a preencherem as lacunas

3\. Discuta as soluções em plenária

4\. Compare diferentes abordagens



\*\*Dica:\*\* Use o template `template\_estudo\_caso.md` para criar exercícios estruturados.



\### 2.3 Projeto Semestral


\*\*Objetivo:\*\* Desenvolver competências de modelagem computacional.


\*\*Sugestões de projetos:\*\*


| Nível | Tema | Complexidade |

|-------|------|--------------|

| Graduação | Dimensionamento de sistema de abastecimento predial | Média |

| Graduação | Análise térmica de dissipador de CPU | Média |

| Pós-Graduação | Calibração de modelo de dispersão em rio | Alta |

| Pós-Graduação | Estimação de parâmetros por problema inverso | Alta |


\### 2.4 Aula Invertida (Flipped Classroom)


\*\*Objetivo:\*\* Maximizar o tempo de interação em sala.


\*\*Como fazer:\*\*

1\. \*\*Antes da aula:\*\* Alunos estudam o capítulo do livro e executam o notebook

2\. \*\*Em sala:\*\* Discutam dúvidas e resolvam problemas avançados

3\. \*\*Pós-aula:\*\* Alunos criam variações do estudo de caso


\---


\## 📚 3. Trilhas de Aprendizagem


\### 3.1 Trilha de Graduação


\*\*Foco:\*\* Aplicação direta de fórmulas consolidadas e interpretação física.


\*\*Capítulos recomendados (ordem sugerida):\*\*

1\. Capítulo 1 — Introdução às Analogias

2\. Capítulo 2 — Fundamentos dos Fluidos

3\. Capítulo 4 — Escoamento em Tubulações

4\. Capítulo 5 — Hidrodinâmica de Canais

5\. Capítulo 7 — Fundamentos de Transferência de Calor

6\. Capítulo 9 — Trocadores de Calor

7\. Capítulo 10 — Aletas e Superfícies Estendidas


\### 3.2 Trilha de Pós-Graduação


\*\*Foco:\*\* Derivação teórica, análise numérica e problemas inversos.


\*\*Capítulos recomendados:\*\*

1\. Capítulo 3 — Modelagem Matemática

2\. Capítulo 6 — Percolação em Meio Poroso

3\. Capítulo 8 — Calor em Solos

4\. Capítulo 11 — Transporte de Calor e Massa


\*\*Projetos sugeridos:\*\*

\- Implementação de esquemas numéricos (Diferenças Finitas, Volumes Finitos)

\- Calibração de parâmetros por problemas inversos (Levenberg-Marquardt)

\- Análise de sensibilidade e incerteza


\---


\## 🛠️ 4. Recursos Técnicos


\### 4.1 Instalação do Ambiente


Forneça aos alunos as seguintes instruções:


```bash

\# Clone o repositório

git clone https://github.com/JaderLugon/fenomenos-transporte-livro.git

cd fenomenos-transporte-livro


\# Crie ambiente virtual

python -m venv venv

source venv/bin/activate  # Linux/Mac

\# ou: venv\\Scripts\\activate  # Windows


\# Instale dependências

pip install -r requirements.txt


\# Inicie o Jupyter

jupyter notebook

4.2 Alternativas Online
Para alunos sem ambiente local, recomende:
Google Colab: Acesse os notebooks diretamente pelo link no QR Code
JupyterHub: Se sua instituição possuir servidor
Binder: Para execução em nuvem (requer configuração)

4.3 Módulos Python Reutilizáveis
Os módulos em src/ fornecem funções consolidadas:

from src import hidrodinamica, transferencia_calor

# Exemplo: calcular profundidade normal
hn = hidrodinamica.profundidade_normal(Q=6.7, n=0.035, b=42.2, m=0, S0=1e-4)

# Exemplo: calcular LMTD
lmtd = transferencia_calor.lmtd(Th_in=90, Th_out=60, Tc_in=20, Tc_out=50)


📝 5. Avaliação de Alunos
5.1 Rubrica de Avaliação

Critério                Peso     Descrição
Correção técnica        30%      Resultados numéricos corretos e dimensionalmente consistentes
Interpretação física    25%      Discussão coerente dos resultados
Qualidade do código     20%      Código limpo, comentado e seguindo PEP 8
Visualizações           15%      Gráficos claros, com legendas e rótulos
Referências             10%      Citações adequadas ao livro e literatura

5.2 Tipos de Avaliação
Relatório técnico: Aluno entrega relatório em PDF com análise do caso
Apresentação oral: Seminário de 10-15 minutos sobre o estudo de caso
Código comentado: Notebook com células adicionais de análise
Variação do caso: Aluno modifica parâmetros e compara resultados

✍️ 6. Criando Seus Próprios Estudos de Caso
6.1 Quando Criar um Novo Caso
Você desenvolveu uma aplicação real em sua pesquisa
Identificou um problema relevante para sua região/indústria
Deseja compartilhar uma abordagem didática inovadora

6.2 Como Criar
Copie o template: docs/template_estudo_caso.md
Preencha as seções: Siga as orientações do template
Teste o notebook: Execute do início ao fim em ambiente limpo
Submeta um Pull Request: Veja docs/contribuindo.md

6.3 Boas Práticas
Seja específico: Dados reais aumentam o engajamento dos alunos
Documente bem: Suponha que outro professor usará seu caso
Teste em múltiplos ambientes: Windows, Linux, Mac
Inclua dados sintéticos: Caso dados reais não possam ser compartilhados

🤝 7. Comunidade e Colaboração
7.1 Como Participar
Reporte bugs: Abra uma Issue no GitHub
Sugira melhorias: Discuta ideias nas Issues
Contribua com código: Siga o guia em docs/contribuindo.md
Compartilhe experiências: Entre em contato com o autor

7.2 Contato
Prof. Jader Lugon Junior
Instituto Federal Fluminense — Campus Macaé
📧 jlugonjr@gmail.com
🌐 www.ambhidro.iff.edu.br

📚 8. Referências Pedagógicas
Para aprofundamento em metodologias ativas:
MAZUR, E. Peer Instruction: A User's Manual. Prentice Hall, 1997.
BERGMANN, J.; SAMS, A. Flip Your Classroom. ISTE, 2012.
FREEMAN, S. et al. Active learning increases student performance. PNAS, 111(23), 8410-8415, 2014.

🎓 Bom trabalho e boa aula!
Juntos, formamos uma comunidade acadêmica mais forte.