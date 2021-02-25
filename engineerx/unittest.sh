set -xe
mv downloads/ media/downloads/
python manage.py test authentication --noinput