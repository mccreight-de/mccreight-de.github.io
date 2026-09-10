# Security

McCreight Labs does not publish a security-reporting email until a verified monitored company address is available.

The public website intentionally avoids claiming certifications, audits, or compliance attestations that have not been verified.

## Website deployment
For hosts that support custom response headers, `_headers` and `vercel.json` provide a baseline for:
- HSTS
- nosniff
- referrer policy
- framing protection
- permissions policy
- a restrictive CSP baseline

GitHub Pages does not apply `_headers`; moving to Cloudflare Pages, Netlify, or Vercel enables stronger response-header control.
