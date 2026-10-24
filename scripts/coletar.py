#!/usr/bin/env python3
"""Coleta metadados de páginas de fontes; nunca atribui vereditos."""
import argparse
import datetime as dt
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser

ROOT=Path(__file__).resolve().parents[1]
SOURCES=ROOT/"data/monitoramento/fontes.json"
OUTPUT=ROOT/"data/monitoramento/descobertas.json"
USER_AGENT="ContraprovaResearchBot/0.4 (+https://github.com/spinolaigor/contraprova)"
MAX_BYTES=500_000

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.in_title=False; self.title=[]; self.meta={}; self.canonical=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="title": self.in_title=True
        if tag=="meta":
            k=(a.get("property") or a.get("name") or "").lower()
            if k and a.get("content"): self.meta[k]=a["content"][:500]
        if tag=="link" and "canonical" in (a.get("rel") or "").lower() and a.get("href"):
            self.canonical=a["href"]
    def handle_endtag(self,tag):
        if tag=="title": self.in_title=False
    def handle_data(self,data):
        if self.in_title: self.title.append(data)

def safe_url(url):
    p=urllib.parse.urlsplit(url)
    if p.scheme!="https" or not p.hostname or p.username or p.password:
        raise ValueError("Somente URLs HTTPS públicas")
    if p.hostname in ("localhost","127.0.0.1","::1") or p.hostname.endswith((".local",".internal")):
        raise ValueError("Host não permitido")
    return url

def fetch(source,timeout=12):
    url=safe_url(source["url"])
    p=urllib.parse.urlsplit(url)
    robots=urllib.robotparser.RobotFileParser()
    robots.set_url(f"{p.scheme}://{p.netloc}/robots.txt")
    robots.read()
    if not robots.can_fetch(USER_AGENT,url):
        raise ValueError("robots.txt não permite coleta")
    req=urllib.request.Request(url,headers={"User-Agent":USER_AGENT,"Accept":"text/html"})
    with urllib.request.urlopen(req,timeout=timeout) as response:
        final=safe_url(response.geturl())
        ctype=response.headers.get("Content-Type","").lower()
        if "text/html" not in ctype and "application/xhtml+xml" not in ctype:
            raise ValueError("Formato de resposta não HTML")
        payload=response.read(MAX_BYTES+1)
        if len(payload)>MAX_BYTES: raise ValueError("Página muito grande")
        encoding=response.headers.get_content_charset() or "utf-8"
        parser=Parser();parser.feed(payload.decode(encoding,errors="replace"))
        canonical=safe_url(urllib.parse.urljoin(final,parser.canonical or final))
        return {"url":canonical,"title":html.unescape(parser.meta.get("og:title") or "".join(parser.title).strip())[:300],
                "published_at":parser.meta.get("article:published_time"),
                "modified_at":parser.meta.get("article:modified_time"),
                "content_fingerprint":hashlib.sha256(payload).hexdigest()[:20]}

def run(sources_path=SOURCES,output_path=OUTPUT,fetcher=fetch):
    sources=json.loads(Path(sources_path).read_text(encoding="utf-8"))["sources"]
    path=Path(output_path)
    old=json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"items":[]}
    known={i["source_id"]:i for i in old.get("items",[])}
    changed=False;errors=[]
    for source in sources:
        if not source.get("enabled",False): continue
        try:
            data=fetcher(source)
            if not data["title"]: raise ValueError("Título ausente")
            previous=known.get(source["id"])
            if previous and previous.get("content_fingerprint")==data["content_fingerprint"]: continue
            now=dt.datetime.now(dt.timezone.utc).isoformat()
            known[source["id"]]={"source_id":source["id"],"source_name":source["name"],
                "source_type":source["type"],**data,"discovery_status":"pending_review",
                "fact_check_verdict":None,"first_seen_at":previous["first_seen_at"] if previous else now,
                "last_changed_at":now}
            changed=True
        except (OSError,ValueError,UnicodeError,urllib.error.URLError) as e:
            errors.append(f"{source['id']}: {type(e).__name__}: {e}")
    if changed:
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps({"schema_version":"0.4.0","generated_at":dt.datetime.now(dt.timezone.utc).isoformat(),
            "items":sorted(known.values(),key=lambda x:x["source_id"])},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for e in errors: print("WARN:",e,file=sys.stderr)
    print(f"updated={changed} sources={len(sources)} failed={len(errors)}")
    return changed,errors

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--sources",default=str(SOURCES))
    parser.add_argument("--output",default=str(OUTPUT))
    args=parser.parse_args()
    run(args.sources,args.output)
