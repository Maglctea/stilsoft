python manage.py migrate --no-input

python manage.py collectstatic --no-input
python manage.py create_superuser
gunicorn stilsoft.wsgi:application --bind 0.0.0.0:8000