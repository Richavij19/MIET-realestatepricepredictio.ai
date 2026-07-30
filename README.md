# realestatepricepredict.ai

A single-file web app for Jammu property price prediction and buy/no-buy scoring.
Marketing landing page plus a five-tab application (Buy, Explore, Compare, Model,
How It Works), with the dataset embedded directly in the page.

Everything runs client-side. No server, no database, no API keys required.

---

## Repository layout

```
.
├── index.html               # the entire app — unmodified, self-contained
├── streamlit_app.py         # thin wrapper that serves index.html inside Streamlit
├── requirements.txt         # streamlit
├── .streamlit/config.toml   # dark theme matching the app
└── .github/workflows/pages.yml   # auto-deploy to GitHub Pages on push to main
```

`index.html` is the single source of truth. The Streamlit wrapper only reads it —
it never modifies it. Edit the HTML and both deployments update.

---

## 1. Push to GitHub

```bash
cd realestatepricepredict-ai

git init
git add .
git commit -m "Initial commit: realestatepricepredict.ai"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/realestatepricepredict-ai.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. Create the empty repository on
github.com first (no README, no .gitignore — this repo already has them).

---

## 2. Host on GitHub Pages (recommended for the public site)

This is the better host for this project: it is a static page, so Pages serves it
instantly with no cold starts and no resource limits.

**Option A — automatic (workflow included)**

1. Go to your repo → **Settings** → **Pages**
2. Under **Source**, choose **GitHub Actions**
3. Push to `main`. The included workflow deploys automatically.

**Option B — no workflow needed**

1. Go to **Settings** → **Pages**
2. Under **Source**, choose **Deploy from a branch**
3. Branch: `main`, folder: `/ (root)` → **Save**

Either way your site appears at:

```
https://YOUR_USERNAME.github.io/realestatepricepredict-ai/
```

First deploy takes 1–2 minutes.

### Custom domain

If you own `realestatepricepredict.ai`, add a file named `CNAME` at the repo root
containing just the domain, then point these DNS records at GitHub:

| Type  | Name  | Value                                             |
| ----- | ----- | ------------------------------------------------- |
| A     | `@`   | `185.199.108.153` (and `.109.153`, `.110.153`, `.111.153`) |
| CNAME | `www` | `YOUR_USERNAME.github.io`                         |

Then tick **Enforce HTTPS** in Settings → Pages.

---

## 3. Host on Streamlit Community Cloud

1. Go to **share.streamlit.io** and sign in with GitHub
2. Click **New app** → **Deploy a public app from GitHub**
3. Fill in:
   - Repository: `YOUR_USERNAME/realestatepricepredict-ai`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
4. Click **Deploy**

You get `https://YOUR_APP_NAME.streamlit.app`.

### Running it locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Opens at http://localhost:8501.

### Tuning the frame height

Streamlit renders the page inside a fixed-height iframe. If the app feels cramped
or leaves dead space, change one line near the top of `streamlit_app.py`:

```python
FRAME_HEIGHT = 1400   # try 1000–1800
```

The inner page scrolls on its own, so this controls how tall the app's viewport
feels rather than clipping content.

---

## Which host should you use?

| | GitHub Pages | Streamlit Cloud |
| --- | --- | --- |
| Cold starts | None | App sleeps after inactivity |
| Layout | True full-screen | Inside an iframe |
| Browser geolocation | Works | May be blocked by the iframe sandbox |
| Cost | Free | Free |
| Custom domain | Yes | No (on the free tier) |

**Use GitHub Pages as the real site.** Use Streamlit if you need it inside a
Streamlit portfolio, or as a stepping stone to adding real Python model inference
later — at that point you would move prediction out of the JavaScript and into
`streamlit_app.py`.

---

## Notes on the app itself

- The dataset lives in `index.html` inside `<script type="text/plain" id="raw-csv">`
  and is parsed at runtime by PapaParse. To update the data, replace that block.
- Third-party libraries load from cdnjs: Leaflet 1.9.4 (maps), Chart.js 4.4.1
  (charts), PapaParse 5.4.1 (CSV). An internet connection is required on first load.
- The Google Maps key field in the Buy tab is optional. Leaflet with OpenStreetMap
  tiles is the default and needs no key.
- Never commit a real Google Maps API key to a public repo. Keys entered in that
  field stay in the browser and are not stored in this repository.
