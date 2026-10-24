import unittest
from scripts.gerar_publicados import exportar

class PublicacaoTest(unittest.TestCase):
    def test_ignora_pendentes(self):
        self.assertEqual(exportar([{"id":"a","status":"em_auditoria"}])["total"], 0)

    def test_rejeita_duplicacao(self):
        with self.assertRaises(ValueError):
            exportar([{"id":"a"},{"id":"a"}])

    def test_rejeita_publicacao_sem_revisao(self):
        with self.assertRaises(ValueError):
            exportar([{"id":"a","status":"publicado"}])

    def test_aceita_registro_auditado(self):
        r={"id":"a","status":"publicado","demonstrativo":False,
           "afirmacao":"Texto","autor":"Candidato","evento":"Debate","data":"2026-10-23",
           "revisao":{"aprovado":True,"data":"2026-10-24","responsavel":"Revisor"},
           "verificacoes":[{"fonte":"Veículo","url":"https://example.org/item",
                             "veredito":"falso","data":"2026-10-24"}]}
        self.assertEqual(exportar([r])["total"],1)

if __name__ == "__main__":
    unittest.main()
