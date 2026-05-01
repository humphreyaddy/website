"""Build the static site.

Run:
    python3 build_site.py

What it does:
  - Reads blog posts from content/posts/*.md (Markdown subset, see md_to_html below).
  - Reads publications from content/publications.json.
  - Renders every page (index, about, research, publications, presentations,
    experience, skills, blog index, individual posts, contact, 404).
  - Writes feed.xml (RSS), sitemap.xml, robots.txt.

To add a blog post:
  1. Copy content/posts/_template.md to content/posts/YYYY-MM-DD-your-slug.md
  2. Fill in the frontmatter and write your post in Markdown.
  3. Run this script.

To add a publication:
  1. Open content/publications.json and add an entry to the JSON array.
  2. Run this script.

Pure stdlib — no pip install needed.
"""
from __future__ import annotations

import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
POSTS_OUT = ROOT / "posts"

SITE_URL = "https://humphreyaddy.github.io/website/"
NAME = "Humphrey P. K. Addy"
TAGLINE = ("Bioinformatician and biomedical scientist working on microbial genomics, "
           "antimicrobial resistance, and multi-omics data analysis in West Africa.")
BUILT_AT = datetime.now(timezone.utc).isoformat(timespec="seconds")

NAV = [
    ("index.html",         "Home"),
    ("about.html",         "About"),
    ("research.html",      "Research"),
    ("publications.html",  "Publications"),
    ("presentations.html", "Talks"),
    ("experience.html",    "Experience"),
    ("skills.html",        "Skills"),
    ("blog.html",          "Blog"),
    ("contact.html",       "Contact"),
]

SOCIALS = [
    ("https://orcid.org/0009-0000-3861-4671", "ORCID",
     "M0 0h24v24H0z M7.4 19.4h-2V7.7h2v11.7zM6.4 5.6a1.2 1.2 0 1 1 0-2.4 1.2 1.2 0 0 1 0 2.4zM10 7.7h4.6c4.4 0 6.3 3.1 6.3 5.9 0 3-2.4 5.9-6.3 5.9H10V7.7zm2 9.9h2.4c3.4 0 4.2-2.6 4.2-4.1 0-2.4-1.5-4-4.3-4H12v8.1z"),
    ("https://www.linkedin.com/in/humphreyaddy", "LinkedIn",
     "M20 3H4a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1zM8.3 18.3H5.7V9.7h2.6v8.6zM7 8.6a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm11.3 9.7h-2.6v-4.2c0-1 0-2.3-1.4-2.3s-1.6 1.1-1.6 2.2v4.3h-2.6V9.7h2.5v1.2h.1a2.7 2.7 0 0 1 2.5-1.4c2.6 0 3.1 1.7 3.1 4v4.8z"),
    ("https://github.com/humphreyaddy", "GitHub",
     "M12 1.5a10.5 10.5 0 0 0-3.3 20.4c.5.1.7-.2.7-.5v-2c-2.9.6-3.5-1.4-3.5-1.4-.5-1.2-1.2-1.5-1.2-1.5-1-.6.1-.6.1-.6 1 .1 1.6 1.1 1.6 1.1 1 1.6 2.5 1.2 3.1.9.1-.7.4-1.2.7-1.5-2.3-.3-4.7-1.2-4.7-5.1 0-1.1.4-2 1-2.8-.1-.3-.5-1.4.1-2.8 0 0 .9-.3 2.9 1.1a10 10 0 0 1 5.2 0c2-1.4 2.9-1.1 2.9-1.1.6 1.4.2 2.5.1 2.8.6.7 1 1.7 1 2.8 0 3.9-2.4 4.8-4.7 5.1.4.3.7.9.7 1.9V21.5c0 .3.2.6.7.5A10.5 10.5 0 0 0 12 1.5z"),
    ("https://x.com/humphrey_addy", "X (Twitter)",
     "M18.244 2H21l-6.55 7.49L22 22h-6.83l-4.78-6.27L4.8 22H2.04l7.02-8.02L2 2h6.99l4.32 5.71L18.244 2zm-2.4 18h1.59L7.27 4H5.6l10.244 16z"),
]

EMAIL = "addy.p.humphrey@gmail.com"
ORCID = "0009-0000-3861-4671"

EDUCATION = [
    ("2024 — Present", "AI-BOND",
     "African Initiative on Bioinformatics Online Training in Neurodegenerative Diseases. Online programme."),
    ("2024 — Present", "MPhil, Biodata Analytics &amp; Computational Genomics",
     "Kwame Nkrumah University of Science and Technology (KNUST), Kumasi, Ghana."),
    ("2017 — 2021",    "BSc, Biomedical Sciences",
     "University of Cape Coast, Cape Coast, Ghana."),
    ("2013 — 2016",    "WASSCE",
     "St. Mary&rsquo;s Seminary Senior High School, Lolobi, Ghana."),
]

AFFILIATIONS = [
    ("SeqbioUCC, University of Cape Coast",
     "Research Assistant &middot; Lead, Data Management &amp; Analytics"),
    ("Kwarteng Lab, KNUST", "Research Assistant"),
]

CURRENT_RESEARCH = [
    {"when": "2025 — Present",
     "title": "Microbial diversity of fermented food microbiomes across Ghana",
     "where": "Kwarteng Lab, KNUST",
     "role":  "Manuscript writing &middot; Bioinformatics analyst &middot; Data analysis",
     "status": "Ongoing"},
    {"when": "2024 — Present",
     "title": "Genomic analysis of multi-drug-resistant <em>Escherichia coli</em>",
     "where": "SeqbioUCC, University of Cape Coast",
     "role":  "Lead bioinformatics analyst &middot; Microbiology &middot; DNA extraction &middot; Bacterial WGS",
     "status": "Ongoing"},
]

PAST_RESEARCH = [
    {"when": "2023 — 2024",
     "title": "ESBL-producing <em>E. coli</em> from healthy pigs in Cape Coast",
     "where": "SeqbioUCC, University of Cape Coast",
     "role":  "Microbiology &middot; AMR phenotyping &middot; Genomic analysis",
     "status": "Completed"},
    {"when": "2022 — 2023",
     "title": "Genomic surveillance of <em>Klebsiella pneumoniae</em> from tertiary hospitals, Southern Ghana",
     "where": "SeqbioUCC, University of Cape Coast",
     "role":  "Bioinformatics analyst &middot; Co-author",
     "status": "Published"},
]

PRESENTATIONS = [
    ("2023", "Oral",
     "&ldquo;ESBL-producing <em>E. coli</em> from healthy pigs&rdquo;",
     "NMIMR Conference, Accra &middot; Nov 2023"),
    ("2023", "Poster",
     "&ldquo;Genomic AMR surveillance in <em>K. pneumoniae</em>&rdquo;",
     "COG-Train Hackathon &middot; Oct 2023"),
    ("2022", "Talk",
     "Cape Coast One-Health Symposium",
     "COHAS Day &middot; 2022"),
]

EXPERIENCE_CURRENT = [
    {"when": "2023 — Present",
     "title": "Lead, Data Management &amp; Analytics",
     "where": "SeqbioUCC, University of Cape Coast",
     "duties": [
         "Organising and maintaining sequenced-genome datasets across studies",
         "Defining data privacy and confidentiality protocols for the lab",
         "Onboarding students into reproducible bioinformatics workflows",
     ]},
    {"when": "2023 — Present",
     "title": "Research Assistant",
     "where": "SeqbioUCC, University of Cape Coast",
     "duties": [
         "Bacterial culture and identification",
         "DNA extraction and Oxford Nanopore MinION sequencing",
         "Genomic data analysis: assembly, AMR genes, comparative genomics",
     ]},
]

EXPERIENCE_PAST = [
    {"when": "2022 — 2023",
     "title": "Junior Research Assistant",
     "where": "SeqbioUCC, University of Cape Coast",
     "duties": [
         "Sample processing for AMR surveillance studies",
         "Phenotypic susceptibility testing",
     ]},
]

SKILLS = [
    ("Bioinformatics", [
        "Command-line scripting (Linux/Bash)",
        "Bacterial genomics: QC, assembly, annotation",
        "AMR gene detection: Abricate, CARD, ResFinder",
        "Comparative genomics &amp; pangenome analysis (Roary)",
        "Genomic surveillance: Pathogenwatch, Kleborate",
        "16S microbiome and metagenomics",
        "RNA-Seq and single-cell transcriptomics",
    ]),
    ("Data Science", [
        "R, Python, MATLAB",
        "Statistical analysis (SPSS, GraphPad Prism)",
        "Geospatial data analysis and mapping",
        "Machine learning workflows in R/Python",
        "Data visualisation (ggplot2, matplotlib, seaborn)",
        "Reproducible reporting (R Markdown, Quarto)",
    ]),
    ("Wet lab", [
        "Bacterial culture and identification",
        "DNA extraction and quantification",
        "Whole-genome sequencing on Oxford Nanopore MinION",
        "Phenotypic AMR testing",
    ]),
]


# =============================================================================
# Markdown subset → HTML
# =============================================================================

def _esc(s: str) -> str:
    return html.escape(s, quote=False)

INLINE_CODE = re.compile(r"`([^`]+)`")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
ITAL = re.compile(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
IMG = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def render_inline(text: str) -> str:
    """Render Markdown inline elements. Operates on already-escaped HTML."""
    out = text
    # placeholders to protect inline code from further substitution
    code_slots = []
    def take_code(m):
        code_slots.append(_esc(m.group(1)))
        return f"\x00CODE{len(code_slots)-1}\x00"
    out = INLINE_CODE.sub(take_code, out)
    out = _esc(out)

    out = IMG.sub(lambda m: f'<img src="{_esc(m.group(2))}" alt="{_esc(m.group(1))}" loading="lazy" />', out)
    out = LINK.sub(lambda m: f'<a href="{_esc(m.group(2))}">{_esc(m.group(1))}</a>', out)
    out = BOLD.sub(r"<strong>\1</strong>", out)
    out = ITAL.sub(r"<em>\1</em>", out)

    def back_code(m):
        return f"<code>{code_slots[int(m.group(1))]}</code>"
    out = re.sub(r"\x00CODE(\d+)\x00", back_code, out)
    return out


def md_to_html(text: str) -> str:
    """Tiny Markdown subset → HTML.

    Supports: headings (#..######), paragraphs, blockquotes, unordered lists
    (-/*), ordered lists (1.), fenced code (```...```), horizontal rules (---),
    inline: **bold**, *italic*, `code`, [links](url), ![imgs](url).
    """
    lines = text.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # blank
        if not line.strip():
            i += 1; continue

        # fenced code
        m = re.match(r"^```\s*([\w-]*)\s*$", line)
        if m:
            lang = m.group(1)
            i += 1
            code_lines: list[str] = []
            while i < n and not re.match(r"^```\s*$", lines[i]):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            cls = f' class="lang-{_esc(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>" + _esc("\n".join(code_lines)) + "</code></pre>")
            continue

        # horizontal rule
        if re.match(r"^-{3,}\s*$", line):
            out.append("<hr />"); i += 1; continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{render_inline(m.group(2))}</h{level}>")
            i += 1; continue

        # blockquote
        if line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            inner = md_to_html("\n".join(buf))
            out.append(f"<blockquote>{inner}</blockquote>")
            continue

        # unordered list
        if re.match(r"^[-*]\s+", line):
            items = []
            while i < n and re.match(r"^[-*]\s+", lines[i]):
                items.append(render_inline(re.sub(r"^[-*]\s+", "", lines[i])))
                i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>")
            continue

        # ordered list
        if re.match(r"^\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i]):
                items.append(render_inline(re.sub(r"^\d+\.\s+", "", lines[i])))
                i += 1
            out.append("<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>")
            continue

        # paragraph (consume until blank line or block element)
        para = [line]
        i += 1
        while i < n and lines[i].strip() and not (
            re.match(r"^(#{1,6})\s+", lines[i]) or
            lines[i].startswith(">") or
            re.match(r"^[-*]\s+", lines[i]) or
            re.match(r"^\d+\.\s+", lines[i]) or
            re.match(r"^```", lines[i]) or
            re.match(r"^-{3,}\s*$", lines[i])
        ):
            para.append(lines[i]); i += 1
        out.append("<p>" + render_inline(" ".join(para)) + "</p>")

    return "\n".join(out)


# =============================================================================
# Frontmatter
# =============================================================================

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.S)


def parse_post(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(raw)
    if not m:
        raise ValueError(f"{path.name}: missing --- frontmatter ---")
    fm_block, body = m.group(1), m.group(2)
    fm: dict = {}
    for line in fm_block.splitlines():
        if not line.strip(): continue
        if ":" not in line:
            raise ValueError(f"{path.name}: bad frontmatter line: {line!r}")
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
        else:
            v = v.strip('"').strip("'")
        fm[k.strip()] = v
    if "title" not in fm or "date" not in fm:
        raise ValueError(f"{path.name}: title and date are required in frontmatter")
    if isinstance(fm.get("tags"), str):
        fm["tags"] = [t.strip() for t in fm["tags"].split(",") if t.strip()]
    fm.setdefault("tags", [])
    fm.setdefault("summary", "")
    slug = path.stem
    if re.match(r"^\d{4}-\d{2}-\d{2}-", slug):
        slug = slug[11:]
    fm["slug"] = slug
    fm["body_md"] = body
    fm["body_html"] = md_to_html(body)
    fm["url"] = f"posts/{slug}.html"
    word_count = len(re.findall(r"\b\w+\b", re.sub(r"[`*\[\]()]", " ", body)))
    fm["read_min"] = max(1, round(word_count / 220))
    return fm


def load_posts() -> list[dict]:
    posts = []
    for p in sorted((CONTENT / "posts").glob("*.md")):
        if p.name.startswith("_"):
            continue
        posts.append(parse_post(p))
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts


def load_publications() -> list[dict]:
    pubs = json.loads((CONTENT / "publications.json").read_text(encoding="utf-8"))
    pubs.sort(key=lambda p: (-int(p["year"]), p["title"]))
    return pubs


# =============================================================================
# HTML chrome (head, header, footer)
# =============================================================================

def head(title, description, page_path, *, og_image=None, article=False):
    canon = SITE_URL + (page_path if page_path != "index.html" else "")
    image = og_image or (SITE_URL + "assets/img/og-cover.png")
    full_title = f"{NAME} — {title}" if title != NAME else NAME
    rel = "../" if page_path.startswith("posts/") else ""
    og_type = "article" if article else "website"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{full_title}</title>
  <meta name="description" content="{html.escape(description, quote=True)}" />
  <meta name="author" content="{NAME}" />
  <meta name="theme-color" content="#0a6b54" media="(prefers-color-scheme: light)" />
  <meta name="theme-color" content="#0e1216" media="(prefers-color-scheme: dark)" />
  <link rel="canonical" href="{canon}" />
  <link rel="icon" type="image/svg+xml" href="{rel}assets/favicon.svg" />
  <link rel="alternate" type="application/rss+xml" title="{NAME} — Blog" href="{rel}feed.xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&amp;family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@400;500&amp;display=swap" />
  <link rel="stylesheet" href="{rel}assets/css/main.css" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{html.escape(full_title, quote=True)}" />
  <meta property="og:description" content="{html.escape(description, quote=True)}" />
  <meta property="og:image" content="{image}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@humphrey_addy" />
  <meta name="twitter:title" content="{html.escape(full_title, quote=True)}" />
  <meta name="twitter:description" content="{html.escape(description, quote=True)}" />
  <meta name="twitter:image" content="{image}" />
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "{NAME}",
    "jobTitle": "Researcher in microbial genomics and bioinformatics",
    "url": "{SITE_URL}",
    "image": "{SITE_URL}assets/img/profile.jpg",
    "email": "{EMAIL}",
    "sameAs": [
      "https://github.com/humphreyaddy",
      "https://www.linkedin.com/in/humphreyaddy",
      "https://x.com/humphrey_addy",
      "https://orcid.org/{ORCID}"
    ],
    "affiliation": [
      {{ "@type": "EducationalOrganization", "name": "Kwame Nkrumah University of Science and Technology" }},
      {{ "@type": "EducationalOrganization", "name": "University of Cape Coast" }}
    ]
  }}
  </script>
  <script>
    (function() {{
      try {{
        var t = localStorage.getItem("hka-theme");
        if (t === "dark" || t === "light") document.documentElement.setAttribute("data-theme", t);
      }} catch (e) {{}}
    }})();
  </script>
</head>"""


def header(current):
    rel = "../" if current.startswith("posts/") else ""
    items = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items += f'      <li><a href="{rel}{href}"{cur}>{label}</a></li>\n'
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="{rel}index.html">
      <span class="mark">H</span>
      <span>Humphrey&nbsp;P.&nbsp;K.&nbsp;Addy</span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="primary-nav">Menu</button>
    <ul class="nav-links" id="primary-nav">
{items.rstrip()}
    </ul>
    <div class="nav-actions">
      <button class="theme-toggle" type="button" aria-label="Toggle colour theme">
        <svg class="icon-light" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4V2m0 20v-2m8-8h2M2 12h2m13.66 5.66 1.41 1.41M4.93 4.93l1.41 1.41m11.31 0 1.41-1.41M4.93 19.07l1.41-1.41M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>
        <svg class="icon-dark" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" fill="currentColor"/></svg>
      </button>
    </div>
  </div>
</header>"""


def footer(page_path):
    rel = "../" if page_path.startswith("posts/") else ""
    socials = ""
    for href, label, path in SOCIALS:
        socials += (
            f'<a href="{href}" rel="me noopener" target="_blank" aria-label="{label}">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{path}"/></svg></a>'
        )
    return f"""<button class="to-top" type="button" aria-label="Back to top">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4l8 8h-5v8h-6v-8H4z"/></svg>
</button>
<footer class="site-footer">
  <div class="wrap foot-row">
    <span>&copy; <span data-year>2026</span> {NAME}. All rights reserved.</span>
    <div class="meta-links">
      <a href="{rel}feed.xml">RSS</a>
      <a href="{rel}sitemap.xml">Sitemap</a>
    </div>
    <div class="socials">
      {socials}
    </div>
  </div>
</footer>
<script src="{rel}assets/js/main.js" defer></script>
</body>
</html>"""


def render(page_path, title, description, body, *, og_image=None, article=False):
    return (head(title, description, page_path, og_image=og_image, article=article)
            + "\n<body>\n" + header(page_path)
            + "\n<main id=\"main\">\n" + body + "\n</main>\n"
            + footer(page_path))


# =============================================================================
# small components
# =============================================================================

def _entry_html(e):
    return f"""<article class="entry reveal">
  <div class="when">{e['when']}</div>
  <div class="what">
    <h3>{e['title']}</h3>
    <p class="sub">{e['where']} &middot; {e['role']}</p>
    <p><strong>Status:</strong> {e['status']}</p>
  </div>
</article>"""

def _pub_html(p):
    role = f" &middot; Role: {p['role']}" if p.get("role") else ""
    return f"""<article class="pub">
  <p class="meta">{p['year']} &middot; {p['venue']}{role}</p>
  <p class="title">{p['title']}</p>
  <p class="authors">{p['authors']}</p>
  <p class="links">
    <a href="https://doi.org/{p['doi']}" target="_blank" rel="noopener">DOI: {p['doi']} &rarr;</a>
  </p>
</article>"""

def _exp_html(e):
    duties = ''.join(f"<li>{d}</li>" for d in e['duties'])
    return f"""<article class="entry reveal">
  <div class="when">{e['when']}</div>
  <div class="what">
    <h3>{e['title']}</h3>
    <p class="sub">{e['where']}</p>
    <ul>{duties}</ul>
  </div>
</article>"""

def _post_card_html(post):
    tag_html = "".join(f"<span>{html.escape(t)}</span>" for t in post["tags"])
    return f"""<a class="post-card reveal" href="{post['url']}">
  <div class="when"><time datetime="{post['date']}">{format_date(post['date'])}</time></div>
  <div>
    <h3>{html.escape(post['title'])}</h3>
    <p class="summary">{html.escape(post['summary'])}</p>
    <div class="meta-row">
      <span>{post['read_min']} min read</span>
      <span class="dot" style="width:4px;height:4px;background:var(--muted);border-radius:50%"></span>
      <div class="tags">{tag_html}</div>
    </div>
  </div>
</a>"""


def format_date(iso):
    try:
        d = datetime.fromisoformat(iso)
        return d.strftime("%-d %b %Y")
    except Exception:
        return iso


# =============================================================================
# pages
# =============================================================================

def page_index(posts, pubs):
    body = f"""<section class="wrap hero" aria-labelledby="hero-h">
  <div class="hero-text reveal">
    <p class="eyebrow">Researcher &middot; Bioinformatician &middot; Ghana</p>
    <h1 id="hero-h">{NAME}</h1>
    <p class="tagline">{TAGLINE}</p>
    <div class="cta-row">
      <a class="btn primary" href="research.html">See my research <span class="arrow">&rarr;</span></a>
      <a class="btn ghost" href="contact.html">Get in touch</a>
    </div>
  </div>
  <figure class="portrait reveal">
    <img src="assets/img/profile.jpg"
         srcset="assets/img/profile.jpg 1x, assets/img/profile@2x.jpg 2x"
         alt="Portrait of {NAME}" width="640" height="760" loading="eager" decoding="async" />
  </figure>
</section>

<section class="wrap section reveal" aria-label="Snapshot">
  <div class="stats">
    <div class="stat"><span class="num">{len(CURRENT_RESEARCH)+len(PAST_RESEARCH)}</span><span class="label">Research projects</span></div>
    <div class="stat"><span class="num">{len(pubs)}</span><span class="label">Publications</span></div>
    <div class="stat"><span class="num">{len(PRESENTATIONS)}</span><span class="label">Talks &amp; posters</span></div>
    <div class="stat"><span class="num">{len(posts)}</span><span class="label">Blog posts</span></div>
  </div>
</section>

<section class="wrap section" aria-labelledby="now-h">
  <div class="section-head reveal">
    <p class="eyebrow">What I&rsquo;m doing now</p>
    <h2 id="now-h">Active research</h2>
    <p class="lede">Two ongoing projects on microbial diversity and antimicrobial resistance.</p>
  </div>
  <div class="cards">
    <a class="card reveal" href="research.html">
      <span class="tag">Microbiome</span>
      <h3>Fermented food microbiomes across Ghana</h3>
      <p class="sub">Kwarteng Lab, KNUST &middot; 2025 — Present</p>
      <p>Mapping community structure and functional potential of indigenous fermented foods, with an eye on probiotic candidates.</p>
      <span class="more">Read more <span class="arrow">&rarr;</span></span>
    </a>
    <a class="card reveal" href="research.html">
      <span class="tag">AMR</span>
      <h3>Multi-drug-resistant <em>E. coli</em> genomics</h3>
      <p class="sub">SeqbioUCC, UCC &middot; 2024 — Present</p>
      <p>Whole-genome sequencing of clinical and environmental isolates to characterise resistance gene flow.</p>
      <span class="more">Read more <span class="arrow">&rarr;</span></span>
    </a>
  </div>
</section>"""

    if posts:
        body += f"""

<section class="wrap section" aria-labelledby="writing-h">
  <div class="section-head reveal">
    <p class="eyebrow">Writing</p>
    <h2 id="writing-h">Recent posts</h2>
    <p class="lede">Notes for students and early-career researchers. <a href="blog.html">All posts &rarr;</a></p>
  </div>
  <div class="post-list">
    {''.join(_post_card_html(p) for p in posts[:2])}
  </div>
</section>"""

    body += f"""

<section class="wrap section" aria-labelledby="pubs-h">
  <div class="section-head reveal">
    <p class="eyebrow">Selected work</p>
    <h2 id="pubs-h">Recent publications</h2>
    <p class="lede"><a href="publications.html">See all &rarr;</a></p>
  </div>
  <div class="pubs">
    {''.join(_pub_html(p) for p in pubs[:2])}
  </div>
</section>

<section class="wrap section reveal" aria-labelledby="contact-h">
  <div class="section-head">
    <p class="eyebrow">Open to</p>
    <h2 id="contact-h">Collaboration, mentorship, conversation</h2>
    <p class="lede">Reach out about microbiome / AMR research, bioinformatics teaching, or African genomic surveillance.</p>
  </div>
  <div class="cta-row">
    <a class="btn primary" href="mailto:{EMAIL}">Email me</a>
    <a class="btn ghost" href="contact.html">All ways to reach me</a>
  </div>
</section>"""
    return render("index.html", NAME, TAGLINE, body)


def page_about():
    edu_html = ''.join(
        f'<article class="entry reveal"><div class="when">{w}</div><div class="what"><h3>{t}</h3><p class="sub">{s}</p></div></article>'
        for (w, t, s) in EDUCATION
    )
    aff_html = ''.join(
        f'<article class="entry reveal"><div class="when">&nbsp;</div><div class="what"><h3>{n}</h3><p class="sub">{r}</p></div></article>'
        for (n, r) in AFFILIATIONS
    )
    body = f"""<section class="wrap page-head reveal">
  <p class="eyebrow">About</p>
  <h1>Hi, I&rsquo;m Humphrey.</h1>
  <p class="lede">I&rsquo;m a postgraduate researcher in microbial genomics and bioinformatics, training in Ghana and contributing to the small-but-growing African genomic-surveillance community. I work on antimicrobial resistance, fermented-food microbiomes, and reproducible analysis pipelines.</p>
</section>

<section class="wrap section" aria-labelledby="edu-h">
  <div class="section-head reveal">
    <p class="eyebrow">Education</p>
    <h2 id="edu-h">Where I trained</h2>
  </div>
  <div class="timeline">{edu_html}</div>
</section>

<section class="wrap section" aria-labelledby="aff-h">
  <div class="section-head reveal">
    <p class="eyebrow">Affiliations</p>
    <h2 id="aff-h">Labs &amp; groups</h2>
  </div>
  <div class="timeline">{aff_html}</div>
</section>"""
    return render("about.html", "About", "Bio, education, and affiliations of Humphrey P. K. Addy.", body)


def page_research():
    cur = ''.join(_entry_html(e) for e in CURRENT_RESEARCH)
    past = ''.join(_entry_html(e) for e in PAST_RESEARCH)
    body = f"""<section class="wrap page-head reveal">
  <p class="eyebrow">Research</p>
  <h1>Projects in the pipeline.</h1>
  <p class="lede">Microbial genomics and antimicrobial resistance, with an eye on West African settings.</p>
</section>

<section class="wrap section" aria-labelledby="cur-h">
  <div class="section-head reveal">
    <h2 id="cur-h">Current research</h2>
  </div>
  <div class="timeline">{cur}</div>
</section>

<section class="wrap section" aria-labelledby="past-h">
  <div class="section-head reveal">
    <h2 id="past-h">Completed research</h2>
  </div>
  <div class="timeline">{past}</div>
</section>"""
    return render("research.html", "Research", "Current and past research projects in microbial genomics and AMR.", body)


def page_publications(pubs):
    by_year: dict[int, list] = {}
    for p in pubs:
        by_year.setdefault(int(p["year"]), []).append(p)
    groups_html = ""
    for year in sorted(by_year, reverse=True):
        items = "".join(_pub_html(p) for p in by_year[year])
        groups_html += f'<section class="year-group reveal"><h2 class="year-label">{year}</h2><div class="pubs">{items}</div></section>'

    body = f"""<section class="wrap page-head reveal">
  <p class="eyebrow">Publications</p>
  <h1>Peer-reviewed work.</h1>
  <p class="lede">Articles I&rsquo;ve co-authored, with DOIs that take you to the canonical record.</p>
</section>

<section class="wrap section">
  {groups_html or '<p class="muted">No publications yet.</p>'}
</section>

<section class="wrap section" aria-labelledby="ur-h">
  <div class="section-head reveal">
    <h2 id="ur-h">Manuscripts under review</h2>
  </div>
  <p class="muted">Coming soon &mdash; check back as preprints land.</p>
</section>"""
    return render("publications.html", "Publications", "Peer-reviewed publications by Humphrey P. K. Addy.", body)


def page_presentations():
    rows = ''.join(
        f"""<article class="entry reveal"><div class="when">{w}</div><div class="what"><h3>{kind}: {what}</h3><p class="sub">{venue}</p></div></article>"""
        for (w, kind, what, venue) in PRESENTATIONS
    )
    body = f"""<section class="wrap page-head reveal">
  <p class="eyebrow">Talks</p>
  <h1>Conference presentations.</h1>
  <p class="lede">Oral talks, posters, and workshops I&rsquo;ve given.</p>
</section>

<section class="wrap section">
  <div class="timeline">{rows}</div>
</section>"""
    return render("presentations.html", "Presentations", "Oral and poster presentations by Humphrey P. K. Addy.", body)


def page_experience():
    cur = ''.join(_exp_html(e) for e in EXPERIENCE_CURRENT)
    past = ''.join(_exp_html(e) for e in EXPERIENCE_PAST)
    body = f"""<section class="wrap page-head reveal">
  <p class="eyebrow">Experience</p>
  <h1>Roles and responsibilities.</h1>
  <p class="lede">Research positions and lab leadership.</p>
</section>

<section class="wrap section" aria-labelledby="cur-h">
  <div class="section-head reveal">
    <h2 id="cur-h">Current positions</h2>
  </div>
  <div class="timeline">{cur}</div>
</section>

<section class="wrap section" aria-labelledby="past-h">
  <div class="section-head reveal">
    <h2 id="past-h">Previous positions</h2>
  </div>
  <div class="timeline">{past}</div>
</section>"""
    return render("experience.html", "Experience", "Research positions and lab leadership held by Humphrey P. K. Addy.", body)


def page_skills():
    blocks = ""
    for name, items in SKILLS:
        li = ''.join(f"<li>{x}</li>" for x in items)
        blocks += f'<div class="skill-block reveal"><h3>{name}</h3><ul>{li}</ul></div>'
    body = f"""<section class="wrap page-head reveal">
  <p class="eyebrow">Skills</p>
  <h1>Technical toolbox.</h1>
  <p class="lede">A working summary of the methods, tools, and languages I use day to day.</p>
</section>

<section class="wrap section">
  <div class="skill-grid">{blocks}</div>
</section>"""
    return render("skills.html", "Skills", "Bioinformatics, data science, and wet-lab skills.", body)


def page_blog(posts):
    if posts:
        items = "".join(_post_card_html(p) for p in posts)
        body = f"""<section class="wrap page-head reveal">
  <p class="eyebrow">Blog</p>
  <h1>Notes &amp; how-tos.</h1>
  <p class="lede">Sharing insights on genomics, microbial ecology, and data-driven biology &mdash; mostly written for students and early-career researchers. <a href="feed.xml">Subscribe via RSS</a>.</p>
</section>

<section class="wrap section">
  <div class="post-list">{items}</div>
</section>"""
    else:
        body = f"""<section class="wrap page-head"><p class="eyebrow">Blog</p><h1>Coming soon.</h1></section>"""
    return render("blog.html", "Blog", "Notes on genomics, microbial ecology, and data-driven biology.", body)


def page_post(post, prev_post, next_post):
    tags = "".join(f"<span>{html.escape(t)}</span>" for t in post["tags"])
    foot = ""
    if prev_post:
        foot += f'<a class="nav-prev" href="../{prev_post["url"]}"><span class="label">Older post</span><span>&larr; {html.escape(prev_post["title"])}</span></a>'
    else:
        foot += '<span></span>'
    if next_post:
        foot += f'<a class="nav-next" href="../{next_post["url"]}"><span class="label">Newer post</span><span>{html.escape(next_post["title"])} &rarr;</span></a>'

    body = f"""<article>
  <header class="wrap read article-head">
    <div class="meta">
      <time datetime="{post['date']}">{format_date(post['date'])}</time>
      <span class="dot"></span>
      <span>{post['read_min']} min read</span>
      <span class="dot"></span>
      <button class="copy-link" type="button" data-copy-link style="background:none;border:0;color:var(--accent);font-family:inherit;font-size:inherit;cursor:pointer;padding:0;font-weight:600">Copy link</button>
    </div>
    <h1>{html.escape(post['title'])}</h1>
    <p class="lede">{html.escape(post['summary'])}</p>
    <div class="tags">{tags}</div>
  </header>

  <div class="read article">
    {post['body_html']}
  </div>

  <footer class="wrap read article-foot">
    {foot}
  </footer>
</article>"""
    return render(post["url"], post["title"], post["summary"] or post["title"],
                  body, article=True)


def page_contact():
    body = f"""<section class="wrap page-head reveal">
  <p class="eyebrow">Contact</p>
  <h1>Let&rsquo;s talk.</h1>
  <p class="lede">Open to collaborations, mentorship, and conversation about microbiome / AMR research, bioinformatics teaching, or African genomic surveillance.</p>
</section>

<section class="wrap section">
  <div class="contact-grid">
    <article class="contact-card reveal">
      <h3>Direct</h3>
      <div class="row"><span class="k">Email</span><span class="v"><a href="mailto:{EMAIL}">{EMAIL}</a></span></div>
      <div class="row"><span class="k">ORCID</span><span class="v"><a href="https://orcid.org/{ORCID}" target="_blank" rel="noopener">{ORCID}</a></span></div>
      <div class="row"><span class="k">X / Twitter</span><span class="v"><a href="https://x.com/humphrey_addy" target="_blank" rel="noopener">@humphrey_addy</a></span></div>
      <div class="row"><span class="k">LinkedIn</span><span class="v"><a href="https://www.linkedin.com/in/humphreyaddy" target="_blank" rel="noopener">@humphreyaddy</a></span></div>
      <div class="row"><span class="k">GitHub</span><span class="v"><a href="https://github.com/humphreyaddy" target="_blank" rel="noopener">@humphreyaddy</a></span></div>
    </article>

    <article class="contact-card reveal">
      <h3>Affiliations</h3>
      <div class="row"><span class="k">KNUST</span><span class="v">Department of Biochemistry &amp; Biotechnology, Kumasi</span></div>
      <div class="row"><span class="k">UCC</span><span class="v">Department of Biomedical Sciences, Cape Coast</span></div>
    </article>
  </div>
</section>"""
    return render("contact.html", "Contact", f"Contact details for {NAME}: email, ORCID, social links, and affiliations.", body)


def page_404():
    body = f"""<section class="wrap center-404">
  <div>
    <h1>404</h1>
    <p class="lede">That page doesn&rsquo;t exist &mdash; or it moved.</p>
    <p style="margin-top:16px"><a class="btn primary" href="index.html">Back home</a></p>
  </div>
</section>"""
    return render("404.html", "Not found", "The page you requested could not be found.", body)


# =============================================================================
# feed / sitemap / robots
# =============================================================================

def write_feed(posts):
    items = []
    for p in posts:
        link = SITE_URL + p["url"]
        date_iso = p["date"]
        try:
            dt = datetime.fromisoformat(date_iso).strftime("%a, %d %b %Y 00:00:00 +0000")
        except Exception:
            dt = date_iso
        items.append(f"""    <item>
      <title>{html.escape(p['title'])}</title>
      <link>{link}</link>
      <guid isPermaLink="true">{link}</guid>
      <pubDate>{dt}</pubDate>
      <description>{html.escape(p['summary'])}</description>
    </item>""")
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{NAME} — Blog</title>
    <link>{SITE_URL}blog.html</link>
    <description>Notes on genomics, microbial ecology, and data-driven biology.</description>
    <language>en</language>
    <lastBuildDate>{BUILT_AT}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""
    (ROOT / "feed.xml").write_text(feed, encoding="utf-8")


def write_sitemap(posts):
    urls = [SITE_URL + p for p in [
        "", "about.html", "research.html", "publications.html",
        "presentations.html", "experience.html", "skills.html",
        "blog.html", "contact.html",
    ]]
    urls += [SITE_URL + p["url"] for p in posts]
    today = datetime.now().strftime("%Y-%m-%d")
    body = "\n".join(
        f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in urls
    )
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n',
        encoding="utf-8",
    )


def write_robots():
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n",
        encoding="utf-8",
    )


# =============================================================================
# driver
# =============================================================================

def main():
    posts = load_posts()
    pubs = load_publications()

    POSTS_OUT.mkdir(exist_ok=True)

    # main pages
    pages = {
        "index.html":         page_index(posts, pubs),
        "about.html":         page_about(),
        "research.html":      page_research(),
        "publications.html":  page_publications(pubs),
        "presentations.html": page_presentations(),
        "experience.html":    page_experience(),
        "skills.html":        page_skills(),
        "blog.html":          page_blog(posts),
        "contact.html":       page_contact(),
        "404.html":           page_404(),
    }
    for name, html_text in pages.items():
        (ROOT / name).write_text(html_text, encoding="utf-8")
        print(f"wrote {name} ({len(html_text):,} bytes)")

    # individual posts
    for i, post in enumerate(posts):
        prev_post = posts[i + 1] if i + 1 < len(posts) else None
        next_post = posts[i - 1] if i > 0 else None
        out = ROOT / "posts" / f"{post['slug']}.html"
        out.write_text(page_post(post, prev_post, next_post), encoding="utf-8")
        print(f"wrote posts/{post['slug']}.html ({out.stat().st_size:,} bytes)")

    # remove stale post files (in case a .md was deleted)
    valid = {f"{p['slug']}.html" for p in posts}
    for stale in (ROOT / "posts").glob("*.html"):
        if stale.name not in valid:
            print(f"removing stale {stale}")
            stale.unlink()

    write_feed(posts)
    write_sitemap(posts)
    write_robots()
    print("wrote feed.xml, sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
