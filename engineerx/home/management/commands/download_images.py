from django.core.management.base import BaseCommand

from images.modules import download


class Command(BaseCommand):
    def handle(self, *args, **options):
        download.download_random_avatars(100)
        download.download_random_images(100)
