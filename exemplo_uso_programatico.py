from qwen_integration.qwen_client import QwenClient

client = QwenClient(api_key="sua-chave")

# Perguntar sobre um conceito
resposta = client.ask(
    chapter="cap4",
    topic="Equação de Colebrook-White",
    level="graduation"  # ou "postgrad"
)
print(resposta)

# Resolver um exercício passo a passo
solucao = client.solve_exercise(
    chapter="cap4",
    exercise=1,
    show_steps=True
)