set -xe
mv downloads/ media/downloads/




python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn engineerx.wsgi:application
