\---

## 📄 Arquivo 3: `docs/contribuindo.md`

```markdown
# 🤝 Guia de Contribuição

> \*\*Obrigado por considerar contribuir com este repositório!\*\*  
> Sua contribuição ajudará estudantes e professores em todo o Brasil a aprender Fenômenos de Transporte com materiais de qualidade.

---

## 📋 1. Como Posso Contribuir?

Existem várias formas de contribuir, mesmo sem ser expert em programação:

### 1.1 Reportando Problemas

Encontrou um erro no código, no notebook ou na documentação?

1. Verifique se o problema já foi reportado nas \[Issues](https://github.com/JaderLugon/fenomenos-transporte-livro/issues)
2. Se não, abra uma nova Issue com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs. observado
   - Screenshots (se aplicável)
   - Ambiente (SO, versão do Python, bibliotecas)

### 1.2 Sugerindo Melhorias

Tem uma ideia para melhorar um estudo de caso existente?

1. Abra uma Issue com o label `enhancement`
2. Descreva sua ideia e os benefícios esperados
3. Discuta com a comunidade antes de implementar

### 1.3 Criando Novos Estudos de Caso

Desenvolveu um caso interessante em sua pesquisa ou disciplina?

1. Siga o template em \[`template\_estudo\_caso.md`](template\_estudo\_caso.md)
2. Submeta um Pull Request (veja seção 3)

### 1.4 Corrigindo Bugs no Código

Encontrou um bug e sabe como corrigir?

1. Faça um fork do repositório
2. Crie uma branch para sua correção
3. Submeta um Pull Request com a correção

### 1.5 Melhorando a Documentação

Erros de digitação, explicações confusas, exemplos faltando?

1. Documentação é tão importante quanto código!
2. Submeta correções via Pull Request

---

## 🚀 2. Fluxo de Trabalho para Contribuições

### 2.1 Para Contribuições Simples (Documentação, Typos)

```bash
# 1. Edite diretamente no GitHub (botão "Edit" no arquivo)
# 2. Faça o commit com mensagem descritiva
# 3. Abra um Pull Request



\### 2.2 Para Contribuições Substanciais (Novos Casos, Features)

\# 1. Fork o repositório no GitHub

\# 2. Clone seu fork localmente

git clone https://github.com/SEU\_USUARIO/fenomenos-transporte-livro.git

cd fenomenos-transporte-livro



\# 3. Configure o upstream

git remote add upstream https://github.com/JaderLugon/fenomenos-transporte-livro.git



\# 4. Crie uma branch para sua contribuição

git checkout -b feature/nome-da-sua-contribuicao



\# 5. Faça suas alterações e commits

git add .

git commit -m "Descrição clara da alteração"



\# 6. Mantenha sua branch atualizada

git fetch upstream

git rebase upstream/main



\# 7. Envie para seu fork

git push origin feature/nome-da-sua-contribuicao



\# 8. Abra um Pull Request no GitHub



📝 3. Submetendo um Pull Request

3.1 Checklist Antes de Submeter

Antes de abrir um Pull Request, verifique:

O código executa sem erros

As alterações seguem o estilo do projeto

A documentação foi atualizada (se necessário)

Os commits possuem mensagens claras e descritivas

Não há arquivos desnecessários (.DS\_Store, \_\_pycache\_\_, etc.)

O Pull Request referencia a Issue relacionada (se houver)



3.2 Estrutura do Pull Request

Use o seguinte template ao abrir um PR:

\## Descrição

\[Descreva brevemente o que este PR faz]



\## Tipo de Mudança

\- \[ ] Correção de bug

\- \[ ] Nova funcionalidade

\- \[ ] Novo estudo de caso

\- \[ ] Melhoria de documentação

\- \[ ] Outro (especifique)



\## Issue Relacionada

Closes #\[número da issue]



\## Checklist

\- \[ ] Meu código segue o estilo do projeto

\- \[ ] Fiz uma auto-revisão do meu código

\- \[ ] Comentei partes complexas do código

\- \[ ] Atualizei a documentação correspondente

\- \[ ] Minhas alterações não geram novos warnings

\- \[ ] Testei minhas alterações localmente



\## Screenshots (se aplicável)

\[Adicione screenshots das alterações visuais]



\## Informações Adicionais

\[Qualquer informação relevante para os revisores]



3.3 Processo de Revisão

Submissão: Você abre o Pull Request

Revisão automática: GitHub Actions executa testes (se configurados)

Revisão humana: Mantenedores revisam o código

Discussão: Possíveis ajustes são solicitados

Aprovação: PR é aprovado e mergeado

Agradecimento: Seu nome é adicionado à lista de contribuidores



🎨 4. Padrões de Estilo

4.1 Python (PEP 8)

Siga o PEP 8 para código Python:

\# ✅ Bom

def calcular\_perda\_carga(f, L, D, V, g=9.81):

&#x20;   """Calcula a perda de carga distribuída pela equação de Darcy-Weisbach."""

&#x20;   return f \* (L / D) \* (V\*\*2 / (2 \* g))



\# ❌ Ruim

def calc(f,L,D,V,g=9.81):

&#x20;   return f\*(L/D)\*(V\*\*2/(2\*g))



4.2 Docstrings

Use docstrings no estilo NumPy:

def manning\_vazao(n, A, Rh, S0):

&#x20;   """

&#x20;   Calcula a vazão pela equação de Manning (SI).

&#x20;   

&#x20;   Parâmetros

&#x20;   ----------

&#x20;   n : float

&#x20;       Coeficiente de rugosidade de Manning \[s/m^(1/3)].

&#x20;   A : float

&#x20;       Área molhada \[m²].

&#x20;   Rh : float

&#x20;       Raio hidráulico \[m].

&#x20;   S0 : float

&#x20;       Declividade do fundo \[m/m].

&#x20;   

&#x20;   Retorna

&#x20;   -------

&#x20;   float

&#x20;       Vazão \[m³/s].

&#x20;   

&#x20;   Exemplo

&#x20;   -------

&#x20;   >>> manning\_vazao(0.035, 30.0, 0.71, 1e-4)

&#x20;   6.80

&#x20;   """

&#x20;   return (1.0 / n) \* A \* (Rh \*\* (2.0 / 3.0)) \* (S0 \*\* 0.5)



4.3 Notebooks Jupyter

Nomeie células com títulos em markdown (# Título)

Comente o código explicando a lógica

Use LaTeX para equações matemáticas

Inclua visualizações com legendas claras

Mantenha a ordem de execução linear (Execute All → Salve)



4.4 Nomenclatura de Arquivos

Siga o padrão estabelecido:

notebooks/

└── NN\_nome\_capitulo.ipynb          # Ex: 04\_escoamento\_tubulacoes.ipynb



casos/

└── NN\_X\_Nome\_Do\_Caso.ipynb         # Ex: 04\_1\_Bombeamento\_Predio\_Residencial.ipynb

&#x20;   ├── NN = número do capítulo

&#x20;   ├── X = número sequencial do caso

&#x20;   └── Nome\_Do\_Caso = descrição clara (use CamelCase ou snake\_case)



🧪 5. Testando Suas Alterações

5.1 Teste Local

Antes de submeter, teste suas alterações:

numpy>=1.21.0

scipy>=1.7.0

matplotlib>=3.4.0

pandas>=1.3.0

jupyter>=1.0.0



5.3 Teste de Reprodutibilidade

Para estudos de caso:

Clone o repositório em um ambiente limpo

Execute o notebook do início ao fim

Verifique se os resultados são idênticos aos esperados

Teste em pelo menos dois sistemas operacionais diferentes



📜 6. Licença

6.1 Licença do Código

O código deste repositório está sob a licença MIT:

MIT License

Copyright (c) 2026 Jader Lugon Junior

Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction...



6.2 Licença dos Estudos de Caso

Os estudos de caso estão sob a licença Creative Commons Attribution-ShareAlike 4.0 (CC-BY-SA-4.0):

✅ Você pode: compartilhar e adaptar o material

✅ Para qualquer fim, inclusive comercial

⚠️ Desde que: dê crédito ao autor e compartilhe pela mesma licença



6.3 Licença do Livro

O livro comercial possui direitos autorais reservados e está disponível para compra via Kindle e editoras parceiras. Este repositório contém apenas materiais complementares abertos.



🤝 7. Código de Conduta

7.1 Nosso Compromisso

Este projeto adota um ambiente acolhedor, respeitoso e livre de assédio para todos os contribuidores, independentemente de:

Idade, corpo, deficiência, etnia, identidade de gênero

Nível de experiência, educação, status socioeconômico

Nacionalidade, aparência, raça, religião

Identidade e orientação sexual



7.2 Comportamento Esperado

✅ Use linguagem acolhedora e inclusiva

✅ Respeite pontos de vista e experiências diferentes

✅ Aceite críticas construtivas com elegância

✅ Foque no que é melhor para a comunidade

✅ Demonstre empatia com outros membros



7.3 Comportamento Inaceitável

❌ Uso de linguagem ou imagens sexualizadas

❌ Trolling, insultos e ataques pessoais

❌ Assédio público ou privado

❌ Publicação de informações privadas sem autorização

❌ Outra conduta considerada inadequada



7.4 Como Reportar

Casos de comportamento abusivo podem ser reportados para:

📧 jlugonjr@gmail.com

Todas as queixas serão revisadas e investigadas, com resposta adequada às circunstâncias.



🎓 8. Reconhecimento

8.1 Lista de Contribuidores

Todos os contribuidores são reconhecidos no arquivo CONTRIBUTORS.md e no README principal.



8.2 Citação Acadêmica

Se você utilizar este material em pesquisa ou ensino, cite como:

@book{lugon2026fenomenos,

&#x20; title={Fenômenos de Transporte: Fundamentos e Modelagem Computacional},

&#x20; author={Lugon Junior, Jader},

&#x20; year={2026},

&#x20; publisher={Repositório GitHub},

&#x20; url={https://github.com/JaderLugon/fenomenos-transporte-livro}

}



❓ 9. Dúvidas?

Se tiver dúvidas sobre como contribuir:

Leia a documentação: Este guia e o template devem responder a maioria das perguntas

Abra uma Issue: Use o label question para dúvidas gerais

Entre em contato: jlugonjr@gmail.com



🎓 Obrigado por fazer parte desta comunidade!

Cada contribuição, por menor que seja, faz a diferença.























