web: python manage.py migrate && gunicorn amzfunnel.wsgi
worker: celery -A amzfunnel worker --loglevel=info
