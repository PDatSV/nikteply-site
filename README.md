# Nikolaus Teply Restorations

Static redesign of [nikteplyrestorations.com](https://nikteplyrestorations.com/) — original copy and workshop photographs, new layout and typography.

## Live demo

https://pdatsv.github.io/nikteply-site/

Published from the `main` branch with GitHub Pages.

## Preview locally

From this folder:

```bash
python -m http.server 8080
```

Then open [http://localhost:8080/](http://localhost:8080/).

Directory URLs such as `/about/` resolve to `about/index.html`. Use the local server rather than `file://`.

## Pages / routes

| Route | File |
|-------|------|
| `/` | `index.html` |
| `/about/` | `about/index.html` |
| `/contact/` | `contact/index.html` |
| `/gallery/` | `gallery/index.html` |
| `/testimonials/` | `testimonials/index.html` |
| `/services/` | `services/index.html` |
| `/services/antique-restoration/` | `services/antique-restoration/index.html` |
| `/services/antique-repairs/` | `services/antique-repairs/index.html` |
| `/services/antique-furniture-restoration/` | `services/antique-furniture-restoration/index.html` |
| `/services/refinishing-old-wood-furniture/` | `services/refinishing-old-wood-furniture/index.html` |
| `/services/veneer-furniture-restoration/` | `services/veneer-furniture-restoration/index.html` |
| `/services/french-polishing/` | `services/french-polishing/index.html` |
| `/services/woodturning/` | `services/woodturning/index.html` |
| `/services/furniture-colour-matching/` | `services/furniture-colour-matching/index.html` |
| `/404.html` | `404.html` |

## Stack

- Vanilla HTML pages
- Tailwind CSS via CDN plus `css/site.css`
- `js/site.js` — sticky header, mobile menu, services dropdown, before/after slider, gallery lightbox, contact form (mailto: nikteply@gmail.com)
- Original images in `public/images/`
- Content inventory in `CONTENT.md`

To regenerate HTML after editing `_generate.py`:

```bash
python _generate.py
```
