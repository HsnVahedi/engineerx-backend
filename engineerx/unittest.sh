set -xe
rm -r media/downloads/
mv downloads/ media/downloads/
python manage.py test authentication --noinput
