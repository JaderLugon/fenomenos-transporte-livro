#!/usr/bin/env python3
"""
Gerador de QR Codes para capítulos do livro
"Fenômenos de Transporte: Fundamentos e Modelagem Computacional"

Cada QR Code direciona para:
- URL do capítulo no repositório
- Parâmetros para chat contextual com Qwen
- Metadados do capítulo para cache offline

Uso:
    python generate_qrcodes.py                    # Todos os capítulos
    python generate_qrcodes.py --chapter cap4     # Capítulo específico
    python generate_qrcodes.py --list             # Lista capítulos disponíveis
"""

import argparse
import json
import qrcode
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


# Configuração dos capítulos
CHAPTERS: Dict[str, Dict] = {
    "cap1": {
        "title": "Introdução aos Fenômenos de Transporte",
        "volume": 1,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap1.tex",
        "notebook": "notebooks/01_fundamentos_fluidos.ipynb",
        "data_folder": "data/fundamentos/",
        "qwen_context": "fen_trans_vol1_cap1"
    },
    "cap2": {
        "title": "Fundamentos dos Fluidos e Viscosidade",
        "volume": 1,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap2.tex",
        "notebook": "notebooks/01_fundamentos_fluidos.ipynb",
        "data_folder": "data/fluid_properties/",
        "qwen_context": "fen_trans_vol1_cap2"
    },
    "cap3": {
        "title": "Balanços e Equações de Conservação",
        "volume": 1,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap3.tex",
        "notebook": "notebooks/02_balancos_conservacao.ipynb",
        "data_folder": "data/conservation/",
        "qwen_context": "fen_trans_vol1_cap3"
    },
    "cap4": {
        "title": "Escoamento em Tubulações e Bombeamento",
        "volume": 1,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap4.tex",
        "notebook": "notebooks/03_escoamento_tubulacoes.ipynb",
        "data_folder": "data/pipe_flow/",
        "qwen_context": "fen_trans_vol1_cap4"
    },
    "cap5": {
        "title": "Hidrodinâmica de Canais Abertos",
        "volume": 1,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap5.tex",
        "notebook": "notebooks/04_hidrodinamica_canais.ipynb",
        "data_folder": "data/rio_macae/",
        "qwen_context": "fen_trans_vol1_cap5"
    },
    "cap6": {
        "title": "Percolação em Meio Poroso",
        "volume": 1,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap6.tex",
        "notebook": "notebooks/05_percolacao_meio_poroso.ipynb",
        "data_folder": "data/porous_media/",
        "qwen_context": "fen_trans_vol1_cap6"
    },
    "cap7": {
        "title": "Fundamentos de Transferência de Calor",
        "volume": 2,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap7.tex",
        "notebook": "notebooks/06_transferencia_calor.ipynb",
        "data_folder": "data/heat_transfer/",
        "qwen_context": "fen_trans_vol2_cap7"
    },
    "cap8": {
        "title": "Transferência de Calor em Solos",
        "volume": 2,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap8.tex",
        "notebook": "notebooks/06_transferencia_calor.ipynb",
        "data_folder": "data/soil_thermal/",
        "qwen_context": "fen_trans_vol2_cap8"
    },
    "cap9": {
        "title": "Aletas e Superfícies Estendidas",
        "volume": 2,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap9.tex",
        "notebook": "notebooks/07_aletras_superficies.ipynb",
        "data_folder": "data/fins/",
        "qwen_context": "fen_trans_vol2_cap9"
    },
    "cap10": {
        "title": "Trocadores de Calor",
        "volume": 2,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap10.tex",
        "notebook": "notebooks/08_trocadores_calor.ipynb",
        "data_folder": "data/heat_exchangers/",
        "qwen_context": "fen_trans_vol2_cap10"
    },
    "cap11": {
        "title": "Advecção e Dispersão em Corpos Hídricos",
        "volume": 2,
        "url_base": "https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/latex/cap11.tex",
        "notebook": "notebooks/09_adveccao_dispersao.ipynb",
        "data_folder": "data/dispersion/",
        "qwen_context": "fen_trans_vol2_cap11"
    }
}


def build_qr_payload(chapter_id: str, include_chat: bool = True) -> str:
    """
    Constrói o payload JSON para o QR Code.
    
    O payload contém:
    - URL do capítulo
    - Metadados para contexto da IA
    - Informações de versão e data
    """
    chap = CHAPTERS[chapter_id]
    
    payload = {
        "chapter": chapter_id,
        "title": chap["title"],
        "volume": chap["volume"],
        "urls": {
            "latex": chap["url_base"],
            "notebook": f"https://github.com/JaderLugon/fenomenos-transporte-livro/blob/main/{chap['notebook']}",
            "data": f"https://github.com/JaderLugon/fenomenos-transporte-livro/tree/main/{chap['data_folder']}"
        },
        "qwen": {
            "enabled": include_chat,
            "context_id": chap["qwen_context"],
            "api_endpoint": "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
        },
        "metadata": {
            "generated": datetime.now().isoformat(),
            "version": "1.0.0-pre",
            "license": "CC-BY-NC-SA-4.0"
        }
    }
    
    # Codifica como string JSON compacta para QR Code menor
    return json.dumps(payload, separators=(',', ':'))


def generate_qrcode(
    chapter_id: str, 
    output_dir: Path,
    size: int = 10,
    border: int = 4,
    include_chat: bool = True
) -> Path:
    """
    Gera QR Code para um capítulo.
    
    Args:
        chapter_id: ID do capítulo (ex: 'cap4')
        output_dir: Diretório para salvar o QR Code
        size: Tamanho do módulo do QR Code (1-40)
        border: Largura da borda branca
        include_chat: Incluir parâmetros para chat com IA
        
    Returns:
        Path do arquivo gerado
    """
    if chapter_id not in CHAPTERS:
        raise ValueError(f"Capítulo '{chapter_id}' não encontrado. Use --list para ver disponíveis.")
    
    # Cria diretório se necessário
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Constrói payload e gera QR
    payload = build_qr_payload(chapter_id, include_chat)
    
    qr = qrcode.QRCode(
        version=None,  # Auto-detect
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=size,
        border=border,
    )
    qr.add_data(payload)
    qr.make(fit=True)
    
    # Cria imagem com cores da marca
    img = qr.make_image(
        fill_color="#0066CC",  # Azul Transporte
        back_color="white"
    )
    
    # Salva arquivo
    output_path = output_dir / f"{chapter_id}.png"
    img.save(output_path, optimize=True)
    
    # Gera também versão SVG para LaTeX
    svg_path = output_dir / f"{chapter_id}.svg"
    img.save(svg_path)
    
    # Gera arquivo de metadados auxiliar
    meta_path = output_dir / f"{chapter_id}.json"
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(CHAPTERS[chapter_id], f, indent=2, ensure_ascii=False)
    
    print(f"✓ QR Code gerado: {output_path}")
    print(f"  SVG: {svg_path}")
    print(f"  Metadados: {meta_path}")
    
    return output_path


def generate_all(output_dir: Path, **kwargs) -> List[Path]:
    """Gera QR Codes para todos os capítulos."""
    paths = []
    for chap_id in CHAPTERS:
        try:
            path = generate_qrcode(chap_id, output_dir, **kwargs)
            paths.append(path)
        except Exception as e:
            print(f"✗ Erro ao gerar {chap_id}: {e}")
    return paths


def main():
    parser = argparse.ArgumentParser(
        description="Gerador de QR Codes para Fenômenos de Transporte"
    )
    parser.add_argument(
        "--chapter", "-c",
        type=str,
        help="ID do capítulo específico (ex: cap4). Omita para gerar todos."
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("qr/generated"),
        help="Diretório de saída (padrão: qr/generated)"
    )
    parser.add_argument(
        "--size", "-s",
        type=int,
        default=10,
        choices=range(1, 41),
        help="Tamanho do módulo QR (1-40, padrão: 10)"
    )
    parser.add_argument(
        "--no-chat",
        action="store_true",
        help="Não incluir parâmetros de chat com IA no QR Code"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="Listar capítulos disponíveis e sair"
    )
    
    args = parser.parse_args()
    
    if args.list:
        print("\n📚 Capítulos disponíveis:\n")
        for cid, info in CHAPTERS.items():
            vol = "I" if info["volume"] == 1 else "II"
            print(f"  {cid:6} | Vol {vol} | {info['title']}")
        print()
        return
    
    include_chat = not args.no_chat
    
    if args.chapter:
        generate_qrcode(args.chapter, args.output, args.size, include_chat=include_chat)
    else:
        paths = generate_all(args.output, size=args.size, include_chat=include_chat)
        print(f"\n✓ Gerados {len(paths)} QR Codes em {args.output}/")
        print("\n📌 Para inserir no LaTeX, use:")
        print("   \\includegraphics[width=2cm]{qr/generated/capX.png}")
        print("\n🔗 Teste os QR Codes com seu celular ou:")
        print("   python -m qrcode_terminal < qr/generated/capX.png")


if __name__ == "__main__":
    main()