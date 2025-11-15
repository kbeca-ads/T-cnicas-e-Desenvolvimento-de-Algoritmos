"""
setup_files.py
Cria arquivos JSON iniciais se não existirem.
Uso: python src/setup_files.py
"""
import json
from pathlib import Path

def ensure_json(path: str, default_obj):
    """Garante que o arquivo JSON exista; cria com default_obj caso contrário."""
    p = Path(path)
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", encoding="utf-8") as f:
            json.dump(default_obj, f, ensure_ascii=False, indent=2)
        print(f"Arquivo criado: {path}")
    else:
        print(f"Arquivo já existe: {path}")

if __name__ == "__main__":
    exemplo = {
        "nome_projeto": "Técnica e Desenvolvimento de Algoritmos",
        "integrantes": [],
        "data": "2025-11-15"
    }
    ensure_json("data/exemplo.json", exemplo)
