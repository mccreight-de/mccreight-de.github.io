from pathlib import Path
import argparse, json, re

parser=argparse.ArgumentParser()
parser.add_argument("--site-url", required=True, help="Example: https://www.mccreightlabs.com/")
parser.add_argument("--contact-email", default="")
parser.add_argument("--contact-endpoint", default="")
parser.add_argument("--analytics-id", default="")
args=parser.parse_args()

url=args.site_url.rstrip("/")+"/"
root=Path(__file__).parent

# Replace current GitHub Pages URL in HTML + sitemap/robots/docs
old="https://mccreight-de.github.io/mccreight-website/"
for p in list(root.glob("*.html"))+[root/"sitemap.xml",root/"robots.txt",root/"README.md",root/"DEPLOYMENT.md"]:
    if p.exists():
        txt=p.read_text(encoding="utf-8").replace(old,url)
        p.write_text(txt,encoding="utf-8")

cfg={
  "siteUrl":url,
  "githubUrl":"https://github.com/mccreight-de/mccreight-labs",
  "contactEmail":args.contact_email,
  "contactEndpoint":args.contact_endpoint,
  "careersEndpoint":"",
  "analytics":{"provider":"ga4" if args.analytics_id else "none","id":args.analytics_id}
}
(root/"site-config.js").write_text("window.MCC_SITE = "+json.dumps(cfg,indent=2)+";\n",encoding="utf-8")
print("Site configuration updated.")
