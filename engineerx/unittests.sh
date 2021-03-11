set -xe
python manage.py test authentication --noinput
python manage.py test home --noinput
