# SUPER ROUTINE — PRE-LAUNCH WEBSITE

## Project Structure

- `index.html` — Complete one-page website, including styles, images, and the founding access questionnaire.
- `assets/` — Logo files, the hero video and product pack renders.
- `assets/site/` — Optimised WebP images used by `index.html`. Images are loaded from files, never embedded as base64 (Google only reads the first 2 MB of a page).
- `robots.txt`, `sitemap.xml`, `favicon.ico`, `apple-touch-icon.png` — SEO and browser files. Add every new page to `sitemap.xml`.
- `vercel.json` — Long cache headers for `/assets`.

## Run Locally

Open `index.html` in your browser to preview the website.

## Deploy the Website

Upload the project files to a static hosting provider such as **Vercel, Netlify, or GitHub Pages**.

For Vercel, import the GitHub repository and deploy it as a static website.

## Google Sheets Integration

The founding access questionnaire is configured to send submissions to a Google Apps Script Web App endpoint.

Responses are intended to be stored in Google Sheets, with the following columns:

1. Person name
2. Contact no
3. Each questionnaire response in its own column
4. Submission timestamp and relevant source metadata

**Google Sheets destination:**  
https://docs.google.com/spreadsheets/d/1MfYqSSiV5WDnqlEnwz54Qc3GsdC5dOtVHbrc_nbFDZk/edit

**Apps Script Web App endpoint:**  
https://script.google.com/macros/s/AKfycbyMRQyWq9Ju2evRYLQQa7RuwrSKNQ7B4rOBm8hAWiDkCXG5XeklnPxgoWKFIrxaHajveg/exec

### Before Going Live

- Confirm that the `FORM_ENDPOINT` setting in `index.html` contains the Apps Script Web App URL.
- Ensure the Apps Script is deployed with the required access permissions.
- Confirm that the script accepts the questionnaire's JSON payload and writes all response fields to the correct spreadsheet columns.
- Submit a test response and verify that it appears in the Google Sheet.

The integration must be tested before assuming that submissions are being recorded successfully.

## Configuration

Search for the `SETTINGS` or `CONFIG` block near the bottom of `index.html`.

- `FORM_ENDPOINT` — Google Apps Script Web App URL used to submit questionnaire responses.
- `MEMBER_COUNT` — Initial member count displayed in the hero section. The existing website uses `255` as its starting value.
- `COUNT_URL` — Optional endpoint returning `{"count":N}` to provide a shared count across visitors.
- `CONTACT_EMAIL` — Contact email address.
- `PRIVACY_URL` — Privacy policy URL.
- `TERMS_URL` — Terms and conditions URL.

The social profile links can also be configured if required.

## Design and Dependencies

- The website uses Inter and Manrope fonts loaded from Google Fonts.
- The existing design and questionnaire should remain unchanged unless a separate update is requested.
- Some features require an internet connection, including Google Fonts and the remote form endpoint.

## Important

Configuring the form endpoint does not, by itself, guarantee that submissions are saved. The Apps Script and spreadsheet integration must be tested successfully before launch.

## Content pages (tools/)
`python3 tools/build_pages.py` regenerates content pages and sitemap.xml. Pages hand-edited directly in HTML
(25-nutrient formula update, 29 Oct 2026) are stored in `tools/synced_pages.json` and take priority over
`tools/content.py`; rerun `python3 tools/sync_from_html.py` after any direct HTML edit to keep it in sync.
New articles: add to SCIENCE in content.py as before.
