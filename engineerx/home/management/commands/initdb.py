from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from posts.modules import fakedata as posts_fakedata
from authentication.modules import fakedata as auth_fakedata
from images.modules import fakedata as img_fakedata

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        auth_fakedata.create_users(50)
        auth_fakedata.create_users(50, is_moderator=True)
        auth_fakedata.create_users(50, is_editor=True)

        img_fakedata.create_wagtail_images()

        posts_fakedata.create_new_posts(50)
