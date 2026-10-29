"""One-off/maintenance: snapshot the live HTML of every generated page into tools/synced_pages.json,
so build_pages.py reproduces hand-edited pages exactly. Run from repo root BEFORE editing content.py
if pages were edited directly."""
import json, os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from content import PAGES
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sm = open(os.path.join(ROOT, "sitemap.xml")).read()
paths = re.findall(r"<loc>https://www.superroutine.in(/[^<]*)</loc>", sm)
known = {p["path"] for p in PAGES}
out = {}
for path in paths:
    if path == "/": continue
    s = open(os.path.join(ROOT, path.strip("/"), "index.html"), encoding="utf-8").read()
    g = lambda pat: re.search(pat, s, re.S)
    ld = json.loads(g(r'<script type="application/ld\+json">(.*?)</script>').group(1))
    graph = ld["@graph"]
    bc = [x for x in graph if x["@type"] == "BreadcrumbList"][0]["itemListElement"]
    page = [x for x in graph if x["@type"] not in ("BreadcrumbList", "Person", "Organization", "FAQPage")][0]
    faq = [x for x in graph if x["@type"] == "FAQPage"]
    art = g(r"<article>\n<h1>(.*?)</h1>\n(.*?)</article>")
    h1, rest = art.group(1), art.group(2)
    m = re.match(r'(<p class="byline">.*?</p>\n)?(.*)', rest, re.S)
    has_byline, inner = bool(m.group(1)), m.group(2).rstrip("\n")
    pri = re.search(r"<loc>https://www.superroutine.in%s</loc><lastmod>[^<]*</lastmod><priority>([^<]*)" % re.escape(path), sm).group(1)
    out[path] = {
        "path": path, "title": html.unescape(g(r"<title>(.*?)</title>").group(1)),
        "description": html.unescape(g(r'<meta name="description" content="(.*?)">').group(1)),
        "h1": h1, "inner": inner, "byline": has_byline, "priority": pri,
        "schema_type": page["@type"], "published": page.get("datePublished"),
        "crumb": bc[-1]["name"], "crumbs": [[c["name"], c["item"].replace("https://www.superroutine.in", "")] for c in bc[1:-1]],
        "about": (page.get("about") or {}).get("name"),
        "faq": [[q["name"], q["acceptedAnswer"]["text"]] for q in faq[0]["mainEntity"]] if faq else [],
    }
json.dump(out, open(os.path.join(ROOT, "tools", "synced_pages.json"), "w"), ensure_ascii=False, indent=1)
print(len(out), "pages;", "new:", [p for p in out if p not in known])
