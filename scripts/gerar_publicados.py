#!/usr/bin/env python3
"""Exporta somente registros auditados; falha se houver inconsistência."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "auditoria" / "registros.json"
DEST = ROOT / "data" / "publicados.json"
REQUIRED = ("id", "afirmacao", "autor", "evento", "data", "verificacoes", "revisao")

def exportar(registros):
    ids = set()
    saida = []
    for item in registros:
        if not isinstance(item, dict):
            raise ValueError("Registro inválido")
        uid = item.get("id")
        if not isinstance(uid, str) or not uid:
            raise ValueError("ID ausente")
        if uid in ids:
            raise ValueError(f"ID duplicado: {uid}")
        ids.add(uid)
        if item.get("status") != "publicado":
            continue
        for field in REQUIRED:
            if not item.get(field):
                raise ValueError(f"{uid}: campo obrigatório ausente: {field}")
        if item.get("demonstrativo") is not False:
            raise ValueError(f"{uid}: registro demonstrativo não publicável")
        revisao = item["revisao"]
        if not isinstance(revisao, dict) or revisao.get("aprovado") is not True or not revisao.get("data") or not revisao.get("responsavel"):
            raise ValueError(f"{uid}: revisão humana incompleta")
        verificacoes = item["verificacoes"]
        if not isinstance(verificacoes, list) or not verificacoes:
            raise ValueError(f"{uid}: sem verificações")
        for v in verificacoes:
            if not isinstance(v, dict) or not all(v.get(k) for k in ("fonte", "url", "veredito", "data")):
                raise ValueError(f"{uid}: verificação sem origem ou veredito")
            if not str(v["url"]).startswith("https://"):
                raise ValueError(f"{uid}: URL de verificação inválida")
            if v.get("tipo") == "automatizada" and v.get("revisao_humana") is not True:
                raise ValueError(f"{uid}: veredito exclusivamente automatizado")
        saida.append(item)
    return {"schema_version": 1, "politica": "Somente registros auditados e aprovados", "total": len(saida), "registros": saida}

def main():
    dados = json.loads(SOURCE.read_text(encoding="utf-8"))
    if not isinstance(dados, list):
        raise ValueError("A fonte deve ser uma lista")
    exportado = exportar(dados)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(exportado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Registros publicados: {exportado['total']}")

if __name__ == "__main__":
    main()
