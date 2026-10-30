#!/bin/bash
# Eenmalig, in Terminal op de Mac:  bash "~/Claude Cowork/Schrijfwerk/tools/setup-github.sh"
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

# 1. Lokale git
if [ ! -d .git ]; then
  git init -q -b main
  git add -A
  git commit -q -m "Schrijfwerk: eerste opzet"
  echo "Git staat klaar."
fi

# 2. Privé repo op GitHub
if ! git remote get-url origin >/dev/null 2>&1; then
  if command -v gh >/dev/null && gh auth status >/dev/null 2>&1; then
    gh repo create schrijfwerk --private --source . --remote origin --push
  else
    echo
    echo "Maak op github.com/new een LEGE privé repository met de naam: schrijfwerk"
    echo "(geen README, geen .gitignore aanvinken). Plak daarna hier de URL:"
    read -r URL
    git remote add origin "$URL"
    git push -u origin main
  fi
fi

# 3. Elk uur automatisch bewaren
PLIST="$HOME/Library/LaunchAgents/nl.binnenbeheer.schrijfwerk.plist"
mkdir -p "$HOME/Library/LaunchAgents" "$HOME/Library/Logs"
cat > "$PLIST" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>nl.binnenbeheer.schrijfwerk</string>
  <key>ProgramArguments</key><array><string>/bin/bash</string><string>$REPO/tools/bewaar.sh</string></array>
  <key>StartInterval</key><integer>3600</integer>
  <key>RunAtLoad</key><true/>
  <key>StandardOutPath</key><string>$HOME/Library/Logs/schrijfwerk.log</string>
  <key>StandardErrorPath</key><string>$HOME/Library/Logs/schrijfwerk.log</string>
</dict></plist>
PL
launchctl unload "$PLIST" 2>/dev/null || true
launchctl load "$PLIST"
echo
echo "Klaar. Schrijfwerk gaat elk uur vanzelf naar GitHub. Log: ~/Library/Logs/schrijfwerk.log"
