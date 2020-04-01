release: python manage.py migrate --noinput
web: gunicorn --chdir backend/ backend.wsgi