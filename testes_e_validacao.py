# Executar testes unitários
pytest tests/ -v

# Executar validação de notebooks
python scripts/validate_notebooks.py

# Gerar relatório de cobertura
pytest --cov=src tests/ --cov-report=html