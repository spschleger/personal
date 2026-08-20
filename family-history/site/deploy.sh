#!/bin/zsh
# Copies the latest dossier HTML into site/ and deploys to the Vercel team that hosts weekly-budget.
# Same Vercel team as weekly-budget (spsholdco-6680s-projects)
set -e
cd "$(dirname "$0")"
cp ../schleger/schleger-line.html schleger.html
cp ../jacklin/jacklin-line.html jacklin.html
# keep search engines out
for f in schleger.html jacklin.html; do
  grep -q 'name="robots"' "$f" || sed -i '' '1s/^/<meta name="robots" content="noindex,nofollow">\n/' "$f"
done
vercel deploy --prod --yes "$@"
