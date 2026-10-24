import copy
import json
from pathlib import Path
import tempfile
import unittest

from scripts.gerar_publicados import exportar
from scripts.preparar_site import preparar

ROOT = Path(__file__).resolve().parents[1]

class EntregaTest(unittest.TestCase):
    def test_pesquisa_nunca_vaza_para_indicadores(self):
        dossies = json.loads((ROOT/'data/auditoria/dossies.json').read_text())
        registros = json.loads((ROOT/'data/auditoria/registros.json').read_text())
        ids = [d['claim_id'] for d in dossies]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertLessEqual(len(ids), 30)
        self.assertEqual(set(ids), {r['id'] for r in registros})
        publicados = {r['id'] for r in exportar(registros)['registros']}
        for d in dossies:
            if d['status'] == 'pendente':
                self.assertNotIn(d['claim_id'], publicados)
                self.assertIsNone(d['revisor'])
            self.assertTrue(d['checagens'])
            self.assertTrue(d['limites'])
            self.assertIs(d['parafrase_explicita'], True)
            self.assertTrue(all(v['url'].startswith('https://') for v in d['checagens']))

    def test_fontes_e_repeticoes_rastreaveis(self):
        catalogo = json.loads((ROOT/'data/auditoria/fontes_consultadas.json').read_text())
        fontes = {s['id']: s for s in catalogo['fontes']}
        dossies = json.loads((ROOT/'data/auditoria/dossies.json').read_text())
        ocorrencias = set()
        for d in dossies:
            for o in d['ocorrencias']:
                chave = (d['claim_id'], o['debate'], o['data'])
                self.assertNotIn(chave, ocorrencias)
                ocorrencias.add(chave)
            for v in d['checagens']:
                self.assertEqual(v['url'], fontes[v['fonte_id']]['url'])
                self.assertIn(fontes[v['fonte_id']]['evento'], [o['debate'] for o in d['ocorrencias']])

    def test_aprovacao_exige_booleano_explicito(self):
        r = dict(id='teste',status='publicado',demonstrativo=False,
                 afirmacao='Teste',autor='Teste',evento='Teste',data='2026-10-23',
                 revisao=dict(aprovado=True,data='2026-10-24',responsavel='editor'),
                 verificacoes=[dict(fonte='Fonte',url='https://example.org',veredito='rótulo original',data='2026-10-24')])
        for valor in ('false', 'true', 1, [], None):
            item = copy.deepcopy(r)
            item['revisao']['aprovado'] = valor
            with self.assertRaises(ValueError):
                exportar([item])
        item = copy.deepcopy(r)
        item['verificacoes'][0].update(tipo='automatizada', revisao_humana='false')
        with self.assertRaises(ValueError):
            exportar([item])
        self.assertEqual(exportar([r])['registros'][0]['verificacoes'][0]['veredito'], 'rótulo original')

    def test_pages_nao_embarca_fila_de_auditoria(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = preparar(Path(tmp)/'site')
            self.assertTrue((dest/'fontes.html').is_file())
            self.assertTrue((dest/'data/publicados.json').is_file())
            self.assertFalse((dest/'data/auditoria').exists())
            self.assertFalse((dest/'docs/DOSSIES_REVISAO_2026-10-24.md').exists())
            self.assertFalse((dest/'WORK.md').exists())

if __name__ == '__main__':
    unittest.main()
