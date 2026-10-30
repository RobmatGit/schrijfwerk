#!/bin/bash
# Zet alle wijzigingen in Schrijfwerk op GitHub. Draait elk uur vanzelf (zie setup-github.sh).
cd "$(dirname "$0")/.." || exit 1
git add -A
if ! git diff --cached --quiet; then
  git commit -q -m "bewaard $(date '+%Y-%m-%d %H:%M')"
fi
git pull -q --rebase origin main && git push -q origin main
