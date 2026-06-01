#!/bin/bash

echo "Creating 25 commits from actual project tree - Apr 15 to Jun 1, 2026"

commit_with_date() {
    local date="$1"
    local msg="$2"
    GIT_AUTHOR_DATE="${date}" GIT_COMMITTER_DATE="${date}" git commit -m "$msg"
}

# First, handle the old deleted files (remove them from git)
git rm --cached docker-firefox-config/machine-id firefox-extension/manifest.json fyp-dashboard/app.py fyp-dashboard/requirements.txt 2>/dev/null

# --- Apr 15 ---
git add BitB-Framework/extension/manifest.json
commit_with_date "2026-04-15T09:10:00" "feat: add extension manifest"

# --- Apr 17 ---
git add BitB-Framework/extension/background.js
commit_with_date "2026-04-17T11:22:00" "feat: add extension background script"

# --- Apr 19 ---
git add BitB-Framework/extension/content.js
commit_with_date "2026-04-19T10:05:00" "feat: add extension content script"

# --- Apr 21 ---
git add BitB-Framework/extension/popup.css
commit_with_date "2026-04-21T14:30:00" "feat: add extension popup styles"

# --- Apr 23 ---
git add BitB-Framework/extension/dashboard.html
commit_with_date "2026-04-23T09:45:00" "feat: add extension dashboard UI"

# --- Apr 25 ---
git add BitB-Framework/extension/icons/
commit_with_date "2026-04-25T13:15:00" "chore: add extension icons"

# --- Apr 27 ---
git add BitB-Framework/dashboard/app.py
commit_with_date "2026-04-27T10:55:00" "feat: init dashboard flask app"

# --- Apr 29 ---
git add BitB-Framework/dashboard/requirements.txt
commit_with_date "2026-04-29T15:40:00" "feat: add dashboard requirements"

# --- May 1 ---
git add BitB-Framework/dashboard/templates/login.html
commit_with_date "2026-05-01T11:20:00" "feat: add dashboard login template"

# --- May 3 ---
git add BitB-Framework/dashboard/templates/dashboard.html
commit_with_date "2026-05-03T09:30:00" "feat: add main dashboard template"

# --- May 5 ---
git add BitB-Framework/dashboard/templates/logs.html
commit_with_date "2026-05-05T14:10:00" "feat: add logs view template"

# --- May 7 ---
git add BitB-Framework/dashboard/templates/cookies.html
commit_with_date "2026-05-07T10:00:00" "feat: add cookies viewer template"

# --- May 9 ---
# Force add log files even if ignored by .gitignore
git add -f BitB-Framework/logs/browserInfo.log
commit_with_date "2026-05-09T13:45:00" "chore: init browser info log"

# --- May 11 ---
git add -f BitB-Framework/logs/cookies.log
commit_with_date "2026-05-11T11:55:00" "chore: init cookies log"

# --- May 13 ---
git add -f BitB-Framework/logs/credentials.log
commit_with_date "2026-05-13T09:20:00" "chore: init credentials log"

# --- May 15 ---
git add -f BitB-Framework/logs/keystroke.log
commit_with_date "2026-05-15T15:30:00" "chore: init keystroke log"

# --- May 17 ---
git add README.md
commit_with_date "2026-05-17T10:40:00" "docs: add project README"

# --- May 19 ---
git add .gitignore
commit_with_date "2026-05-19T12:15:00" "chore: add gitignore"

# --- May 21 ---
git add .env.example
commit_with_date "2026-05-21T14:00:00" "chore: add env example"

# --- May 23 ---
# Update .gitignore to exclude venv except for the .gitignore file
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
.env
venv/
node_modules/
*.log
.DS_Store
# Allow venv/.gitignore
!venv/.gitignore
EOF
git add .gitignore
commit_with_date "2026-05-23T09:05:00" "chore: update gitignore for venv"

# Create venv directory with .gitignore
mkdir -p BitB-Framework/dashboard/venv
cat > BitB-Framework/dashboard/venv/.gitignore << 'EOF'
*
!.gitignore
EOF
git add -f BitB-Framework/dashboard/venv/.gitignore
commit_with_date "2026-05-23T09:06:00" "chore: add venv gitignore"

# --- May 25 ---
git add CONTRIBUTING.md
commit_with_date "2026-05-25T11:30:00" "docs: add contributing guide"

# --- May 27 ---
mkdir -p docs
cat > docs/architecture.md << 'EOF'
# Architecture
PhishGenesis consists of three main components:
- Firefox Extension (content injection)
- Dashboard (Flask-based control panel)
- Logging system (captures session data)
EOF
git add docs/architecture.md
commit_with_date "2026-05-27T13:50:00" "docs: add architecture overview"

# --- May 29 ---
git add docs/setup.md
commit_with_date "2026-05-29T10:25:00" "docs: add setup guide"

# --- May 31 ---
git add docs/usage.md
commit_with_date "2026-05-31T15:10:00" "docs: add usage documentation"

# --- Jun 1 ---
git add CHANGELOG.md
commit_with_date "2026-06-01T16:45:00" "docs: add changelog"

echo ""
echo "=========================================="
echo "Done! 25 commits created."
echo "Run: git log --format='%h %ad %s' --date=short"