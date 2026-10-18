# Campus Resource Management System — Web Version

A Flask web application for managing campus resources and fellows. Planned features include resource inventory, fellow registration, borrowing and returns, search, and reporting.

**Current status:** Initial Flask homepage built with Jinja templates and CSS. Database-backed management features are planned and not yet implemented.

## Technology stack

- Python and Flask
- Jinja templates, HTML, and CSS
- Flask-SQLAlchemy and SQLite (database integration planned)
- python-dotenv (configuration support)

## Requirements

Python 3, Git, and an internet connection to install Python packages.

## Set up from GitHub (new laptop or wiped workspace)

Run these commands in a terminal:

```bash
git clone https://github.com/AlphonsusOrtse-dev/campus_resource_system_web_version.git
cd campus_resource_system_web_version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
```

Open **http://127.0.0.1:5000** in your browser.

- `python3 -m venv .venv` creates a virtual environment.
- `source .venv/bin/activate` activates it on Linux.
- `python -m pip install -r requirements.txt` installs the project dependencies.
- `python run.py` starts Flask's local development server. Stop it with **Ctrl+C**.

**If the project folder already exists**, do not clone again. Open it with `cd campus_resource_system_web_version`, activate the existing environment with `source .venv/bin/activate`, and run `python run.py`. If `.venv` was deleted, recreate it and reinstall dependencies using the commands above.

## Quick checks

With the server running, visit **http://127.0.0.1:5000** to check the homepage. You can also run:

```bash
curl -I http://127.0.0.1:5000/
curl -I http://127.0.0.1:5000/static/css/style.css
```

Both should return an HTTP 200 response when the app and stylesheet are available.

## Project structure

```text
app/
  __init__.py           # Flask application factory
  routes.py             # HTTP routes
  templates/
    base.html           # Shared page layout
    home.html           # Homepage
  static/css/
    style.css           # Styling
run.py                  # Development entry point
requirements.txt        # Python dependencies
.gitignore              # Excluded local files
README.md               # Project documentation
```

## Save progress before leaving

Review changes before committing:

```bash
git status
git add README.md
git commit -m "docs: add project setup and recovery instructions"
git push origin main
```

For future code changes, stage the relevant files rather than only `README.md`. **Only committed and pushed changes are recoverable from GitHub.** The `.venv` folder is intentionally not committed; recreate it after a wipe. Local SQLite data and secrets are not automatically backed up by Git.

> This app currently runs with Flask's development server. Do not expose the debugger publicly or use the development server in production.
