"""Builds the Super Routine content pages (pack, ingredient, about) and sitemap.xml.

Run from the repo root:  python3 tools/build_pages.py
Page content lives in tools/content.py. Edit it there, then re-run this script.
"""
import json, os, sys, html, datetime

sys.path.insert(0, os.path.dirname(__file__))
from content import AUTHOR, PAGES, SITE  # noqa: E402

TODAY = datetime.date.today().isoformat()
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [("Day Pack", "/day-pack/"), ("Night Pack", "/night-pack/"),
       ("Ingredients", "/ingredients/"), ("About", "/about/")]


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def page_html(p):
    url = SITE + p["path"]
    crumbs = [("Home", "/")] + p.get("crumbs", []) + [(p["crumb"], p["path"])]
    crumb_html = " / ".join(
        f'<a href="{c[1]}">{esc(c[0])}</a>' if i < len(crumbs) - 1 else esc(c[0])
        for i, c in enumerate(crumbs))

    graph = [{
        "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c[0], "item": SITE + c[1]}
                            for i, c in enumerate(crumbs)]}]
    page_type = p.get("schema_type", "MedicalWebPage")
    node = {"@type": page_type, "@id": url + "#page", "url": url, "name": strip_tags(p["h1"]),
            "headline": strip_tags(p["h1"]), "description": p["description"], "inLanguage": "en-IN",
            "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"},
            "datePublished": p.get("published", TODAY), "dateModified": TODAY}
    if page_type != "AboutPage":
        node["author"] = {"@id": SITE + "/about/#founder"}
        node["reviewedBy"] = {"@id": SITE + "/about/#founder"}
        node["lastReviewed"] = TODAY
    if p.get("about"):
        node["about"] = {"@type": "Thing", "name": p["about"]}
    graph.append(node)
    if True:
        graph.append({"@type": "Person", "@id": SITE + "/about/#founder", "name": AUTHOR["name"],
                      "jobTitle": AUTHOR["title"], "worksFor": {"@id": SITE + "/#org"},
                      "url": SITE + "/about/", "knowsAbout": AUTHOR["knows"]})
    graph.append({"@type": "Organization", "@id": SITE + "/#org", "name": "Super Routine",
                  "alternateName": ["SuperRoutine", "Super Routine Supplements", "Super Routine Daily Supplements", "superroutine.in"],
                  "url": SITE + "/", "logo": SITE + "/assets/logo-square.png",
                  "sameAs": ["https://www.instagram.com/super.routine/", "https://www.linkedin.com/company/super-routine/"]})
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in p["faq"]]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))

    byline = ""
    if p.get("byline", True):
        byline = (f'<p class="byline"><span>Written and reviewed by <a href="/about/">{esc(AUTHOR["name"])}</a>, '
                  f'{esc(AUTHOR["title"])}</span><span>Updated {datetime.date.today().strftime("%d %b %Y")}</span></p>')
    answer = f'<div class="answer"><p>{p["answer"]}</p></div>' if p.get("answer") else ""
    facts = ""
    if p.get("facts"):
        facts = '<div class="facts">' + "".join(
            f"<div><small>{esc(k)}</small><b>{esc(v)}</b></div>" for k, v in p["facts"]) + "</div>"
    faq = ""
    if p.get("faq"):
        faq = "<h2>FAQ</h2>" + "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in p["faq"])
    sources = ""
    if p.get("sources"):
        sources = '<h2>Sources</h2><ol class="sources">' + "".join(
            f'<li><a href="{esc(u)}" rel="nofollow noopener" target="_blank">{esc(t)}</a></li>' for t, u in p["sources"]) + "</ol>"
    disclaimer = ('<div class="note"><p><strong>Not medical advice.</strong> Super Routine is a food supplement, '
                  'not a medicine, and is not intended to diagnose, treat, cure or prevent any disease. Speak to your '
                  'doctor before use if you are pregnant, breastfeeding, under 18, have a medical condition or take '
                  'any medicine.</p></div>')
    join = ('<section class="join"><h2>Join the founding list</h2><p>Get first access and the founding price '
            'when Super Routine launches.</p><a href="/#join">Claim your spot →</a></section>')
    nav = "".join(f'<a href="{u}">{esc(t)}</a>' for t, u in NAV)
    foot = "".join(f'<a href="{u}">{esc(t)}</a>' for t, u in [("Home", "/")] + NAV[:3] + [("Science", "/science/")] + NAV[3:] + [("FAQ", "/faq/")])

    return f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["description"])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0B2654">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Super Routine">
<meta property="og:locale" content="en_IN">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(p["title"])}">
<meta property="og:description" content="{esc(p["description"])}">
<meta property="og:image" content="{SITE}/assets/pack-render.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site/pages.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header class="top"><div class="in"><a class="logo" href="/" aria-label="Super Routine home"><img src="/assets/site/logo.webp" alt="Super Routine" width="350" height="209"></a><nav aria-label="Main">{nav}<a class="cta" href="/#join">Join</a></nav></div></header>
<main>
<p class="crumbs">{crumb_html}</p>
<article>
<h1>{p["h1"]}</h1>
{byline}
{answer}
{facts}
{p["body"]}
{faq}
{disclaimer}
{sources}
</article>
{join}
</main>
<footer><div class="in"><nav aria-label="Footer">{foot}</nav><p>© 2026 Super Routine. Food supplements are not a substitute for a varied, balanced diet and a healthy lifestyle.</p></div></footer>
</body>
</html>
'''


def main():
    urls = [(SITE + "/", "1.0")]
    for p in PAGES:
        out = os.path.join(ROOT, p["path"].strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(page_html(p))
        urls.append((SITE + p["path"], p.get("priority", "0.8")))
        print("wrote", out)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in urls:
        sm.append(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm) + "\n")
    print("sitemap:", len(urls), "urls")


if __name__ == "__main__":
    main()
