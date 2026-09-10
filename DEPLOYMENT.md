# GitHub Pages — Clean Replacement

To replace all older versions:

1. In the repository, delete the old website HTML files.
2. Upload every file from this package directly to the repository root.
3. Confirm that `index.html` and `.nojekyll` are at the root.
4. In GitHub, open Settings → Pages.
5. Use branch `main` and folder `/ (root)`.
6. Save and wait for deployment.
7. Open the published site and perform a hard refresh once.

This version embeds its CSS and JavaScript in every HTML file, so missing asset folders cannot break the layout.
