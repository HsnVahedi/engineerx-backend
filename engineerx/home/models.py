from django.contrib.auth.models import AbstractUser
from django.db import models
from django.http import HttpResponse
from django.conf import settings

from wagtail.core.models import Page


class HomePage(Page):
    pass
    # def serve(self, request, *args, **kwargs):
    #     return HttpResponse(settings.DEBUG)
