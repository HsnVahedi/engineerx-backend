from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings

from posts.modules import fakedata as posts_fakedata
from authentication.modules import fakedata as auth_fakedata
from images.modules import fakedata as img_fakedata

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        auth_fakedata.create_users(settings.INITDB_USERS_SIZE)
        auth_fakedata.create_users(settings.INITDB_MODERATORS_SIZE, is_moderator=True)
        auth_fakedata.create_users(settings.INITDB_EDITORS_SIZE, is_editor=True)

        img_fakedata.create_wagtail_images()

        posts_fakedata.create_new_posts(settings.INITDB_POSTS_SIZE)
