from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings

from posts.modules import fakedata as posts_fakedata
from authentication.modules import fakedata as auth_fakedata
from images.modules import fakedata as img_fakedata
from accounts.modules import fakedata as accounts_fakedata
from posts.models import PostsPage
from accounts.models import PersonalPages
from home.models import HomePage
from posts.modules.initialize import create_posts_page
from accounts.modules.initialize import create_personal_accounts_page

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        auth_fakedata.create_users(settings.INITDB_USERS_SIZE)
        auth_fakedata.create_users(settings.INITDB_MODERATORS_SIZE, is_moderator=True)
        auth_fakedata.create_users(settings.INITDB_EDITORS_SIZE, is_editor=True)

        img_fakedata.create_wagtail_images()

        superuser = User.objects.filter(is_superuser=True).first()

        create_posts_page(owner=superuser)
        create_personal_accounts_page(owner=superuser)

        posts_fakedata.create_new_posts(settings.INITDB_POSTS_SIZE)

        accounts_fakedata.create_new_personal_pages()
