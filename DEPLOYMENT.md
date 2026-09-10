# Deployment Guide

## GitHub Pages
1. Push the contents of this folder to the website repository.
2. Open repository Settings → Pages.
3. Deploy from the branch/folder that contains `index.html`.
4. Add the custom domain only after DNS is ready.
5. Replace `https://example.com/` in `sitemap.xml` and the structured-data block with the production domain.

## Other static hosts
The site is also compatible with Netlify, Cloudflare Pages, Vercel static hosting, and standard web servers.

## Production checks
- Confirm all links.
- Connect the contact form.
- Review privacy/terms.
- Confirm favicon and social-preview assets.
- Test mobile navigation, theme toggle, search palette, and service worker.
