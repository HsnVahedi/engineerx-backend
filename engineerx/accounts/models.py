from django.conf import settings
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable
from wagtail.core.models import Page
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.edit_handlers import ImageChooserPanel
from accounts.forms import PersonalPageForm
from wagtail.users.models import UserProfile


class PersonalPages(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['accounts.PersonalPage']

    content_panels = []
    promote_panels = []
    settings_panels = []


class PersonalPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def owner_info(self):
        image = None
        if UserProfile.objects.filter(user=self.owner).exists():
            if self.owner.wagtail_userprofile.avatar:
                image = self.owner.wagtail_userprofile.avatar.url
        return {
            'firstname': self.owner.first_name,
            'lastname': self.owner.last_name,
            'image': image,
        }

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        InlinePanel('related_accounts', label="Social Media Accounts"),
        InlinePanel('related_links', label="Links"),
        InlinePanel('related_fields', label="Fields"),
        InlinePanel('related_educations', label="Educations"),
        InlinePanel('related_experiences', label="Experiences"),
        InlinePanel('related_skills', label="Skills"),
    ]

    promote_panels = []
    settings_panels = []

    parent_page_types = ['accounts.PersonalPages']
    subpage_types = []

    api_fields = [
        APIField('owner_info'),
        APIField("related_accounts"),
        APIField('related_links'),
        APIField('related_fields'),
        APIField('related_educations'),
        APIField('related_experiences'),
        APIField('related_skills'),
        APIField('image', serializer=ImageRenditionField('min-1500x200')),
        APIField('image_16x9', serializer=ImageRenditionField('fill-1600x900-c70', source='image')),
    ]

    base_form_class = PersonalPageForm


class PersonalPageRelatedAccount(Orderable):
    GITHUB = 'Github'
    LINKEDIN = 'LinkedIn'
    INSTAGRAM = 'Instagram'
    FACEBOOK = 'Facebook'

    SOCIAL_MEDIA_CHOICES = [
        (GITHUB, GITHUB),
        (LINKEDIN, LINKEDIN),
        (INSTAGRAM, INSTAGRAM),
        (FACEBOOK, FACEBOOK),
    ]

    page = ParentalKey(
        PersonalPage,
        on_delete=models.CASCADE,
        related_name='related_accounts'
    )
    social_media = models.CharField(max_length=255, choices=SOCIAL_MEDIA_CHOICES)
    url = models.URLField()

    api_fields = [
        APIField("social_media"),
        APIField("url"),
    ]


class PersonalPageRelatedLink(Orderable):
    page = ParentalKey(
        PersonalPage,
        on_delete=models.CASCADE,
        related_name='related_links'
    )
    name = models.CharField(max_length=255)
    url = models.URLField()

    api_fields = [
        APIField("name"),
        APIField("url"),
    ]


class PersonalPageRelatedField(Orderable):
    page = ParentalKey(
        PersonalPage,
        on_delete=models.CASCADE,
        related_name='related_fields'
    )
    name = models.CharField(max_length=255)
    value = models.TextField()

    api_fields = [
        APIField("name"),
        APIField("value"),
    ]


class Education(Orderable):
    page = ParentalKey(
        PersonalPage,
        on_delete=models.CASCADE,
        related_name='related_educations'
    )
    degree = models.CharField(max_length=255, null=True, blank=True)
    institution = models.CharField(max_length=1000, null=True, blank=True)
    begin = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=1000, null=True, blank=True)

    api_fields = [
        APIField("degree"),
        APIField("institution"),
        APIField("begin"),
        APIField("end"),
        APIField("location"),
    ]


class Experience(Orderable):
    page = ParentalKey(
        PersonalPage,
        on_delete=models.CASCADE,
        related_name='related_experiences'
    )
    company = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    role = RichTextField(
        features=settings.DEFAULT_RICHTEXT_FEATURES, null=True, blank=True
    )
    begin = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    api_fields = [
        APIField("company"),
        APIField("location"),
        APIField('role'),
        APIField("begin"),
        APIField("end"),
        APIField("link"),
    ]


class Skill(Orderable):
    page = ParentalKey(
        PersonalPage,
        on_delete=models.CASCADE,
        related_name='related_skills'
    )
    name = models.CharField(max_length=255)
    description = RichTextField(
        features=settings.DEFAULT_RICHTEXT_FEATURES
    )

    api_fields = [
        APIField("name"),
        APIField("description"),
    ]
