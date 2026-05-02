# Managing your website

Hi Humphrey — this is your everyday handbook for keeping <https://humphreyaddy.github.io/website/> up to date. Add a publication, write a blog post, drop conference photos, swap your bio. **No deep coding required.**

> **Your working folder is at `/Users/alex/Desktop/humphrey/website/`.**
> Every command in this guide assumes you `cd` there first.

---

## The 30-second flow (every update follows this)

```bash
# 1. open Terminal, go to your website folder
cd /Users/alex/Desktop/humphrey/website

# 2. pull the latest before you start (in case you edited from another machine)
git pull

# 3. make your change (edit a file, add a post, drop in photos, etc.)

# 4. rebuild the site
python3 build_site.py

# 5. preview locally (optional but recommended)
python3 -m http.server 8000
# open http://127.0.0.1:8000 in your browser; Ctrl+C to stop

# 6. commit and push
git add -A
git commit -m "short note about what you changed"
git push
```

GitHub Pages redeploys automatically — refresh the live site after about 30–60 seconds.

---

## Where things live

```
website/
├── content/                       ← THE FILES YOU EDIT MOST OFTEN
│   ├── posts/                     ← one Markdown file per blog post
│   │   ├── _template.md           ← copy this when starting a new post
│   │   └── 2025-08-10-…md         ← existing posts
│   ├── publications.json          ← all publications (one entry per paper)
│   └── conferences.json           ← all conferences attended
│
├── assets/img/conferences/        ← photo folders, one per conference slug
│   ├── nmimr-2023/                ← drop NMIMR photos here
│   ├── cog-train-2023/            ← drop COG-Train photos here
│   └── cohas-2022/                ← drop COHAS photos here
│
├── assets/img/profile.jpg         ← your portrait (640×760)
├── assets/img/profile@2x.jpg      ← retina version (1280×1519)
├── assets/img/og-cover.png        ← social-share image
│
├── build_site.py                  ← the renderer (also has Education/Skills lists)
├── assets/css/main.css            ← visual design (colours, fonts, spacing)
├── assets/js/main.js              ← interactivity (theme toggle, animations)
│
├── index.html, about.html, ...    ← GENERATED — never hand-edit, build_site.py rewrites these
├── posts/<slug>.html              ← generated post pages
└── feed.xml, sitemap.xml, robots.txt   ← generated
```

**Rule of thumb:** if a file ends in `.md` or `.json`, edit it. If it ends in `.html` at the top level, leave it alone — `build_site.py` will overwrite it.

---

## How do I…?

Each task below is a self-contained recipe. Copy-paste the commands.

### 1. Write a new blog post

```bash
cd /Users/alex/Desktop/humphrey/website

# copy the template (use today's date and a short slug separated by dashes)
cp content/posts/_template.md content/posts/2026-05-15-my-new-post.md

# open it in your editor (or use TextEdit, VS Code, whatever)
open content/posts/2026-05-15-my-new-post.md
```

The file starts with **frontmatter** (between the `---` lines). Fill it in:

```markdown
---
title: My new post
date: 2026-05-15
tags: [Bioinformatics, Tutorial]
summary: One sentence that shows on the blog index and in social previews.
---

Write your post in Markdown below.

## A heading

A paragraph. **Bold**, *italic*, and `inline code` work as expected.

- Bullet
- Another bullet

> A quote.

```python
print("hello")
```
```

> **Heads up about code blocks:** when you write three backticks in a `.md` file, end with another three backticks on a line by themselves.

Then build, commit, push:

```bash
python3 build_site.py
git add -A
git commit -m "post: my new post"
git push
```

Your post appears at `https://humphreyaddy.github.io/website/posts/my-new-post.html`, on the blog index, in the RSS feed, and in the sitemap — all automatically.

**Markdown supported**: headings (`#` … `######`), paragraphs, lists (`-` or `1.`), blockquotes (`>`), fenced code (` ``` `), horizontal rules (`---`), inline `code`, `**bold**`, `*italic*`, `[links](url)`, `![images](url)`.

### 2. Add a publication

Open `content/publications.json` and add a new entry to the top of the list:

```json
[
  {
    "year": 2026,
    "venue": "Nature Microbiology",
    "authors": "Addy, H.P.K. et al.",
    "title": "Pangenome analysis of Klebsiella pneumoniae across West Africa.",
    "doi": "10.1038/s41564-026-00000-0",
    "type": "Journal article",
    "role": "Lead author"
  },
  ... existing entries ...
]
```

The `type` and `role` fields are optional. The `doi` is what makes the "DOI →" link work, so include it whenever you can.

```bash
python3 build_site.py
git add -A && git commit -m "pub: Pangenome analysis K. pneumoniae" && git push
```

The new paper appears on `/publications.html` (grouped by year) and on the home page if it's one of the two most recent.

### 3. Add a brand-new conference

Open `content/conferences.json` and add an entry. Pick a short **slug** — this is the folder name where you'll drop photos:

```json
{
  "slug": "icabr-2026",
  "name": "ICABR — International Conference on Applied Bioinformatics Research",
  "year": 2026,
  "date": "Mar 2026",
  "location": "Nairobi, Kenya",
  "role": "Poster presenter",
  "description": "Poster: \"Pangenome analysis of Ghanaian K. pneumoniae\"."
}
```

Create the matching photo folder (use the same slug):

```bash
mkdir -p assets/img/conferences/icabr-2026
```

Drop photos in (see next recipe). Then:

```bash
python3 build_site.py
git add -A && git commit -m "conference: ICABR 2026" && git push
```

### 4. Add photos to a conference (existing or new)

Find the slug in `content/conferences.json` (e.g. `nmimr-2023`). Then:

```bash
cd /Users/alex/Desktop/humphrey/website

# copy or move photos into the conference folder
cp ~/Downloads/IMG_*.JPG assets/img/conferences/nmimr-2023/

# (optional) rename them so they sort in the order you want
# alphabetical sort wins, so prefix with 01_, 02_, etc.
mv assets/img/conferences/nmimr-2023/IMG_4523.JPG \
   assets/img/conferences/nmimr-2023/01_keynote.jpg
```

```bash
python3 build_site.py
git add -A && git commit -m "photos: NMIMR 2023" && git push
```

The conference page rebuilds with a right-to-left sliding gallery for that conference. Hovering pauses the slide.

**Photo guidelines** (important — keeps the site fast):
- 1000–1500 px wide
- Under 500 KB each
- JPG, PNG, WEBP, or AVIF

If your phone photos are 5+ MB each, resize them before adding. macOS Preview can do it: **File → Export…** with a smaller image dimension.

### 5. Update your bio / tagline

The big sentence on the home page lives in `build_site.py`. Open the file and look near the top for `TAGLINE`:

```python
TAGLINE = ("Bioinformatician and biomedical scientist working on microbial genomics, "
           "antimicrobial resistance, and multi-omics data analysis in West Africa.")
```

Edit the text inside the parentheses. Keep the leading and trailing quotes. Then:

```bash
python3 build_site.py
git add -A && git commit -m "update tagline" && git push
```

The longer bio paragraph lives in `build_site.py` inside `def page_about():` — search for `"Hi, I'm Humphrey."` and edit the `<p class="lede">…</p>` text right after it.

### 6. Replace your profile photo

```bash
cd /Users/alex/Desktop/humphrey/website

# put your new photo in (any size — script will resize)
cp ~/Pictures/new-portrait.jpg assets/img/_source.jpg

# resize to web sizes
python3 - <<'PY'
from PIL import Image, ImageOps
src = ImageOps.exif_transpose(Image.open("assets/img/_source.jpg")).convert("RGB")
for w, name in [(640, "profile.jpg"), (1280, "profile@2x.jpg")]:
    img = src.copy()
    img.thumbnail((w, w*2), Image.LANCZOS)
    img.save(f"assets/img/{name}", "JPEG", quality=82, optimize=True, progressive=True)
PY

rm assets/img/_source.jpg
git add -A && git commit -m "update profile photo" && git push
```

### 7. Add your CV (PDF)

```bash
cp ~/Documents/CV.pdf /Users/alex/Desktop/humphrey/website/CV.pdf
```

Then add a button to the home-page hero in `build_site.py`. Find this block inside `def page_index(...):`:

```python
    <div class="cta-row">
      <a class="btn primary" href="research.html">See my research <span class="arrow">&rarr;</span></a>
      <a class="btn ghost" href="contact.html">Get in touch</a>
    </div>
```

Add a third button:

```python
    <div class="cta-row">
      <a class="btn primary" href="research.html">See my research <span class="arrow">&rarr;</span></a>
      <a class="btn ghost" href="contact.html">Get in touch</a>
      <a class="btn ghost" href="CV.pdf" download>Download CV</a>
    </div>
```

```bash
python3 build_site.py && git add -A && git commit -m "cv: add CV download" && git push
```

### 8. Update Education / Experience / Skills / Affiliations

These lists live near the top of `build_site.py`. Search for the section name in the file:

| You want to edit         | Search inside `build_site.py` for     |
|--------------------------|---------------------------------------|
| Education                | `EDUCATION = [`                       |
| Affiliations             | `AFFILIATIONS = [`                    |
| Current research         | `CURRENT_RESEARCH = [`                |
| Past research            | `PAST_RESEARCH = [`                   |
| Current jobs / positions | `EXPERIENCE_CURRENT = [`              |
| Past jobs / positions    | `EXPERIENCE_PAST = [`                 |
| Skills (3 categories)    | `SKILLS = [`                          |

Each is a Python list. Add or remove entries by following the existing pattern — keep the punctuation (commas, brackets, quotes) consistent. Then build, commit, push.

> **Tip:** if Python complains after you edit one of these lists, you almost certainly missed a comma or a closing bracket. Compare your edit to the existing entries.

### 9. Update contact info

In `build_site.py`, search for these constants near the top:

```python
EMAIL = "addy.p.humphrey@gmail.com"
ORCID = "0009-0000-3861-4671"
```

Or for the full contact-page details, search for `def page_contact():` and edit the rows inside the `Direct` and `Affiliations` cards.

### 10. Tweak colours / fonts (lightly)

All design tokens are at the very top of `assets/css/main.css`:

```css
:root {
  --bg: #fbf7ee;        /* page background (cream) */
  --ink: #14171f;       /* main text */
  --accent: #0a6b54;    /* emerald — main brand colour */
  --accent-hot: #128a6e;/* hover state */
  ...
}
```

Change the values, save, run `python3 build_site.py` is **not needed for CSS** — but you do need to commit and push for the live site to pick it up. The dark-mode tokens live just below in `[data-theme="dark"] {…}`.

---

## Troubleshooting

### `No such file or directory` when running `python3 build_site.py`

You're in the wrong folder. Run:

```bash
cd /Users/alex/Desktop/humphrey/website
python3 build_site.py
```

Confirm you're in the right place with `pwd` (should print `/Users/alex/Desktop/humphrey/website`) and `ls build_site.py` (should print the filename, not "No such file").

### The build script crashed with a Python error

Read the last few lines of the error. The most common ones are:

- **`SyntaxError` or `JSONDecodeError`** — you missed a comma, bracket, or quote when editing `publications.json` or `conferences.json` or one of the lists in `build_site.py`. Compare your edit to the existing entries and fix the mismatch.
- **`ValueError: missing --- frontmatter ---`** — your blog post `.md` file doesn't have the `---` frontmatter block at the top. Make sure the very first line is `---` and the closing `---` comes before the post body.
- **`ValueError: title and date are required in frontmatter`** — add `title:` and `date:` lines inside the frontmatter block.

### Live site didn't update

GitHub Pages takes 30–60 seconds after a push. Check the **Actions** tab on the repo: <https://github.com/humphreyaddy/website/actions>. Once the latest run is green, hard-refresh your browser (`Cmd+Shift+R` on Mac).

If it's been more than 5 minutes and still wrong:

```bash
gh run list --repo humphreyaddy/website --limit 3
```

If a run failed, click into it on github.com to see why.

### A photo I added isn't showing

1. Confirm the file is in the right folder. The folder name must **exactly match** the `slug` from `conferences.json`.
2. Confirm the extension is one of: `.jpg`, `.jpeg`, `.png`, `.webp`, `.avif`. Other formats (e.g. `.heic`) are skipped.
3. Run `python3 build_site.py` again — the script picks up new photos at build time.
4. Make sure you committed both the photo file AND the regenerated `conferences.html`. `git status` will show what's pending.

### A photo is too big / page loads slowly

Anything over 500 KB will start to drag the site. Resize before committing:

```bash
# resize all photos in one folder to max 1400px wide, in place
cd /Users/alex/Desktop/humphrey/website
python3 - <<'PY'
from PIL import Image, ImageOps
import sys, glob, os
folder = "assets/img/conferences/nmimr-2023"   # ← change to your folder
for f in glob.glob(f"{folder}/*"):
    if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')): continue
    img = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    img.thumbnail((1400, 1400), Image.LANCZOS)
    img.save(f, "JPEG", quality=82, optimize=True)
    print(f, "->", os.path.getsize(f), "bytes")
PY
```

### I want to undo my last commit (before pushing)

```bash
git reset --soft HEAD~1   # keeps your changes, undoes the commit
```

### I pushed something I regret

```bash
git revert HEAD           # creates a new commit that reverses the last one
git push
```

(Don't use `git reset --hard` after pushing unless you really know what you're doing.)

---

## Reference: what each file does

| File / folder                     | Role                                                            |
|-----------------------------------|-----------------------------------------------------------------|
| `build_site.py`                   | The renderer. Reads content, writes HTML pages, RSS, sitemap.   |
| `content/posts/*.md`              | One Markdown file per blog post.                                |
| `content/publications.json`       | List of publications. Edit to add a paper.                      |
| `content/conferences.json`        | List of conferences. Edit to add a conference.                  |
| `assets/img/conferences/<slug>/`  | Photos for one conference. Drop files in.                       |
| `assets/img/profile*.jpg`         | Your portrait at 1× and 2× sizes.                               |
| `assets/img/og-cover.png`         | Social-share preview image.                                     |
| `assets/css/main.css`             | All visual styling (colours, fonts, layout, animations).        |
| `assets/js/main.js`               | Interactivity: theme toggle, scroll reveals, back-to-top.       |
| `index.html`, `about.html`, etc.  | Generated pages. Don't hand-edit. Re-run `build_site.py`.       |
| `posts/<slug>.html`               | Generated per-post pages.                                       |
| `feed.xml`                        | RSS feed of blog posts (generated).                             |
| `sitemap.xml`, `robots.txt`       | SEO files (generated).                                          |
| `.github/workflows/static.yml`    | The GitHub Actions workflow that deploys after every push.      |
| `LICENSE.txt`                     | MIT for code, all-rights-reserved for content.                  |
| `README.md`                       | Public-facing repo overview.                                    |
| `MANAGING.md` (this file)         | Your operations guide.                                          |

---

## Common Markdown bits, copy-paste ready

| You want         | Markdown                                           |
|------------------|----------------------------------------------------|
| Heading          | `## My heading`                                    |
| Bold             | `**important**`                                    |
| Italic           | `*emphasis*`                                       |
| Inline code      | `` `gene_name` ``                                  |
| Code block       | Three backticks, language, your code, three backticks |
| Link             | `[link text](https://example.com)`                 |
| Image            | `![what it is](path/to/image.jpg)`                 |
| Bullet list      | `- item` (one per line)                            |
| Numbered list    | `1. item`                                          |
| Quote            | `> a quote`                                        |
| Horizontal rule  | `---`                                              |

---

## What's automatic (you don't have to think about it)

- **SEO**: page titles, descriptions, canonical URLs, Open Graph + Twitter cards, JSON-LD Person schema — all generated for every page including individual blog posts.
- **RSS feed** at `/feed.xml` — updated every build.
- **Sitemap** at `/sitemap.xml` — every page including posts.
- **Reading time** on blog posts — calculated from word count.
- **Prev / next post navigation** — built from post dates.
- **Year-grouped publications** — driven by `year` in the JSON.
- **Stats on the home page** — research project / publication / conference / blog post counts.
- **Stale page cleanup** — if you remove a post `.md` or rename a section, the old HTML file gets deleted on the next build.
- **Light / dark theme** — toggle in the header, saved per-visitor.
- **Mobile menu, scroll-reveal animations, back-to-top button** — handled in `assets/js/main.js`.

---

## Cheat sheet

```bash
# wherever I am, get to my website folder
cd /Users/alex/Desktop/humphrey/website

# pull latest (especially if I edited from another machine)
git pull

# build the site after any content edit
python3 build_site.py

# preview locally
python3 -m http.server 8000   # then open http://127.0.0.1:8000

# what changed?
git status
git diff

# ship it
git add -A
git commit -m "what I changed"
git push

# is the deploy done?
gh run list --repo humphreyaddy/website --limit 3
```

That's the whole job. Anything else, message and I'll help.
