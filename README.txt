SUPER ROUTINE - PRE-LAUNCH WEBSITE
==================================
index.html  = the complete one-page site (images and styles are inside the file).
assets/     = logo (navy and white) and pack render, for reference or reuse.

To open: double-click index.html.
To publish: upload index.html to any static host (Netlify, Vercel, GitHub Pages, cPanel).

BEFORE GOING LIVE - edit the CONFIG block near the bottom of index.html (search for "SETTINGS"):
  FORM_ENDPOINT  paste your form URL (Google Apps Script, Formspree, Web3Forms).
                 Without it, form answers are NOT collected anywhere.
  MEMBER_COUNT   starting count shown in the hero (255); it goes up by 1 per claim on that device.
  COUNT_URL      optional URL returning {"count":N} so every visitor sees the same live total.
  CONTACT_EMAIL, PRIVACY_URL, TERMS_URL (Instagram, LinkedIn and WhatsApp links are already set)
                 profile and policy links (social icons point to # until set).

Fonts (Inter, Manrope) load from Google Fonts. Everything else works offline.
