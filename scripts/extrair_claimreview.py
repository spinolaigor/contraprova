#!/usr/bin/env python3
"""Descobre ClaimReview em JSON-LD sem produzir ou publicar vereditos próprios.

Entrada: arquivo HTML local ou URL HTTPS explicitamente autorizada.
Saída: registros candidatos, sempre pending_review.
Sem dependências externas. Não rastreia páginas por conta própria.
"""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit

MAX_SCRIPT=1_000_000

class StructuredDataParser(HTMLParser):
    def __init__(self):
        super().__init__();self.active=False;self.chunks=[];self.scripts=[]
    def handle_starttag(self,tag,attrs):
        if tag!="script":return
        attributes=dict(attrs)
        self.active=attributes.get("type","").strip().lower()=="application/ld+json"
        self.chunks=[]
    def handle_data(self,data):
        if self.active and sum(map(len,self.chunks))+len(data)<=MAX_SCRIPT:self.chunks.append(data)
    def handle_endtag(self,tag):
        if tag=="script" and self.active:
            self.scripts.append("".join(self.chunks))
            self.active=False;self.chunks=[]

def walk(node):
    if isinstance(node,list):
        for part in node:yield from walk(part)
    elif isinstance(node,dict):
        typ=node.get("@type",[])
        types=typ if isinstance(typ,list) else [typ]
        if any(str(t).rsplit("/",1)[-1]=="ClaimReview" for t in types):
            yield node
        if "@graph" in node:yield from walk(node["@graph"])

def https_url(url):
    if not isinstance(url,str):return None
    p=urlsplit(url)
    if p.scheme!="https" or not p.hostname or p.username or p.password:return None
    return url

def get_name(value):
    if isinstance(value,str):return value
    if isinstance(value,dict):return value.get("name") or ""
    return ""

def extract(html_text,page_url,source_id):
    """Conserva as classificações ORIGINAIS como pistas, não como vereditos aprovados."""
    parser=StructuredDataParser();parser.feed(html_text)
    records=[];seen=set()
    for script in parser.scripts:
        try:payload=json.loads(script)
        except (ValueError,TypeError):continue
        for item in walk(payload):
            claim=item.get("claimReviewed")
            if not isinstance(claim,str) or not claim.strip():continue
            raw_url=item.get("url",page_url)
            if isinstance(raw_url,dict):raw_url=raw_url.get("@id","")
            item_url=https_url(urljoin(page_url,raw_url)) if isinstance(raw_url,str) else None
            if not item_url:continue
            rating=item.get("reviewRating") or {}
            if not isinstance(rating,dict):rating={}
            original_rating=rating.get("alternateName") or rating.get("name")
            author=get_name(item.get("author"))
            key=hashlib.sha256((source_id+"|"+item_url+"|"+claim.strip()).encode()).hexdigest()[:20]
            if key in seen:continue
            seen.add(key)
            records.append({
                "candidate_id":"cr-"+key,
                "source_id":source_id,
                "source_url":item_url,
                "claim_reviewed":claim.strip(),
                "review_publisher":author,
                "original_rating":original_rating if isinstance(original_rating,str) else None,
                "published_at":item.get("datePublished"),
                "discovery_status":"pending_review",
                "audit_approved":False,
                "provenance":"jsonld_claimreview"
            })
    return records

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--html",required=True,help="HTML já coletado de fonte permitida")
    parser.add_argument("--url",required=True,help="URL HTTPS da página original")
    parser.add_argument("--source-id",required=True)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    if not https_url(args.url):parser.error("--url deve ser HTTPS")
    data=Path(args.html).read_text(encoding="utf-8")
    result={"schema_version":"0.5.0","kind":"claimreview_candidates",
            "source_url":args.url,"items":extract(data,args.url,args.source_id)}
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("Candidatos extraídos:",len(result["items"]))

if __name__=="__main__":main()
