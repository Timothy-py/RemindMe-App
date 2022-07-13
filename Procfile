web: gunicorn wsgi:app
worker: celery -A app.utility.mailer worker --loglevel=info
flower: celery -A app.utility.mailer flower --port=5566