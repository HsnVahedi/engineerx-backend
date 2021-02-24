import os
from random import random
from faker import Faker

from django.conf import settings

from common.modules import filesystem

fake = Faker()

filesystem.create_dir_if_not_exists(settings.MEDIA_ROOT)
filesystem.create_dir_if_not_exists(settings.DOWNLOADS_ROOT)
filesystem.create_dir_if_not_exists(settings.IMAGE_DOWNLOADS_DIR)
filesystem.create_dir_if_not_exists(settings.AVATAR_DOWNLOADS_DIR)


def download_random_image():
    width = int(random() * 1000) + 200
    height = int(random() * 1000) + 200
    image_url = f'{settings.RANDOM_IMAGE_URL}/{width}/{height}'
    filename = os.path.join(settings.IMAGE_DOWNLOADS_DIR, f'{fake.word()}.jpg')
    filesystem.download(image_url, filename)


def download_random_avatar():
    size = int(random() * 1000) + 200
    image_url = f'{settings.RANDOM_AVATAR_URL}/{size}'
    filename = os.path.join(settings.AVATAR_DOWNLOADS_DIR, f'{fake.word()}.jpg')
    filesystem.download(image_url, filename)


def download_random_images(size):
    i = 0
    while i < size:
        try:
            download_random_image()
            i += 1
        except:
            continue


def download_random_avatars(size):
    i = 0
    while i < size:
        try:
            download_random_avatar()
            i += 1
        except:
            continue
