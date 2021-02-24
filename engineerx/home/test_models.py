from random import random

from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.modules import fakedata as posts_fakedata
from authentication.modules import fakedata as auth_fakedata

User = get_user_model()


class PageTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.users = auth_fakedata.create_users(50)

