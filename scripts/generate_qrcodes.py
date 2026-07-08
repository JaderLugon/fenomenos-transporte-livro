#!/usr/bin/env python3
"""
Gerador de QR Codes para capítulos do livro
"Fenômenos de Transporte: Fundamentos e Modelagem Computacional"

Cada QR Code contém uma URL direta para execução no Google Colab.

Uso:
    python generate_qrcodes.py                    # Gera todos os QR Codes
    python generate_qrcodes.py --chapter cap4     # Gera apenas cap4
    python generate_qrcodes.py --list             # Lista capítulos disponíveis
"""

import argparse
import qrcode
from pathlib import Path
from typing import Dict

# =============================================================================
# DICIONÁRIO DE CAPÍTULOS → URL DO COLAB
# =============================================================================
CHAPTERS: Dict[str, str] = {
    "cap1": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/01_fundamentos_fluidos.ipynb",
    "cap2": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/02_fundamentos_fluidos.ipynb",
    "cap3": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/03_balancos_conservacao.ipynb",
    "cap4": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/04_escoamento_tubulacoes.ipynb",
    "cap5": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/05_hidrodinamica_canais_abertos.ipynb",
    "cap6": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/06_percolacao_meio_poroso.ipynb",
    "cap7": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/07_transferencia_calor.ipynb",
    "cap8": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/08_transferencia_calor.ipynb",
    "cap9": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/09_trocadores_calor.ipynb",
    "cap10": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/10_aletas_superficies.ipynb",
    "cap11": "https://colab.research.google.com/github/JaderLugon/fenomenos-transporte-livro/blob/main/notebooks/11_adveccao_dispersao.ipynb"
}


def generate_qrcode(url: str, output_path: Path, size: int = 10, border: int = 4):
    """
    Gera um QR Code para uma URL simples.
    
    Args:
        url: URL a ser codificada
        output_path: Caminho para salvar o arquivo PNG
        size: Tamanho do módulo do QR Code (1-40)
        border: Largura da borda branca
    """
    qr = qrcode.QRCode(
        version=None,  # Auto-detect based on content
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Cria imagem com cores personalizadas (opcional)
    img = qr.make_image(fill_color="#0066CC", back_color="white")
    
    # Salva como PNG
    img.save(output_path, optimize=True)
    print(f"✓ QR Code salvo: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Gerador de QR Codes para Fenômenos de Transporte (Google Colab)"
    )
    parser.add_argument(
        "--chapter", "-c",
        type=str,
        help="ID do capítulo específico (ex: cap4). Omita para gerar todos."
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("qr"),
        help="Diretório de saída para os QR Codes (padrão: qr/)"
    )
    parser.add_argument(
        "--size", "-s",
        type=int,
        default=10,
        choices=range(1, 41),
        help="Tamanho do módulo QR (1-40, padrão: 10)"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="Listar capítulos disponíveis e sair"
    )
    
    args = parser.parse_args()
    
    # Criar diretório de saída se necessário
    args.output.mkdir(parents=True, exist_ok=True)
    
    if args.list:
        print("\n📚 Capítulos disponíveis:\n")
        for cid, url in CHAPTERS.items():
            notebook = url.split("/")[-1]
            print(f"  {cid:6} → {notebook}")
        print()
        return
    
    if args.chapter:
        if args.chapter not in CHAPTERS:
            print(f"❌ Capítulo '{args.chapter}' não encontrado.")
            print("Use --list para ver os capítulos disponíveis.")
            return
        
        url = CHAPTERS[args.chapter]
        output_file = args.output / f"{args.chapter}.png"
        generate_qrcode(url, output_file, args.size)
        print(f"\n🔗 URL codificada:\n{url}\n")
    else:
        print(f"🔄 Gerando QR Codes para {len(CHAPTERS)} capítulos...\n")
        for cid, url in CHAPTERS.items():
            output_file = args.output / f"{cid}.png"
            generate_qrcode(url, output_file, args.size)
        
        print(f"\n✅ Concluído! {len(CHAPTERS)} QR Codes gerados em: {args.output}/")
        print("\n📌 Para inserir no LaTeX, use:")
        print("   \\includegraphics[width=2cm]{qr/capX.png}")
        print("\n🔗 Teste com seu celular ou:")
        print("   python -m qrcode_terminal < qr/capX.png")


if __name__ == "__main__":
    main()