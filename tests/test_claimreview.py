import unittest
from scripts.extrair_claimreview import extract

URL="https://checador.example/noticia"
def html(body):
    return '<html><script type="application/ld+json">'+body+'</script></html>'

class ClaimReviewTest(unittest.TestCase):
    def test_extract_single(self):
        sample=html('{"@type":"ClaimReview","claimReviewed":"Afirmacao A","url":"https://checador.example/a","reviewRating":{"alternateName":"Falso"},"author":{"name":"Fonte A"}}')
        out=extract(sample,URL,"fonte")
        self.assertEqual(len(out),1)
        self.assertEqual(out[0]["original_rating"],"Falso")
        self.assertFalse(out[0]["audit_approved"])
        self.assertEqual(out[0]["discovery_status"],"pending_review")
    def test_graph_and_list(self):
        sample=html('{"@graph":[{"@type":"NewsArticle"},{"@type":["Review","ClaimReview"],"claimReviewed":"A","url":"/a"},{"@type":"ClaimReview","claimReviewed":"B","url":"/b"}]}')
        self.assertEqual(len(extract(sample,URL,"fonte")),2)
    def test_ignores_invalid_and_deduplicates(self):
        sample=html('[{"@type":"ClaimReview","claimReviewed":"A","url":"/a"},{"@type":"ClaimReview","claimReviewed":"A","url":"/a"},{"@type":"ClaimReview","claimReviewed":"B","url":"http://insecure.example/b"}]')
        self.assertEqual(len(extract(sample,URL,"fonte")),1)
    def test_ignores_broken_json(self):
        self.assertEqual(extract(html("{broken"),URL,"fonte"),[])
    def test_ignores_non_claimreview(self):
        self.assertEqual(extract(html('{"@type":"NewsArticle","headline":"x"}'),URL,"fonte"),[])

if __name__=="__main__":unittest.main()
