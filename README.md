# McCreight Labs Enterprise v6.1 — Fixed GitHub Pages Build

This build is intentionally designed to avoid missing CSS/JS/image problems on GitHub Pages.

## What changed
- CSS is embedded directly inside every HTML page.
- JavaScript is embedded directly inside every HTML page.
- Brand mark and architecture artwork are embedded as data URIs.
- No `assets/` folder is required for the site to render correctly.
- Service worker was removed to prevent stale-cache issues.
- `.nojekyll` is included for GitHub Pages.
- All pages remain linked with relative URLs.

## Upload to GitHub
Upload **all files inside this folder** directly to the repository root.
Do not upload the parent folder itself.

The repository root should show:
- `index.html`
- `company.html`
- `services.html`
- `solutions.html`
- `engineering.html`
- `platform.html`
- `case-studies.html`
- `insights.html`
- `careers.html`
- `security.html`
- `accessibility.html`
- `contact.html`
- `privacy.html`
- `terms.html`
- `404.html`
- `.nojekyll`

Then enable GitHub Pages from the branch root.
