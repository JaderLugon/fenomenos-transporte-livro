#!/usr/bin/env python3
"""Valida execução de todos os notebooks da coleção."""
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path

def validate_notebook(nb_path, timeout=600):
    """Executa um notebook e retorna status."""
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=timeout, kernel_name='python3')
    try:
        ep.preprocess(nb, {'metadata': {'path': nb_path.parent}})
        print(f"✓ {nb_path.name}: OK")
        return True
    except Exception as e:
        print(f"✗ {nb_path.name}: {e}")
        return False

if __name__ == "__main__":
    notebooks_dir = Path("notebooks")
    success = all(validate_notebook(nb) for nb in notebooks_dir.glob("*.ipynb"))
    print(f"\n{'✓ Todos os notebooks validados!' if success else '✗ Alguns notebooks falharam.'}")