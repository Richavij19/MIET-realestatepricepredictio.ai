"""
realestatepricepredict.ai — Streamlit host wrapper.

The entire product lives in index.html (a self-contained single-page app).
This file does exactly one job: serve that HTML full-bleed inside Streamlit,
with no Streamlit chrome around it.

Run locally:   streamlit run streamlit_app.py
"""

from pathlib import Path

import streamlit as st

# --- config -----------------------------------------------------------------
HTML_FILE = Path(__file__).parent / "index.html"

# Height of the embedded frame in CSS pixels. The inner page scrolls on its own,
# so this is really "how tall the viewport of the app feels". 1100-1600 is sane.
FRAME_HEIGHT = 1400

st.set_page_config(
    page_title="realestatepricepredict.ai",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- strip Streamlit chrome so the page fills the window --------------------
st.markdown(
    """
    <style>
      /* kill the default padding/max-width so the app goes edge to edge */
      .block-container {
          padding: 0 !important;
          margin: 0 !important;
          max-width: 100% !important;
      }
      /* hide header, footer, toolbar, and the "Made with Streamlit" badge */
      header[data-testid="stHeader"] { display: none !important; }
      div[data-testid="stToolbar"]   { display: none !important; }
      div[data-testid="stDecoration"]{ display: none !important; }
      footer                          { display: none !important; }
      #MainMenu                       { visibility: hidden !important; }

      /* let the component iframe use the full width */
      iframe { width: 100% !important; border: none !important; }

      /* match the app's dark background so there is no white flash */
      .stApp, body { background: #181310 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- render -----------------------------------------------------------------
if not HTML_FILE.exists():
    st.error(
        f"Could not find {HTML_FILE.name}. It must sit next to streamlit_app.py "
        "in the repository root."
    )
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")

st.components.v1.html(html, height=FRAME_HEIGHT, scrolling=True)
