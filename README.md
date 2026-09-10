# McCreight Labs — Enterprise Website v11

A clean, production-oriented rebuild intended to look and behave like a mature technology-company website rather than a starter template.

## Major implementation areas
- Premium corporate home page and visual hierarchy
- Individual service pages
- Work / reference blueprint section
- Full original Insights articles
- Company, Solutions, Engineering, Platform, Technology, Industries, Engagements
- Security / Trust content
- Accessibility, Privacy, Cookies, Terms
- Contact intake flow with real endpoint support
- Thank-you state
- Search palette (`Ctrl/Cmd + K`)
- Dark/light theme
- Scroll progress and restrained reveal motion
- Reduced-motion support
- Accessible focus states and skip navigation
- SEO titles, descriptions, canonicals, Open Graph, Twitter cards
- Organization / Article structured data
- `sitemap.xml`, `robots.txt`, `humans.txt`
- Open Graph image
- Security header templates for Cloudflare/Netlify/Vercel
- GitHub Pages `.nojekyll`
- No service worker, avoiding stale-cache problems
- Critical visual system embedded in every HTML page

## Important: what still requires real company credentials
The frontend is prepared, but these cannot be truthfully invented:
- official custom domain
- verified business email
- real form endpoint
- analytics account / ID
- real client case studies and testimonials
- certifications or audited compliance claims
- active job openings

Edit `site-config.js` once you have the real contact endpoint or analytics ID.

## GitHub Pages
The canonical URL is currently configured for:
https://mccreight-de.github.io/mccreight-website/

If a custom domain is added later, update the site URL in the HTML metadata and sitemap using `configure-site.py`.
