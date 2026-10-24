#!/usr/bin/env python3
"""Prepara apenas os arquivos públicos; a fila editorial fica no GitHub."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]

def preparar(destino):
    destino = Path(destino)
    if destino.exists():
        shutil.rmtree(destino)
    destino.mkdir(parents=True)
    for arquivo in ('index.html', 'fontes.html', 'checagens.html', '.nojekyll'):
        shutil.copy2(ROOT / arquivo, destino / arquivo)
    (destino / 'data').mkdir()
    shutil.copy2(ROOT / 'data/publicados.json', destino / 'data/publicados.json')
    shutil.copy2(ROOT / 'data/checagens_atribuidas.json', destino / 'data/checagens_atribuidas.json')
    shutil.copy2(ROOT / 'data/README.md', destino / 'data/README.md')
    for pasta in ('docs',):
        shutil.copytree(ROOT / pasta, destino / pasta, ignore=shutil.ignore_patterns('DOSSIES_*'))
    return destino

if __name__ == '__main__':
    preparar(ROOT / '_site')
    print('Site preparado em _site; dossiês disponíveis somente no repositório.')
