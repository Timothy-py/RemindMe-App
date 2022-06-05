web: gunicorn wsgi:app
worker: celery -A app.utility.mailer worker --loglevel=info