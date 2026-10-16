# -*- coding: utf-8 -*-
"""
Hierarquia completa de modelos de escoamento
Livro: Fenômenos de Transporte na Engenharia e Meio Ambiente — Vol. I
Capítulo 7, Figura hierarquia_completa

Gera:
    figuras/hierarquia_modelos.pdf  (vetorial, para inclusão no LaTeX)
    figuras/hierarquia_modelos.png  (300 dpi, para slides/material web)

Uso:
    python gera_fig_hierarquia_modelos.py
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ----------------------------------------------------------------------
# Paleta padrão do livro
# ----------------------------------------------------------------------
AZUL    = "#0066CC"   # azulTransporte
LARANJA = "#FF8C00"   # laranjaGrad
VERDE   = "#00994C"   # verdePos
ROXO    = "#7B1FA2"   # roxoPoroso (meios porosos)
CINZA   = "#404040"   # texto e rótulos

OUT_DIR = "figuras"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "mathtext.default": "regular",
})

fig, ax = plt.subplots(figsize=(12, 6.8))          # canvas mais largo: textos ocupam fração menor
fig.subplots_adjust(left=0.01, right=0.99,         # eixos ocupam quase todo o canvas
                    top=0.99, bottom=0.01)
ax.set_xlim(-0.10, 1.10)   # folga lateral de 10%
ax.set_ylim(-0.08, 1.08)   # folga vertical
ax.axis("off")

# ----------------------------------------------------------------------
# Funções auxiliares
# ----------------------------------------------------------------------
def node(x, y, titulo, subtitulo, cor, w=0.22, h=0.10):
    """Caixa arredondada com título em negrito e subtítulo discreto."""
    ax.add_patch(FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.008,rounding_size=0.02",
        linewidth=1.6,
        edgecolor=cor,
        facecolor=to_rgba(cor, 0.12),
        zorder=3))
    ax.text(x, y + 0.020, titulo, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=cor, zorder=4)
    ax.text(x, y - 0.022, subtitulo, ha="center", va="center",
            fontsize=8.0, color=CINZA, zorder=4)


def seta(x1, y1, x2, y2, cor):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="-|>", mutation_scale=13,
        linewidth=1.8, color=cor, zorder=2))


def rotulo(x, y, texto):
    """Rótulo da seta com fundo branco para não brigar com o traço."""
    ax.text(x, y, texto, ha="center", va="center", fontsize=7.8,
            color=CINZA, zorder=5,
            bbox=dict(boxstyle="round,pad=0.25", fc="white",
                      ec="none", alpha=0.90))

# ----------------------------------------------------------------------
# Nós da hierarquia
# ----------------------------------------------------------------------
# Nível 0 — equação completa
node(0.50, 0.90, "Navier–Stokes", "equação completa (Cap. 7)",
     AZUL, w=0.30, h=0.11)

# Nível 1 — primeiras simplificações
node(0.20, 0.62, "Euler",            "fluido ideal",          VERDE)
node(0.50, 0.62, "Hagen–Poiseuille", "tubo laminar (Cap. 4)", LARANJA)
node(0.80, 0.62, "Lei de Darcy",     "meio poroso (Cap. 6)",  ROXO)

# Nível 2 — modelos aplicados
node(0.10, 0.30, "Bernoulli",    "linha de corrente (Cap. 4)", VERDE, w=0.19, h=0.09)
node(0.31, 0.30, "Saint-Venant", "águas rasas 1D (Cap. 5)",    VERDE, w=0.19, h=0.09)
node(0.69, 0.30, "Forchheimer",  r"$Re_g$ moderado (Cap. 6)",  ROXO,  w=0.19, h=0.09)
node(0.90, 0.30, "Brinkman",     "fronteiras (Cap. 6)",        ROXO,  w=0.19, h=0.09)

# ----------------------------------------------------------------------
# Setas (simplificações)
# ----------------------------------------------------------------------
# Nível 0 -> 1
seta(0.40, 0.845, 0.22, 0.675, VERDE)
seta(0.50, 0.845, 0.50, 0.675, LARANJA)
seta(0.60, 0.845, 0.78, 0.675, ROXO)
# Nível 1 -> 2
seta(0.15, 0.565, 0.11, 0.350, VERDE)
seta(0.25, 0.565, 0.30, 0.350, VERDE)
seta(0.75, 0.565, 0.70, 0.350, ROXO)
seta(0.85, 0.565, 0.89, 0.350, ROXO)

# ----------------------------------------------------------------------
# Rótulos das setas (termos desprezados / hipóteses)
# ----------------------------------------------------------------------
rotulo(0.26, 0.78, "viscosidade desprezível\n($\\nu \\to 0$, $Re \\gg 1$)")
rotulo(0.50, 0.76, "tubo circular, laminar,\ncompletamente desenvolvido")
rotulo(0.74, 0.78, "média volumétrica (VER),\nescoamento lento ($Re_g \\ll 1$)")
rotulo(0.115, 0.465, "permanente, integrar\nna linha de corrente")
rotulo(0.295, 0.465, "pressão hidrostática,\nintegrar na vertical")
rotulo(0.705, 0.465, "$Re_g$ moderado\n($1 < Re_g < 100$)")
rotulo(0.895, 0.465, "próximo a fronteiras\ne interfaces")

# ----------------------------------------------------------------------
# Exportação
# ----------------------------------------------------------------------
os.makedirs(OUT_DIR, exist_ok=True)
fig.savefig(os.path.join(OUT_DIR, "hierarquia_modelos.pdf"), bbox_inches="tight")
fig.savefig(os.path.join(OUT_DIR, "hierarquia_modelos.png"), dpi=300, bbox_inches="tight")
print(f"Figuras geradas em {OUT_DIR}/hierarquia_modelos.pdf e .png")