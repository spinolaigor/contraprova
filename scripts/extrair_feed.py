#!/usr/bin/env python3
"""Descoberta offline de entradas RSS/Atom, com URLs canônicas e IDs estáveis."""
import hashlib
from urllib.parse import urljoin, urlsplit, urlunsplit, parse_qsl, urlencode
import xml.etree.ElementTree as ET

TRACKING={"utm_source","utm_medium","utm_campaign","utm_term","utm_content","fbclid","gclid"}
def canonical(url,base):
    joined=urljoin(base,url.strip())
    p=urlsplit(joined)
    if p.scheme!="https" or not p.hostname or p.username or p.password:return None
    query=urlencode([(k,v) for k,v in parse_qsl(p.query,keep_blank_values=True) if k.lower() not in TRACKING])
    return urlunsplit((p.scheme,p.netloc.lower(),p.path or "/",query,""))

def localname(tag):
    return tag.rsplit("}",1)[-1].lower()

def first_text(node,name):
    for child in node:
        if localname(child.tag)==name and child.text:
            return child.text.strip()
    return ""

def parse_feed(xml,source_url,source_id,limit=100):
    """Nunca transforma entradas de feed em afirmações verificadas."""
    if len(xml)>2_000_000:raise ValueError("Feed excede limite")
    root=ET.fromstring(xml)
    if localname(root.tag) not in ("rss","feed","rdf"):raise ValueError("Não é RSS/Atom")
    entries=[n for n in root.iter() if localname(n.tag) in ("item","entry")]
    found={}
    for entry in entries[:limit]:
        link=""
        for child in entry:
            if localname(child.tag)=="link":
                if child.attrib.get("rel","alternate")!="alternate":continue
                link=child.attrib.get("href") or (child.text or "").strip()
                if link:break
        url=canonical(link,source_url) if link else None
        if not url:continue
        identifier="feed-"+hashlib.sha256((source_id+"|"+url).encode()).hexdigest()[:20]
        found[identifier]={"candidate_id":identifier,"source_id":source_id,"url":url,
            "title":first_text(entry,"title")[:300],
            "published_at":first_text(entry,"pubdate") or first_text(entry,"published") or first_text(entry,"updated") or None,
            "discovery_status":"pending_review","audit_approved":False,"provenance":"rss_atom"}
    return list(found.values())
