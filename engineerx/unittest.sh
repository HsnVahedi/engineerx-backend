set -xe
python manage.py download_images
python manage.py test authentication --noinput