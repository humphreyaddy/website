# humphreyaddy.github.io/website

Personal site for **Humphrey P. K. Addy** — bioinformatics researcher in Ghana.

Live: <https://humphreyaddy.github.io/website/>

## Day-to-day editing

You change the **content** files, run **one command**, then `git push`. That's it.

| What you want to change                | Edit                                              |
|----------------------------------------|---------------------------------------------------|
| Write a new blog post                  | New file in `content/posts/YYYY-MM-DD-slug.md`    |
| Add a publication                      | `content/publications.json`                       |
| Edit education / experience / skills   | `build_site.py` (top of file, plain Python lists) |
| Tweak colours, fonts, spacing          | `assets/css/main.css`                             |
| Edit interactivity (toggle, reveal…)   | `assets/js/main.js`                               |

Then build and deploy:

```bash
python3 build_site.py
git add -A
git commit -m "post: <short title>"
git push
```

GitHub Pages redeploys in ~30 seconds.

## Writing a blog post

1. Copy the template:
   ```bash
   cp content/posts/_template.md content/posts/2026-01-15-my-new-post.md
   ```
2. Edit the frontmatter (title, date, tags, summary) and write the post in Markdown.
3. Run `python3 build_site.py`.
4. Your post appears at `/posts/my-new-post.html`, on the blog index, in the RSS feed, and in the sitemap.

Markdown subset supported: headings (`#`..`######`), paragraphs, lists (`-`, `1.`),
blockquotes (`>`), fenced code (` ``` `), horizontal rules (`---`), inline `code`,
`**bold**`, `*italic*`, `[links](url)`, and `![images](url)`. Pure stdlib — no
extra Python packages required.

## Adding a publication

Open `content/publications.json` and prepend an entry:

```json
{
  "year": 2026,
  "venue": "Nature Microbiology",
  "authors": "Addy, H.P.K. et al.",
  "title": "Some great paper title.",
  "doi": "10.1038/...",
  "type": "Journal article",
  "role": "Lead author"
}
```

Run `python3 build_site.py`. The new entry appears on the publications page
(grouped by year) and on the home page (if it's one of the two most recent).

## Adding a CV

Drop `CV.pdf` at the repo root and add a button to the hero in `build_site.py`:

```python
'<a class="btn ghost" href="CV.pdf" download>Download CV <span class="arrow">↓</span></a>'
```

## What's in the site

**Pages**: home, about, research, publications (year-grouped), presentations,
experience, skills, blog index + per-post pages, contact, custom 404.

**Interactive features**:
- Theme toggle (light / dark / auto with localStorage)
- Reading-progress bar at the top of long pages
- Subtle scroll-reveal animations (respects `prefers-reduced-motion`)
- Back-to-top button
- "Copy link" button on blog posts
- Mobile slide-down navigation
- Print stylesheet — `/about` and any page prints clean for CV use

**SEO / discovery**:
- Per-page `<title>`, description, canonical URL
- Open Graph and Twitter card metadata + custom OG cover
- Person JSON-LD structured data
- `feed.xml` (RSS), `sitemap.xml`, `robots.txt`

## Layout

```
.
├── index.html, about.html, ...           ← rendered (do not hand-edit)
├── posts/<slug>.html                     ← rendered post pages
├── feed.xml, sitemap.xml, robots.txt     ← rendered
├── build_site.py                         ← single source: run after editing content
├── content/
│   ├── publications.json                 ← edit to add a paper
│   └── posts/
│       ├── _template.md                  ← template for new posts
│       └── YYYY-MM-DD-slug.md            ← one file per post
├── assets/
│   ├── css/main.css
│   ├── js/main.js
│   ├── favicon.svg
│   └── img/
│       ├── profile.jpg, profile@2x.jpg
│       └── og-cover.png
├── .github/workflows/static.yml          ← Pages deploy
├── LICENSE.txt
└── README.md
```

## License

- Code (HTML, CSS, JS, build script): MIT — see `LICENSE.txt`
- Site content (text, images, biography): © Humphrey P. K. Addy, all rights reserved.
