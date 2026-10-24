import unittest
from scripts.extrair_feed import parse_feed,canonical

BASE="https://example.org/feed.xml"
class FeedTest(unittest.TestCase):
    def test_rss(self):
        xml='<rss><channel><item><title>Notícia</title><link>https://example.org/a?utm_source=x</link><pubDate>Hoje</pubDate></item></channel></rss>'
        out=parse_feed(xml,BASE,"a")
        self.assertEqual(len(out),1)
        self.assertEqual(out[0]["url"],"https://example.org/a")
        self.assertFalse(out[0]["audit_approved"])
    def test_atom(self):
        xml='<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>A</title><link href="/noticia" rel="alternate"/></entry></feed>'
        self.assertEqual(parse_feed(xml,BASE,"a")[0]["url"],"https://example.org/noticia")
    def test_rejects_insecure(self):
        xml='<rss><channel><item><link>http://example.org/a</link></item></channel></rss>'
        self.assertEqual(parse_feed(xml,BASE,"a"),[])
    def test_dedupe(self):
        xml='<rss><channel><item><link>/a</link></item><item><link>/a?fbclid=123</link></item></channel></rss>'
        self.assertEqual(len(parse_feed(xml,BASE,"a")),1)
    def test_rejects_non_feed(self):
        with self.assertRaises(ValueError):parse_feed('<html/>',BASE,"a")

if __name__=="__main__":unittest.main()
