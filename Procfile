release: sh -c 'python manage.py makemigrations && python manage.py migrate'
web: gunicorn backend.wsgi