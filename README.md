# humphreyaddy.github.io/website

Personal site for **Humphrey P. K. Addy** — bioinformatics researcher in Ghana.

Live: <https://humphreyaddy.github.io/website/>

## Stack

- Plain static HTML / CSS / vanilla JS — no framework, no build step beyond a tiny
  Python script that DRYs up the shared header/footer
- Google Fonts: Fraunces (display serif) + Inter (body)
- Deployed via GitHub Actions (`.github/workflows/static.yml`) — every push to `main` redeploys

## Editing

All page content lives in `build_site.py` as plain Python data structures. To
change copy, edit the dict for the page (e.g. `EDUCATION`, `PUBLICATIONS`,
`SKILLS`), then regenerate every page:

```bash
python3 build_site.py
```

CSS is in `assets/css/main.css` (one file, ~12 KB). JS is in `assets/js/main.js`
(one file, mobile menu + footer year).

## Adding a publication

Open `build_site.py`, find the `PUBLICATIONS` list, prepend a new entry, then
run `python3 build_site.py`. The new pub appears on `publications.html` and (if
it is in the first two) on `index.html`.

## Adding a CV PDF

Drop `CV.pdf` at the repo root, then add a "Download CV" button to the hero in
`build_site.py`:

```python
'<a class="btn ghost" href="CV.pdf" download>Download CV</a>'
```

## Layout

```
.
├── index.html              ← rendered
├── about.html              ← rendered
├── research.html           ← rendered
├── publications.html       ← rendered
├── presentations.html      ← rendered
├── experience.html         ← rendered
├── skills.html             ← rendered
├── blog.html               ← rendered
├── contact.html            ← rendered
├── 404.html                ← rendered
├── build_site.py           ← single source of truth
├── assets/
│   ├── css/main.css
│   ├── js/main.js
│   ├── favicon.svg
│   └── img/
│       ├── profile.jpg     ← 640×760
│       ├── profile@2x.jpg  ← 1280×1519 (retina)
│       └── og-cover.png    ← 1200×630 social card
├── .github/workflows/
│   └── static.yml          ← Pages deploy
├── LICENSE.txt             ← MIT (code) · © Addy (content)
└── README.md
```

## License

- Code: MIT (see `LICENSE.txt`)
- Site content (text, images): © Humphrey P. K. Addy, all rights reserved.
