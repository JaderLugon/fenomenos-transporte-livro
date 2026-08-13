# Guia de Contribuição

> **Obrigado por considerar contribuir com este repositório!**
> Sua contribuição ajudará estudantes e professores em todo o Brasil a aprender
> Fenômenos de Transporte com materiais de qualidade.

---

## Sumário

1. Como Posso Contribuir?
2. Fluxo de Trabalho para Contribuições
3. Submetendo um Pull Request
4. Criando Novos Estudos de Caso
5. Padrões de Estilo
6. Testando Suas Alterações
7. Licença
8. Código de Conduta
9. Reconhecimento
10. Dúvidas?

---

## 1. Como Posso Contribuir?

Existem várias formas de contribuir, mesmo sem ser expert em programação.

### 1.1 Reportando Problemas

Encontrou um erro no código, no notebook ou na documentação?

1. Verifique se o problema já foi reportado nas Issues:
   github.com/JaderLugon/fenomenos-transporte-livro/issues
2. Se não, abra uma nova Issue com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs. observado
   - Screenshots (se aplicável)
   - Ambiente (SO, versão do Python, bibliotecas)

### 1.2 Sugerindo Melhorias

Tem uma ideia para melhorar um estudo de caso existente?

1. Abra uma Issue com o label `enhancement`.
2. Descreva sua ideia e os benefícios esperados.
3. Discuta com a comunidade antes de implementar.

### 1.3 Criando Novos Estudos de Caso

Desenvolveu um caso interessante em sua pesquisa ou disciplina?

1. Leia o guia completo em `docs/GUIA_COMPLETO_NOTEBOOKS.md`.
2. Consulte a numeração disponível em `casos/READMEcasos.md`.
3. Submeta um Pull Request (veja Seção 3).

### 1.4 Corrigindo Bugs no Código

Encontrou um bug e sabe como corrigir?

1. Faça um fork do repositório.
2. Crie uma branch para sua correção.
3. Submeta um Pull Request com a correção.

### 1.5 Melhorando a Documentação

Erros de digitação, explicações confusas, exemplos faltando?

1. Documentação é tão importante quanto código!
2. Submeta correções via Pull Request.

---

## 2. Fluxo de Trabalho para Contribuições

### 2.1 Para Contribuições Simples (Documentação, Typos)

1. Edite diretamente no GitHub (botão "Edit" no arquivo).
2. Faça o commit com mensagem descritiva.
3. Abra um Pull Request.

### 2.2 Para Contribuições Substanciais (Novos Casos, Features)

    # 1. Fork o repositório no GitHub

    # 2. Clone seu fork localmente
    git clone https://github.com/SEU_USUARIO/fenomenos-transporte-livro.git
    cd fenomenos-transporte-livro

    # 3. Configure o upstream
    git remote add upstream https://github.com/JaderLugon/fenomenos-transporte-livro.git

    # 4. Crie uma branch para sua contribuição
    git checkout -b feature/nome-da-sua-contribuicao

    # 5. Faça suas alterações e commits
    git add .
    git commit -m "Descrição clara da alteração"

    # 6. Mantenha sua branch atualizada
    git fetch upstream
    git rebase upstream/main

    # 7. Envie para seu fork
    git push origin feature/nome-da-sua-contribuicao

    # 8. Abra um Pull Request no GitHub

---

## 3. Submetendo um Pull Request

### 3.1 Checklist Antes de Submeter

Antes de abrir um Pull Request, verifique:

- [ ] O código executa sem erros.
- [ ] As alterações seguem o estilo do projeto.
- [ ] A documentação foi atualizada (se necessário).
- [ ] Os commits possuem mensagens claras e descritivas.
- [ ] Não há arquivos desnecessários (.DS_Store, __pycache__, etc.).
- [ ] O Pull Request referencia a Issue relacionada (se houver).

### 3.2 Estrutura do Pull Request

Use o seguinte template ao abrir um PR:

    ## Descrição
    [Descreva brevemente o que este PR faz]

    ## Tipo de Mudança
    - [ ] Correção de bug
    - [ ] Nova funcionalidade
    - [ ] Novo estudo de caso
    - [ ] Melhoria de documentação
    - [ ] Outro (especifique)

    ## Issue Relacionada
    Closes #[número da issue]

    ## Checklist
    - [ ] Meu código segue o estilo do projeto
    - [ ] Fiz uma auto-revisão do meu código
    - [ ] Comentei partes complexas do código
    - [ ] Atualizei a documentação correspondente
    - [ ] Minhas alterações não geram novos warnings
    - [ ] Testei minhas alterações localmente
    - [ ] O notebook executa do início ao fim sem erros (se aplicável)

    ## Screenshots (se aplicável)
    [Adicione screenshots das alterações visuais]

    ## Informações Adicionais
    [Qualquer informação relevante para os revisores]

### 3.3 Processo de Revisão

1. **Submissão:** Você abre o Pull Request.
2. **Revisão automática:** GitHub Actions executa testes (se configurados).
3. **Revisão humana:** Mantenedores revisam o código.
4. **Discussão:** Possíveis ajustes são solicitados.
5. **Aprovação:** PR é aprovado e mergeado.
6. **Agradecimento:** Seu nome é adicionado à lista de contribuidores.

---

## 4. Criando Novos Estudos de Caso

Esta é a forma mais valiosa de contribuir com o repositório. Siga rigorosamente
o guia completo em `docs/GUIA_COMPLETO_NOTEBOOKS.md`.

### 4.1 Convenção de Numeração

Antes de criar um caso novo, verifique a numeração correta.

#### Casos publicados no livro

Recebem o número do capítulo e da seção onde estão localizados:

    EC_Capitulo_Secao_TemaPrincipal.ipynb

Exemplo: EC_05_06_Rio_Macae_Hidrodinamica.ipynb

#### Casos novos (contribuições da comunidade)

Recebem o número do capítulo, a letra X e um número sequencial crescente:

    EC_Capitulo_X_Sequencial_TemaPrincipal.ipynb

Exemplo: EC_05_X2_Onda_Cheia_Saint_Venant.ipynb

### 4.2 Regras Importantes

- Consulte `casos/READMEcasos.md` para verificar o próximo X disponível no capítulo.
- Nunca reutilize um número sequencial, mesmo que um caso tenha sido removido.
- O número do capítulo deve sempre ter 2 dígitos (04, 07, 11).
- Ao ser incorporado ao livro, um caso X é renumerado para o formato de seção.

### 4.3 Checklist do Caso Novo

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
- [ ] Adição do link em `casos/READMEcasos.md`.

### 4.4 Capítulos Disponíveis para Contribuição

Os capítulos do livro abrangem os seguintes temas. Ao criar um caso novo,
associe-o ao capítulo mais adequado:

| Capítulo | Tema |
|:---:|:---|
| 1 | Introdução às Analogias / Fundamentos e Motivação |
| 2 | Fundamentos dos Fluidos e Viscosidade |
| 3 | Modelagem Matemática do Escoamento |
| 4 | Escoamento em Tubulações e Bombeamento |
| 5 | Hidrodinâmica de Canais Abertos |
| 6 | Percolação em Meio Poroso |
| 7 | Fundamentos de Transferência de Calor |
| 8 | Transferência de Calor em Solos |
| 9 | Trocadores de Calor |
| 10 | Aletas e Superfícies Estendidas |
| 11 | Transporte de Calor e Massa em Corpos Hídricos |

---

## 5. Padrões de Estilo

As diretrizes completas de formatação e rigor técnico estão em
`docs/GUIA_COMPLETO_NOTEBOOKS.md`. Abaixo, um resumo rápido.

### 5.1 Python (PEP 8)

Siga o PEP 8 para código Python.

Exemplo correto:

    def calcular_perda_carga(f, L, D, V, g=9.81):
        """Calcula a perda de carga distribuída pela equação de Darcy-Weisbach."""
        return f * (L / D) * (V**2 / (2 * g))

Exemplo incorreto:

    def calc(f,L,D,V,g=9.81):
        return f*(L/D)*(V**2/(2*g))

### 5.2 Docstrings

Use docstrings no estilo NumPy:

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

### 5.3 Notebooks Jupyter

- Nomeie células com títulos em markdown.
- Comente o código explicando a física, não apenas a sintaxe.
- Use LaTeX para equações matemáticas.
- Inclua visualizações com legendas claras.
- Mantenha a ordem de execução linear (Execute All e depois Salve).
- Inclua observações pedagógicas após cada gráfico.

### 5.4 Nomenclatura de Arquivos

Siga o padrão estabelecido na Seção 4.1:

    notebooks/
        NN_nome_capitulo.ipynb
        Exemplo: 04_escoamento_tubulacoes.ipynb

    casos/
        EC_Capitulo_Secao_TemaPrincipal.ipynb      (caso publicado)
        EC_Capitulo_X_Sequencial_TemaPrincipal.ipynb (caso novo)

Onde:
- Capitulo = número do capítulo (2 dígitos)
- Secao = número da seção do livro
- X = marcador literal de caso complementar
- Sequencial = número crescente dentro do capítulo
- TemaPrincipal = descrição clara e concisa

---

## 6. Testando Suas Alterações

### 6.1 Teste Local

Antes de submeter, teste suas alterações.

Dependências mínimas:

    numpy>=1.21.0
    scipy>=1.7.0
    matplotlib>=3.4.0
    pandas>=1.3.0
    jupyter>=1.0.0

### 6.2 Teste de Reprodutibilidade

Para estudos de caso:

1. Clone o repositório em um ambiente limpo.
2. Execute o notebook do início ao fim (Execute All).
3. Verifique se os resultados são idênticos aos esperados.
4. Teste em pelo menos dois sistemas operacionais diferentes (se possível).
5. Confirme que o tempo de execução total é inferior a 5 minutos.

### 6.3 Teste de Legibilidade

- Todos os gráficos possuem títulos, rótulos nos eixos e legendas?
- As tabelas estão formatadas corretamente?
- As equações estão em LaTeX e legíveis?
- Os comentários explicam a física, não apenas o código?

---

## 7. Licença

### 7.1 Licença do Código

O código deste repositório está sob a licença MIT:

    MIT License

    Copyright (c) 2026 Jader Lugon Junior

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

### 7.2 Licença dos Estudos de Caso

Os estudos de caso estão sob a licença Creative Commons
Attribution-ShareAlike 4.0 (CC-BY-SA-4.0):

- Você pode compartilhar e adaptar o material.
- Para qualquer fim, inclusive comercial.
- Desde que dê crédito ao autor e compartilhe pela mesma licença.

### 7.3 Licença do Livro

O livro comercial possui direitos autorais reservados e está disponível para
compra via Kindle e editoras parceiras. Este repositório contém apenas
materiais complementares abertos.

### 7.4 Licenciamento da Sua Contribuição

Ao submeter um Pull Request, você concorda que sua contribuição será
licenciada sob os mesmos termos do projeto (MIT para código, CC-BY-SA-4.0
para conteúdo educacional).

---

## 8. Código de Conduta

### 8.1 Nosso Compromisso

Este projeto adota um ambiente acolhedor, respeitoso e livre de assédio para
todos os contribuidores, independentemente de:

- Idade, corpo, deficiência, etnia, identidade de gênero
- Nível de experiência, educação, status socioeconômico
- Nacionalidade, aparência, raça, religião
- Identidade e orientação sexual

### 8.2 Comportamento Esperado

- Use linguagem acolhedora e inclusiva.
- Respeite pontos de vista e experiências diferentes.
- Aceite críticas construtivas com elegância.
- Foque no que é melhor para a comunidade.
- Demonstre empatia com outros membros.

### 8.3 Comportamento Inaceitável

- Uso de linguagem ou imagens sexualizadas.
- Trolling, insultos e ataques pessoais.
- Assédio público ou privado.
- Publicação de informações privadas sem autorização.
- Outra conduta considerada inadequada.

### 8.4 Como Reportar

Casos de comportamento abusivo podem ser reportados para:

Email: jlugonjr@gmail.com

Todas as queixas serão revisadas e investigadas, com resposta adequada às
circunstâncias.

---

## 9. Reconhecimento

### 9.1 Lista de Contribuidores

Todos os contribuidores são reconhecidos no arquivo `CONTRIBUTORS.md` e no
`README.md` principal.

### 9.2 Citação Acadêmica

Se você utilizar este material em pesquisa ou ensino, cite como:

    @book{lugon2026fenomenos,
      title={Fenômenos de Transporte: Fundamentos e Modelagem Computacional},
      author={Lugon Junior, Jader},
      year={2026},
      publisher={Repositório GitHub},
      url={https://github.com/JaderLugon/fenomenos-transporte-livro}
    }

### 9.3 Citação de um Estudo de Caso Específico

Para citar um estudo de caso individual:

    @misc{lugon2026caso,
      title={Estudo de Caso EC_05_06 — Hidrodinâmica do Rio Macaé},
      author={Lugon Junior, Jader},
      year={2026},
      howpublished={\url{https://github.com/JaderLugon/fenomenos-transporte-livro}},
      note={Repositório Fenômenos de Transporte}
    }

---

## 10. Dúvidas?

Se tiver dúvidas sobre como contribuir:

1. **Leia a documentação:** Este guia e o `GUIA_COMPLETO_NOTEBOOKS.md`
   devem responder a maioria das perguntas.
2. **Abra uma Issue:** Use o label `question` para dúvidas gerais.
3. **Entre em contato:** jlugonjr@gmail.com

---

## Obrigado por fazer parte desta comunidade!

Cada contribuição, por menor que seja, faz a diferença. Juntos, construímos
um material de qualidade para o ensino de Fenômenos de Transporte no Brasil.

---

Coleção "Fenômenos de Transporte: Fundamentos e Modelagem Computacional"
Guia de Contribuição — Versão 2.0 — Agosto de 2026