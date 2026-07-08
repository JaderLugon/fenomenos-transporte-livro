# 📘 Fenômenos de Transporte: Fundamentos e Modelagem Computacional

> **Material complementar ao livro comercial**  
> **Autor:** Jader Lugon Junior  
> **Instituição:** Instituto Federal Fluminense – Campus Macaé  
> **Repositório:** [github.com/JaderLugon/fenomenos-transporte-livro](https://github.com/JaderLugon/fenomenos-transporte-livro)

---

## 🎯 Sobre este Repositório

Este repositório contém **códigos Python, Jupyter Notebooks e estudos de caso** que complementam o livro **"Fenômenos de Transporte: Fundamentos e Modelagem Computacional"**. O livro está disponível comercialmente via Kindle e editoras parceiras.

### ✨ O que você encontra aqui:

- 📓 **11 Notebooks principais** (um por capítulo) — acessíveis via QR Codes no livro
- 🔬 **23+ Estudos de caso** aplicados a problemas reais de engenharia
- 🛠️ **Módulos Python reutilizáveis** (`src/`) com funções consolidadas
- 📖 **Documentação completa** para professores e estudantes
- 🤝 **Convite à contribuição** — professores podem adicionar seus próprios casos

### 🎓 Para quem é este material:

- **Estudantes de graduação e pós-graduação** em Engenharia, Física, Química e Ciências Ambientais
- **Professores** que desejam adotar o livro e utilizar os códigos em sala de aula
- **Pesquisadores** que precisam de ferramentas computacionais para modelagem de fenômenos de transporte
- **Profissionais** da indústria que buscam soluções práticas para problemas térmicos e hidráulicos

---

## 🗂️ Estrutura do Repositório

```
fenomenos-transporte-livro/
│
├── README.md                          # Este arquivo
├── LICENSE                            # Licença MIT
├── requirements.txt                   # Dependências Python
│
├── notebooks/                         # Notebooks principais (QR Codes do livro)
│   ├── 01_introducao_analogias.ipynb
│   ├── 02_fundamentos_fluidos.ipynb
│   ├── 03_modelagem_matematica.ipynb
│   ├── 04_escoamento_tubulacoes.ipynb
│   ├── 05_hidrodinamica_canais.ipynb
│   ├── 06_percolacao_meio_poroso.ipynb
│   ├── 07_fundamentos_calor.ipynb
│   ├── 08_calor_solos.ipynb
│   ├── 09_trocadores_calor.ipynb
│   ├── 10_aletas_superficies.ipynb
│   └── 11_adveccao_dispersao.ipynb
│
├── casos/                             # Estudos de caso aplicados
│   ├── README.md                      # Índice de casos
│   ├── 02_1_Classificador_Fluidos_Nao_Newtonianos.ipynb
│   ├── 04_1_Bombeamento_Predio_Residencial.ipynb
│   ├── 04_2_Sistema_Hidraulico_Carga_Pesada.ipynb
│   ├── 05_1_Rio_Macae_Hidrodinamica.ipynb
│   ├── 05_2_Profundidade_Normal_Canal_Trapezoidal.ipynb
│   ├── 06_1_Percolacao_Terreno_Textura_Conhecida.ipynb
│   ├── 06_2_Curva_Retencao_van_Genuchten.ipynb
│   ├── 07_1_Forno_Padaria_Isolamento_Termico.ipynb
│   ├── 07_2_Circuito_Termico_Parede_Composta.ipynb
│   ├── 08_1_Perfil_Termico_Diurno_Solo.ipynb
│   ├── 08_2_Estabilidade_Numerica_Diferencas_Finitas.ipynb
│   ├── 09_1_Resfriamento_Oleo_Hidraulico_Hidreletrica.ipynb
│   ├── 09_2_Condensador_Vapor_UTE_100MW.ipynb
│   ├── 09_3_Caldeira_Industrial_Vapor.ipynb
│   ├── 10_1_Condensador_ACC_Tubos_Aletados.ipynb
│   ├── 10_2_Dissipador_Termico_Processador.ipynb
│   ├── 10_3_Aleta_Diferencas_Finitas_1D.ipynb
│   ├── 11_1_Rio_Macae_Dispersao_Poluentes.ipynb
│   └── 11_2_Difusao_Artificial_Upwind.ipynb
│
├── src/                               # Módulos Python reutilizáveis
│   ├── __init__.py
│   ├── hidrodinamica.py
│   ├── transferencia_calor.py
│   ├── meio_poroso.py
│   ├── dispersao.py
│   ├── problemas_inversos.py
│   └── utils.py
│
└── docs/                              # Documentação adicional
    ├── guia_professor.md
    ├── template_estudo_caso.md
    └── contribuindo.md
```

---

## 🚀 Instalação e Uso

### Pré-requisitos

- **Python 3.9+**
- **pip** ou **conda**
- **Git** (opcional, para clonar o repositório)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/JaderLugon/fenomenos-transporte-livro.git
cd fenomenos-transporte-livro

# Crie ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### Executando os Notebooks

```bash
# Inicie o Jupyter Notebook
jupyter notebook

# Navegue até a pasta desejada (notebooks/ ou casos/)
# Abra qualquer arquivo .ipynb no navegador
```

### Usando os Módulos Python

```python
# Em qualquer notebook ou script Python
from src import hidrodinamica, transferencia_calor

# Exemplo: calcular profundidade normal
hn = hidrodinamica.profundidade_normal(Q=6.7, n=0.035, b=42.2, m=0, S0=1e-4)
print(f"Profundidade normal: {hn:.3f} m")

# Exemplo: calcular LMTD
lmtd = transferencia_calor.lmtd(Th_in=90, Th_out=60, Tc_in=20, Tc_out=50)
print(f"LMTD: {lmtd:.1f} °C")
```

---

## 📚 Capítulos do Livro

| Capítulo | Título | Notebook Principal | Estudos de Caso |
|----------|--------|-------------------|-----------------|
| 1 | Introdução às Analogias | [`01_introducao_analogias.ipynb`](notebooks/01_introducao_analogias.ipynb) | — |
| 2 | Fundamentos dos Fluidos | [`02_fundamentos_fluidos.ipynb`](notebooks/02_fundamentos_fluidos.ipynb) | [1 caso](casos/) |
| 3 | Modelagem Matemática | [`03_modelagem_matematica.ipynb`](notebooks/03_modelagem_matematica.ipynb) | [2 casos](casos/) |
| 4 | Escoamento em Tubulações | [`04_escoamento_tubulacoes.ipynb`](notebooks/04_escoamento_tubulacoes.ipynb) | [2 casos](casos/) |
| 5 | Hidrodinâmica de Canais | [`05_hidrodinamica_canais.ipynb`](notebooks/05_hidrodinamica_canais.ipynb) | [2 casos](casos/) |
| 6 | Percolação em Meio Poroso | [`06_percolacao_meio_poroso.ipynb`](notebooks/06_percolacao_meio_poroso.ipynb) | [2 casos](casos/) |
| 7 | Fundamentos de Calor | [`07_fundamentos_calor.ipynb`](notebooks/07_fundamentos_calor.ipynb) | [2 casos](casos/) |
| 8 | Calor em Solos | [`08_calor_solos.ipynb`](notebooks/08_calor_solos.ipynb) | [2 casos](casos/) |
| 9 | Trocadores de Calor | [`09_trocadores_calor.ipynb`](notebooks/09_trocadores_calor.ipynb) | [3 casos](casos/) |
| 10 | Aletas e Superfícies | [`10_aletas_superficies.ipynb`](notebooks/10_aletas_superficies.ipynb) | [3 casos](casos/) |
| 11 | Advecção e Dispersão | [`11_adveccao_dispersao.ipynb`](notebooks/11_adveccao_dispersao.ipynb) | [2 casos](casos/) |

---

## 🤝 Como Contribuir

Este é um projeto **colaborativo e aberto**. Professores, pesquisadores e estudantes são convidados a contribuir com novos estudos de caso, correções e melhorias.

### 📝 Contribuindo com um novo estudo de caso

1. **Fork** este repositório
2. **Copie o template** em [`docs/template_estudo_caso.md`](docs/template_estudo_caso.md)
3. **Crie seu notebook** em `casos/NN_X_Nome_Do_Caso.ipynb`
4. **Adicione o link** em [`casos/README.md`](casos/README.md)
5. **Abra um Pull Request** descrevendo o caso

### 📋 Critérios para aceitação

- ✅ Código reprodutível (qualquer pessoa deve conseguir executar)
- ✅ Documentação completa seguindo o template
- ✅ Dados de entrada públicos ou sintéticos
- ✅ Referências adequadas (ao livro e fontes externas)
- ✅ Nível didático claro (graduação ou pós-graduação)

### 🐛 Reportando problemas

Encontrou um bug ou erro nos códigos? Abra uma **Issue** no GitHub descrevendo:

- O problema encontrado
- Passos para reproduzir
- Comportamento esperado vs. observado
- Screenshots (se aplicável)

---

## 📄 Licença

Este projeto está sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE) para detalhes.

O **livro comercial** possui direitos autorais reservados e está disponível para compra via Kindle e editoras parceiras.

---

## 📧 Contato

**Jader Lugon Junior**  
Instituto Federal Fluminense – Campus Macaé  
📧 jlugonjr@gmail.com  
🌐 [www.ambhidro.iff.edu.br](http://www.ambhidro.iff.edu.br)

---

<div align="center">

**🎓 Bom estudo e boa modelagem!**

*Fenômenos de Transporte: Fundamentos e Modelagem Computacional*  
© 2026 Jader Lugon Junior

</div>