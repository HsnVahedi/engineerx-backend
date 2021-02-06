import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.conf import settings

from authentication.modules import fakedata

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        fakedata.create_users(100)
