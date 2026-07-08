#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exemplo_basico.py — Exemplo didático de uso do QwenClient.

Este script demonstra as principais funcionalidades da integração com o modelo
Qwen (via API da Alibaba Cloud/DashScope) aplicadas a problemas de Fenômenos
de Transporte. Cada exemplo corresponde a um modo de uso do cliente:

    1. Conversa livre (perguntar)
    2. Explicação de conceito (explicar_conceito)
    3. Resolução de exercício (resolver_exercicio)
    4. Geração de código Python (gerar_codigo)

Requisitos:
    - Variável de ambiente QWEN_API_KEY configurada
    - Bibliotecas: openai (ou requests)

Execução:
    python exemplo_basico.py

Autor: Jader Lugon Junior
Livro: Fenômenos de Transporte: Fundamentos e Modelagem Computacional
Repositório: https://github.com/JaderLugon/fenomenos-transporte-livro
"""

import sys
import os
from pathlib import Path

# ==========================================================================
# CONFIGURAÇÃO DO CAMINHO
# ==========================================================================
# Adiciona a pasta raiz do repositório ao path para importar qwen_client
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    from qwen_integration.qwen_client import QwenClient
except ImportError as e:
    print(f"❌ Erro ao importar QwenClient: {e}")
    print("\nCertifique-se de que:")
    print("  1. O arquivo qwen_client.py existe em qwen_integration/")
    print("  2. As dependências estão instaladas: pip install openai")
    sys.exit(1)


# ==========================================================================
# FUNÇÕES AUXILIARES
# ==========================================================================
def separador(titulo: str) -> None:
    """Imprime um separador visual com título."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70 + "\n")


def imprimir_resposta(resposta, titulo: str = "Resposta") -> None:
    """Imprime a resposta do Qwen de forma formatada."""
    print(f"🤖 {titulo}:")
    print("-" * 70)
    # Imprime apenas os primeiros 500 caracteres para não poluir o terminal
    texto = resposta.content
    if len(texto) > 500:
        print(texto[:500] + "\n... [truncado para visualização]")
    else:
        print(texto)
    print("-" * 70)
    print(f"📊 Modelo: {resposta.modelo}")
    print(f"⏱️  Tempo: {resposta.tempo_resposta:.2f}s")
    print(f"🔢 Tokens: {resposta.tokens_usados}")
    print()


# ==========================================================================
# EXEMPLO 1: CONVERSA LIVRE
# ==========================================================================
def exemplo_conversa_livre(client: QwenClient) -> None:
    """
    Exemplo 1: Conversa livre sobre um conceito de Fenômenos de Transporte.
    
    Aplicações: tirar dúvidas rápidas, explorar ideias, obter explicações
    informais sobre conceitos do livro.
    """
    separador("EXEMPLO 1: CONVERSA LIVRE")
    
    pergunta = (
        "Qual é a diferença física entre viscosidade dinâmica e viscosidade "
        "cinemática? Dê um exemplo prático de quando cada uma é mais útil "
        "em engenharia ambiental."
    )
    
    print(f"👤 Pergunta: {pergunta}\n")
    
    resposta = client.perguntar(pergunta)
    imprimir_resposta(resposta, "Resposta do Qwen")


# ==========================================================================
# EXEMPLO 2: EXPLICAÇÃO DE CONCEITO (Capítulo 4)
# ==========================================================================
def exemplo_explicar_conceito(client: QwenClient) -> None:
    """
    Exemplo 2: Explicação didática do Número de Reynolds.
    
    Aplicações: preparar aulas, revisar conceitos, obter explicações
    estruturadas com exemplos numéricos.
    """
    separador("EXEMPLO 2: EXPLICAR CONCEITO (Capítulo 4)")
    
    resposta = client.explicar_conceito(
        conceito="Número de Reynolds e transição laminar-turbulento",
        capitulo=4,
        nivel="graduacao",
        incluir_exemplo=True
    )
    
    imprimir_resposta(resposta, "Explicação do Conceito")


# ==========================================================================
# EXEMPLO 3: RESOLUÇÃO DE EXERCÍCIO (Capítulo 11 - Rio Macaé)
# ==========================================================================
def exemplo_resolver_exercicio(client: QwenClient) -> None:
    """
    Exemplo 3: Resolução de exercício sobre dispersão no Rio Macaé.
    
    Aplicações: validar soluções, obter passo a passo detalhado,
    aprender metodologia de resolução.
    """
    separador("EXEMPLO 3: RESOLVER EXERCÍCIO (Capítulo 11)")
    
    enunciado = """
    Para o Rio Macaé com os seguintes parâmetros:
    - Largura B = 42,2 m
    - Profundidade D = 0,71 m
    - Velocidade média U = 0,20 m/s
    - Declividade S₀ = 1,0 × 10⁻⁴
    
    Calcule:
    (a) A velocidade de atrito U*
    (b) O coeficiente de dispersão longitudinal E_L pela correlação de Liu
    (c) O coeficiente de dispersão transversal E_T pela correlação de Elder
    (d) O número de Péclet longitudinal para L = 100 m
    
    Use β = 0,011 para Liu e φ = 0,23 para Elder.
    """
    
    print(f"📝 Enunciado: {enunciado}")
    
    resposta = client.resolver_exercicio(
        enunciado=enunciado,
        capitulo=11,
        mostrar_passos=True,
        auditoria_ia=True  # Inclui verificação V&V
    )
    
    imprimir_resposta(resposta, "Solução do Exercício")


# ==========================================================================
# EXEMPLO 4: GERAÇÃO DE CÓDIGO (Capítulo 10 - Aletas)
# ==========================================================================
def exemplo_gerar_codigo(client: QwenClient) -> None:
    """
    Exemplo 4: Geração de código Python para calcular eficiência de aleta.
    
    Aplicações: criar funções reutilizáveis, implementar modelos matemáticos,
    automatizar cálculos de engenharia.
    """
    separador("EXEMPLO 4: GERAR CÓDIGO (Capítulo 10)")
    
    descricao = """
    Função Python que calcula a eficiência de uma aleta retangular de ponta
    adiabática usando a fórmula η = tanh(mL_c)/(mL_c), onde:
    
    m = sqrt(h*P / (k*A_c))
    L_c = L + t/2 (comprimento corrigido)
    
    A função deve:
    - Receber h, P, k, A_c, L, t como parâmetros
    - Validar as entradas (todos positivos)
    - Retornar η como float
    - Incluir docstring no estilo NumPy
    - Incluir exemplo de uso com dados de aleta de alumínio
    """
    
    print(f"📝 Descrição: {descricao}")
    
    resposta = client.gerar_codigo(
        descricao=descricao,
        linguagem="python",
        capitulo=10,
        incluir_testes=True,
        incluir_docstrings=True
    )
    
    imprimir_resposta(resposta, "Código Gerado")


# ==========================================================================
# EXEMPLO 5: CONVERSA COM CONTEXTO (Histórico)
# ==========================================================================
def exemplo_conversa_contexto(client: QwenClient) -> None:
    """
    Exemplo 5: Conversa mantendo contexto entre mensagens.
    
    Aplicações: aprofundar discussões, fazer perguntas de acompanhamento,
    explorar variações de um problema.
    """
    separador("EXEMPLO 5: CONVERSA COM CONTEXTO")
    
    # Primeira mensagem
    msg1 = "O que é o método LMTD em trocadores de calor?"
    print(f"👤 Mensagem 1: {msg1}")
    r1 = client.conversar(msg1)
    imprimir_resposta(r1, "Resposta 1")
    
    # Segunda mensagem (aproveita o contexto)
    msg2 = "E qual a vantagem do método ε-NTU sobre o LMTD?"
    print(f"👤 Mensagem 2: {msg2}")
    r2 = client.conversar(msg2)
    imprimir_resposta(r2, "Resposta 2")
    
    # Terceira mensagem
    msg3 = "Quando C_r = 0, o que acontece com a efetividade?"
    print(f"👤 Mensagem 3: {msg3}")
    r3 = client.conversar(msg3)
    imprimir_resposta(r3, "Resposta 3")


# ==========================================================================
# FUNÇÃO PRINCIPAL
# ==========================================================================
def main() -> None:
    """Executa todos os exemplos de uso do QwenClient."""
    
    print("=" * 70)
    print("  EXEMPLO BÁSICO — INTEGRAÇÃO COM QWEN")
    print("  Livro: Fenômenos de Transporte")
    print("=" * 70)
    
    # Inicializar cliente
    print("\n🔧 Inicializando QwenClient...")
    try:
        client = QwenClient(
            modelo="qwen3.7",
            temperatura=0.7,
            max_tokens=2048
        )
        print(f"✅ Cliente inicializado: {client}")
    except ValueError as e:
        print(f"\n❌ Erro: {e}")
        print("\n📋 Para executar este exemplo, configure a variável de ambiente:")
        print("   Linux/Mac:  export QWEN_API_KEY='sua-chave-aqui'")
        print("   Windows:    set QWEN_API_KEY=sua-chave-aqui")
        print("\n   Ou obtenha sua chave em: https://dashscope.aliyuncs.com/")
        sys.exit(1)
    
    # Executar exemplos
    exemplos = [
        ("Conversa Livre", exemplo_conversa_livre),
        ("Explicar Conceito", exemplo_explicar_conceito),
        ("Resolver Exercício", exemplo_resolver_exercicio),
        ("Gerar Código", exemplo_gerar_codigo),
        ("Conversa com Contexto", exemplo_conversa_contexto),
    ]
    
    print("\n📚 Executando exemplos...")
    print("   (Pressione Ctrl+C a qualquer momento para interromper)\n")
    
    for i, (nome, funcao) in enumerate(exemplos, 1):
        print(f"\n{'─' * 70}")
        print(f"  Executando exemplo {i}/{len(exemplos)}: {nome}")
        print(f"{'─' * 70}")
        
        try:
            funcao(client)
        except KeyboardInterrupt:
            print("\n\n⚠️  Execução interrompida pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro no exemplo '{nome}': {e}")
            continue
    
    # Salvar histórico
    print("\n💾 Salvando histórico da conversa...")
    try:
        client.salvar_historico("historico_exemplo.json")
        print(f"✅ Histórico salvo ({len(client.historico)} mensagens)")
    except Exception as e:
        print(f"⚠️  Não foi possível salvar o histórico: {e}")
    
    # Resumo final
    print("\n" + "=" * 70)
    print("  ✅ EXEMPLOS CONCLUÍDOS COM SUCESSO!")
    print("=" * 70)
    print("\n📖 Próximos passos:")
    print("   1. Explore o notebook interativo: chat_interface.ipynb")
    print("   2. Crie seus próprios prompts em prompt_templates/")
    print("   3. Consulte a documentação completa em README.md")
    print("\n🔗 Repositório: https://github.com/JaderLugon/fenomenos-transporte-livro")
    print()


# ==========================================================================
# EXECUÇÃO
# ==========================================================================
if __name__ == "__main__":
    main()