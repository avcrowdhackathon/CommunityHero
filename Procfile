release: python backend/manage.py migrate --noinput
web: gunicorn --chdir backend/ backend.wsgi