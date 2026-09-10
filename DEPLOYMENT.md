# Deployment — McCreight Labs v11

## Clean replacement on GitHub Pages
1. Delete the old website files from the repository.
2. Upload every file from this package directly to the repository root.
3. Confirm `index.html`, `.nojekyll`, `site-config.js`, `og-image.png`, and `sitemap.xml` are at the root.
4. In GitHub: Settings → Pages.
5. Deploy from branch `main` and `/ (root)`.
6. Wait for GitHub to publish.
7. Open https://mccreight-de.github.io/mccreight-website/ and hard refresh once.

## Contact form
Edit `site-config.js`:
- `contactEndpoint`: your verified form endpoint
- `contactEmail`: optional verified business email

The form already knows how to POST to an endpoint and redirect to `thank-you.html` after success.

## Analytics
`site-config.js` supports:
- provider: `ga4`
- id: your GA4 measurement ID

Analytics remain off until explicitly configured.

## Stronger production hosting
GitHub Pages is good for static hosting, but it does not support custom response headers.
For stronger CSP/HSTS/header control, deploy to Cloudflare Pages, Netlify, or Vercel. `_headers` and `vercel.json` are already included.
