set -xe
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
touch do
gunicorn engineerx.wsgi:application