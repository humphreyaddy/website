"""Render all HTML pages from a single source.

Run:  python3 build_site.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE_URL = "https://humphreyaddy.github.io/website/"
NAME = "Humphrey P. K. Addy"
TAGLINE = "Bioinformatician and biomedical scientist working on microbial genomics, antimicrobial resistance, and multi-omics data analysis in West Africa."

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
    ("https://orcid.org/0009-0000-3861-4671", "ORCID",   "M0 0h24v24H0z M7.4 19.4h-2V7.7h2v11.7zM6.4 5.6a1.2 1.2 0 1 1 0-2.4 1.2 1.2 0 0 1 0 2.4zM10 7.7h4.6c4.4 0 6.3 3.1 6.3 5.9 0 3-2.4 5.9-6.3 5.9H10V7.7zm2 9.9h2.4c3.4 0 4.2-2.6 4.2-4.1 0-2.4-1.5-4-4.3-4H12v8.1z"),
    ("https://www.linkedin.com/in/humphreyaddy", "LinkedIn", "M20 3H4a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1zM8.3 18.3H5.7V9.7h2.6v8.6zM7 8.6a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm11.3 9.7h-2.6v-4.2c0-1 0-2.3-1.4-2.3s-1.6 1.1-1.6 2.2v4.3h-2.6V9.7h2.5v1.2h.1a2.7 2.7 0 0 1 2.5-1.4c2.6 0 3.1 1.7 3.1 4v4.8z"),
    ("https://github.com/humphreyaddy", "GitHub",   "M12 1.5a10.5 10.5 0 0 0-3.3 20.4c.5.1.7-.2.7-.5v-2c-2.9.6-3.5-1.4-3.5-1.4-.5-1.2-1.2-1.5-1.2-1.5-1-.6.1-.6.1-.6 1 .1 1.6 1.1 1.6 1.1 1 1.6 2.5 1.2 3.1.9.1-.7.4-1.2.7-1.5-2.3-.3-4.7-1.2-4.7-5.1 0-1.1.4-2 1-2.8-.1-.3-.5-1.4.1-2.8 0 0 .9-.3 2.9 1.1a10 10 0 0 1 5.2 0c2-1.4 2.9-1.1 2.9-1.1.6 1.4.2 2.5.1 2.8.6.7 1 1.7 1 2.8 0 3.9-2.4 4.8-4.7 5.1.4.3.7.9.7 1.9V21.5c0 .3.2.6.7.5A10.5 10.5 0 0 0 12 1.5z"),
    ("https://x.com/humphrey_addy", "X (Twitter)", "M18.244 2H21l-6.55 7.49L22 22h-6.83l-4.78-6.27L4.8 22H2.04l7.02-8.02L2 2h6.99l4.32 5.71L18.244 2zm-2.4 18h1.59L7.27 4H5.6l10.244 16z"),
]

EMAIL = "addy.p.humphrey@gmail.com"
ORCID = "0009-0000-3861-4671"

# ---------- content ----------
EDUCATION = [
    ("2024 — Present", "AI-BOND", "African Initiative on Bioinformatics Online Training in Neurodegenerative Diseases. Online programme."),
    ("2024 — Present", "MPhil, Biodata Analytics &amp; Computational Genomics", "Kwame Nkrumah University of Science and Technology (KNUST), Kumasi, Ghana."),
    ("2017 — 2021",    "BSc, Biomedical Sciences",                                "University of Cape Coast, Cape Coast, Ghana."),
    ("2013 — 2016",    "WASSCE",                                                  "St. Mary&rsquo;s Seminary Senior High School, Lolobi, Ghana."),
]

AFFILIATIONS = [
    ("SeqbioUCC, University of Cape Coast", "Research Assistant &middot; Lead, Data Management &amp; Analytics"),
    ("Kwarteng Lab, KNUST",                  "Research Assistant"),
]

CURRENT_RESEARCH = [
    {
        "when": "2025 — Present",
        "title": "Microbial diversity of fermented food microbiomes across Ghana",
        "where": "Kwarteng Lab, KNUST",
        "role":  "Manuscript writing &middot; Bioinformatics analyst &middot; Data analysis",
        "status": "Ongoing",
    },
    {
        "when": "2024 — Present",
        "title": "Genomic analysis of multi-drug-resistant <em>Escherichia coli</em>",
        "where": "SeqbioUCC, University of Cape Coast",
        "role":  "Lead bioinformatics analyst &middot; Microbiology &middot; DNA extraction &middot; Bacterial WGS",
        "status": "Ongoing",
    },
]

PAST_RESEARCH = [
    {
        "when": "2023 — 2024",
        "title": "ESBL-producing <em>E. coli</em> from healthy pigs in Cape Coast",
        "where": "SeqbioUCC, University of Cape Coast",
        "role":  "Microbiology &middot; AMR phenotyping &middot; Genomic analysis",
        "status": "Completed",
    },
    {
        "when": "2022 — 2023",
        "title": "Genomic surveillance of <em>Klebsiella pneumoniae</em> from tertiary hospitals, Southern Ghana",
        "where": "SeqbioUCC, University of Cape Coast",
        "role":  "Bioinformatics analyst &middot; Co-author",
        "status": "Published",
    },
]

PUBLICATIONS = [
    {
        "year": "2023",
        "venue": "Journal of Antimicrobial Chemotherapy",
        "authors": "Mills, R.O. <em>et al.</em>",
        "title":   "Genomic diversity and antimicrobial resistance in clinical <em>Klebsiella pneumoniae</em> isolates from tertiary hospitals in Southern Ghana.",
        "doi": "10.1093/jac/dkae123",
    },
    {
        "year": "2023",
        "venue": "Discover Public Health",
        "authors": "Boampong, D.S. <em>et al.</em>",
        "title":   "Knowledge, attitudes, and practices of antimicrobial use and resistance among nursing mothers in the Cape Coast Metropolis of Ghana: a cross-sectional study.",
        "doi": "10.1186/s12982-025-00564-z",
    },
]

PRESENTATIONS = [
    ("2023", "Oral",    "&ldquo;ESBL-producing <em>E. coli</em> from healthy pigs&rdquo;",       "NMIMR Conference, Accra &middot; Nov 2023"),
    ("2023", "Poster",  "&ldquo;Genomic AMR surveillance in <em>K. pneumoniae</em>&rdquo;",      "COG-Train Hackathon &middot; Oct 2023"),
    ("2022", "Talk",    "Cape Coast One-Health Symposium",                                       "COHAS Day &middot; 2022"),
]

EXPERIENCE_CURRENT = [
    {
        "when": "2023 — Present",
        "title": "Lead, Data Management &amp; Analytics",
        "where": "SeqbioUCC, University of Cape Coast",
        "duties": [
            "Organising and maintaining sequenced-genome datasets across studies",
            "Defining data privacy and confidentiality protocols for the lab",
            "Onboarding students into reproducible bioinformatics workflows",
        ],
    },
    {
        "when": "2023 — Present",
        "title": "Research Assistant",
        "where": "SeqbioUCC, University of Cape Coast",
        "duties": [
            "Bacterial culture and identification",
            "DNA extraction and Oxford Nanopore MinION sequencing",
            "Genomic data analysis: assembly, AMR genes, comparative genomics",
        ],
    },
]

EXPERIENCE_PAST = [
    {
        "when": "2022 — 2023",
        "title": "Junior Research Assistant",
        "where": "SeqbioUCC, University of Cape Coast",
        "duties": [
            "Sample processing for AMR surveillance studies",
            "Phenotypic susceptibility testing",
        ],
    },
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

BLOG_POSTS = [
    ("2025-08-10", "Microbiome visualisation in R",   "R, Visualisation",
     "Practical recipes for plotting microbiome data in R: stacked bars that don&rsquo;t lie, ordinations that read at a glance, and tidy taxa wrangling."),
    ("2025-07-29", "The importance of file naming in bioinformatics", "Workflow, Reproducibility",
     "File-naming conventions are critical for reproducibility and pipeline stability. Here&rsquo;s how I automated naming checks across a lab&rsquo;s shared drives."),
]


# ---------- HTML helpers ----------
def head(title, description, page_path):
    """Return <head> with shared metadata."""
    canon = SITE_URL + (page_path if page_path != "index.html" else "")
    og_image = SITE_URL + "assets/img/og-cover.png"
    full_title = f"{NAME} — {title}" if title != NAME else NAME
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{full_title}</title>
  <meta name="description" content="{description}" />
  <meta name="author" content="{NAME}" />
  <meta name="theme-color" content="#0a6b54" />
  <link rel="canonical" href="{canon}" />
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&amp;family=Inter:wght@400;500;600;700&amp;display=swap" />
  <link rel="stylesheet" href="assets/css/main.css" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{full_title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{og_image}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@humphrey_addy" />
  <meta name="twitter:title" content="{full_title}" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="{og_image}" />
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
</head>"""


def header(current):
    items = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items += f'      <li><a href="{href}"{cur}>{label}</a></li>\n'
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html">
      <span class="mark">H</span>
      <span>Humphrey&nbsp;P.&nbsp;K.&nbsp;Addy</span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="primary-nav">Menu</button>
    <ul class="nav-links" id="primary-nav">
{items.rstrip()}
    </ul>
  </div>
</header>"""


def footer():
    socials = ""
    for href, label, path in SOCIALS:
        socials += (
            f'<a href="{href}" rel="me noopener" target="_blank" aria-label="{label}">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{path}"/></svg></a>'
        )
    return f"""<footer class="site-footer">
  <div class="wrap foot-row">
    <span>&copy; <span data-year>2026</span> {NAME}. All rights reserved.</span>
    <div class="socials">
      {socials}
    </div>
  </div>
</footer>
<script src="assets/js/main.js" defer></script>
</body>
</html>"""


def render(page_path, title, description, body):
    return head(title, description, page_path) + "\n<body>\n" + header(page_path) + "\n<main id=\"main\">\n" + body + "\n</main>\n" + footer()


# ---------- pages ----------
def page_index():
    body = f"""<section class="wrap hero" aria-labelledby="hero-h">
  <div class="hero-text">
    <p class="eyebrow">Researcher &middot; Bioinformatician &middot; Ghana</p>
    <h1 id="hero-h">{NAME}</h1>
    <p class="tagline">{TAGLINE}</p>
    <div class="cta-row">
      <a class="btn primary" href="research.html">See my research</a>
      <a class="btn ghost" href="contact.html">Get in touch</a>
    </div>
  </div>
  <figure class="portrait">
    <img src="assets/img/profile.jpg"
         srcset="assets/img/profile.jpg 1x, assets/img/profile@2x.jpg 2x"
         alt="Portrait of {NAME}" width="640" height="760" loading="eager" decoding="async" />
  </figure>
</section>

<section class="wrap section" aria-labelledby="now-h">
  <div class="section-head">
    <p class="eyebrow">What I&rsquo;m doing now</p>
    <h2 id="now-h">Active research</h2>
    <p class="lede">Two ongoing projects on microbial diversity and antimicrobial resistance.</p>
  </div>
  <div class="cards">
    <article class="card">
      <span class="tag">Microbiome</span>
      <h3>Fermented food microbiomes across Ghana</h3>
      <p class="sub">Kwarteng Lab, KNUST &middot; 2025 — Present</p>
      <p>Mapping community structure and functional potential of indigenous fermented foods, with an eye on probiotic candidates.</p>
    </article>
    <article class="card">
      <span class="tag">AMR</span>
      <h3>Multi-drug-resistant <em>E. coli</em> genomics</h3>
      <p class="sub">SeqbioUCC, UCC &middot; 2024 — Present</p>
      <p>Whole-genome sequencing of clinical and environmental isolates to characterise resistance gene flow.</p>
    </article>
  </div>
</section>

<section class="wrap section" aria-labelledby="pubs-h">
  <div class="section-head">
    <p class="eyebrow">Selected work</p>
    <h2 id="pubs-h">Recent publications</h2>
    <p class="lede">Two of the studies I&rsquo;ve contributed to. <a href="publications.html">See all &rarr;</a></p>
  </div>
  <div class="pubs">
    {''.join(_pub_html(p) for p in PUBLICATIONS[:2])}
  </div>
</section>

<section class="wrap section" aria-labelledby="contact-h">
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


def _entry_html(e):
    return f"""<article class="entry">
  <div class="when">{e['when']}</div>
  <div class="what">
    <h3>{e['title']}</h3>
    <p class="sub">{e['where']} &middot; {e['role']}</p>
    <p><strong>Status:</strong> {e['status']}</p>
  </div>
</article>"""

def _pub_html(p):
    return f"""<article class="pub">
  <p class="meta">{p['year']} &middot; {p['venue']}</p>
  <p class="title">{p['title']}</p>
  <p class="authors">{p['authors']}</p>
  <p class="links">
    <a href="https://doi.org/{p['doi']}" target="_blank" rel="noopener">DOI: {p['doi']} &rarr;</a>
  </p>
</article>"""

def _exp_html(e):
    duties = ''.join(f"<li>{d}</li>" for d in e['duties'])
    return f"""<article class="entry">
  <div class="when">{e['when']}</div>
  <div class="what">
    <h3>{e['title']}</h3>
    <p class="sub">{e['where']}</p>
    <ul>{duties}</ul>
  </div>
</article>"""


def page_about():
    edu_html = ''.join(
        f'<article class="entry"><div class="when">{w}</div><div class="what"><h3>{t}</h3><p class="sub">{s}</p></div></article>'
        for (w, t, s) in EDUCATION
    )
    aff_html = ''.join(
        f'<article class="entry"><div class="when">&nbsp;</div><div class="what"><h3>{n}</h3><p class="sub">{r}</p></div></article>'
        for (n, r) in AFFILIATIONS
    )
    body = f"""<section class="wrap page-head">
  <p class="eyebrow">About</p>
  <h1>Hi, I&rsquo;m Humphrey.</h1>
  <p class="lede">I&rsquo;m a postgraduate researcher in microbial genomics and bioinformatics, training in Ghana and contributing to the small-but-growing African genomic-surveillance community. I work on antimicrobial resistance, fermented-food microbiomes, and reproducible analysis pipelines.</p>
</section>

<section class="wrap section" aria-labelledby="edu-h">
  <div class="section-head">
    <p class="eyebrow">Education</p>
    <h2 id="edu-h">Where I trained</h2>
  </div>
  <div class="timeline">{edu_html}</div>
</section>

<section class="wrap section" aria-labelledby="aff-h">
  <div class="section-head">
    <p class="eyebrow">Affiliations</p>
    <h2 id="aff-h">Labs &amp; groups</h2>
  </div>
  <div class="timeline">{aff_html}</div>
</section>"""
    return render("about.html", "About", "Bio, education, and affiliations of Humphrey P. K. Addy.", body)


def page_research():
    cur = ''.join(_entry_html(e) for e in CURRENT_RESEARCH)
    past = ''.join(_entry_html(e) for e in PAST_RESEARCH)
    body = f"""<section class="wrap page-head">
  <p class="eyebrow">Research</p>
  <h1>Projects in the pipeline.</h1>
  <p class="lede">Microbial genomics and antimicrobial resistance, with an eye on West African settings.</p>
</section>

<section class="wrap section" aria-labelledby="cur-h">
  <div class="section-head">
    <h2 id="cur-h">Current research</h2>
  </div>
  <div class="timeline">{cur}</div>
</section>

<section class="wrap section" aria-labelledby="past-h">
  <div class="section-head">
    <h2 id="past-h">Completed research</h2>
  </div>
  <div class="timeline">{past}</div>
</section>"""
    return render("research.html", "Research", "Current and past research projects in microbial genomics and AMR.", body)


def page_publications():
    pubs_html = ''.join(_pub_html(p) for p in PUBLICATIONS)
    body = f"""<section class="wrap page-head">
  <p class="eyebrow">Publications</p>
  <h1>Peer-reviewed work.</h1>
  <p class="lede">Articles I&rsquo;ve co-authored, with DOIs that take you to the canonical record. Manuscripts under review live below as I add them.</p>
</section>

<section class="wrap section" aria-labelledby="pub-h">
  <div class="section-head">
    <h2 id="pub-h">Published articles</h2>
  </div>
  <div class="pubs">{pubs_html}</div>
</section>

<section class="wrap section" aria-labelledby="ur-h">
  <div class="section-head">
    <h2 id="ur-h">Manuscripts under review</h2>
  </div>
  <p class="muted">Coming soon &mdash; check back as preprints land.</p>
</section>"""
    return render("publications.html", "Publications", "Peer-reviewed publications by Humphrey P. K. Addy.", body)


def page_presentations():
    rows = ''.join(
        f"""<article class="entry"><div class="when">{w}</div><div class="what"><h3>{kind}: {what}</h3><p class="sub">{venue}</p></div></article>"""
        for (w, kind, what, venue) in PRESENTATIONS
    )
    body = f"""<section class="wrap page-head">
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
    body = f"""<section class="wrap page-head">
  <p class="eyebrow">Experience</p>
  <h1>Roles and responsibilities.</h1>
  <p class="lede">Research positions and lab leadership.</p>
</section>

<section class="wrap section" aria-labelledby="cur-h">
  <div class="section-head">
    <h2 id="cur-h">Current positions</h2>
  </div>
  <div class="timeline">{cur}</div>
</section>

<section class="wrap section" aria-labelledby="past-h">
  <div class="section-head">
    <h2 id="past-h">Previous positions</h2>
  </div>
  <div class="timeline">{past}</div>
</section>"""
    return render("experience.html", "Experience", "Research positions and lab leadership held by Humphrey P. K. Addy.", body)


def page_skills():
    blocks = ""
    for name, items in SKILLS:
        li = ''.join(f"<li>{x}</li>" for x in items)
        blocks += f'<div class="skill-block"><h3>{name}</h3><ul>{li}</ul></div>'
    body = f"""<section class="wrap page-head">
  <p class="eyebrow">Skills</p>
  <h1>Technical toolbox.</h1>
  <p class="lede">A working summary of the methods, tools, and languages I use day to day.</p>
</section>

<section class="wrap section">
  <div class="skill-grid">{blocks}</div>
</section>"""
    return render("skills.html", "Skills", "Bioinformatics, data science, and wet-lab skills.", body)


def page_blog():
    posts = ''.join(
        f"""<article class="entry"><div class="when">{d}</div><div class="what"><h3>{t}</h3><p class="sub">Tags: {tags}</p><p>{summary}</p></div></article>"""
        for (d, t, tags, summary) in BLOG_POSTS
    )
    body = f"""<section class="wrap page-head">
  <p class="eyebrow">Blog</p>
  <h1>Notes &amp; how-tos.</h1>
  <p class="lede">Sharing insights on genomics, microbial ecology, and data-driven biology &mdash; mostly written for students and early-career researchers.</p>
</section>

<section class="wrap section">
  <div class="timeline">{posts}</div>
  <p class="muted" style="margin-top:24px">More posts coming. Drafts in progress on AMR pipelines, single-cell QC, and reproducible reporting in Quarto.</p>
</section>"""
    return render("blog.html", "Blog", "Notes on genomics, microbial ecology, and data-driven biology.", body)


def page_contact():
    body = f"""<section class="wrap page-head">
  <p class="eyebrow">Contact</p>
  <h1>Let&rsquo;s talk.</h1>
  <p class="lede">Open to collaborations, mentorship, and conversation about microbiome / AMR research, bioinformatics teaching, or African genomic surveillance.</p>
</section>

<section class="wrap section">
  <div class="contact-grid">
    <article class="contact-card">
      <h3>Direct</h3>
      <div class="row"><span class="k">Email</span><span class="v"><a href="mailto:{EMAIL}">{EMAIL}</a></span></div>
      <div class="row"><span class="k">ORCID</span><span class="v"><a href="https://orcid.org/{ORCID}" target="_blank" rel="noopener">{ORCID}</a></span></div>
      <div class="row"><span class="k">X / Twitter</span><span class="v"><a href="https://x.com/humphrey_addy" target="_blank" rel="noopener">@humphrey_addy</a></span></div>
      <div class="row"><span class="k">LinkedIn</span><span class="v"><a href="https://www.linkedin.com/in/humphreyaddy" target="_blank" rel="noopener">@humphreyaddy</a></span></div>
      <div class="row"><span class="k">GitHub</span><span class="v"><a href="https://github.com/humphreyaddy" target="_blank" rel="noopener">@humphreyaddy</a></span></div>
    </article>

    <article class="contact-card">
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


# ---------- driver ----------
PAGES = {
    "index.html":         page_index,
    "about.html":         page_about,
    "research.html":      page_research,
    "publications.html":  page_publications,
    "presentations.html": page_presentations,
    "experience.html":    page_experience,
    "skills.html":        page_skills,
    "blog.html":          page_blog,
    "contact.html":       page_contact,
    "404.html":           page_404,
}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        out = ROOT / name
        out.write_text(fn(), encoding="utf-8")
        print(f"wrote {name} ({out.stat().st_size:,} bytes)")
