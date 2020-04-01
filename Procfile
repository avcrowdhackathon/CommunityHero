release: python backend/manage.py migrate --noinput
release: python backend/manage.py loaddata db.json
web: gunicorn --chdir backend/ backend.wsgi