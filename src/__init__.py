"""
fenomenos_transporte — Módulos reutilizáveis do livro
"Fenômenos de Transporte: Fundamentos e Modelagem Computacional".

Autor: Jader Lugon Junior
Repositório: https://github.com/JaderLugon/fenomenos-transporte-livro
"""

from . import hidrodinamica
from . import transferencia_calor
from . import meio_poroso
from . import dispersao
from . import problemas_inversos
from . import utils

__version__ = "1.0.0"
__author__ = "Jader Lugon Junior"

__all__ = [
    "hidrodinamica",
    "transferencia_calor",
    "meio_poroso",
    "dispersao",
    "problemas_inversos",
    "utils",
]