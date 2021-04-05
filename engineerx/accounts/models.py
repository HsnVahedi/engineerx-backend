from accounts.forms import PersonalPageForm
from django.conf import settings
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import InlinePanel
from wagtail.api import APIField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable
from wagtail.core.models import Page
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.users.models import UserProfile
from django.shortcuts import redirect


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
            'id': self.owner.id,
        }

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        InlinePanel('related_accounts', label="Social Media Accounts"),
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
        APIField('owner'),
        APIField("related_accounts"),
        APIField('related_educations'),
        APIField('related_experiences'),
        APIField('related_skills'),
        APIField('image', serializer=ImageRenditionField('min-1500x200')),
        APIField('image_16x9', serializer=ImageRenditionField('fill-1600x900-c70', source='image')),
    ]

    base_form_class = PersonalPageForm

    def save(self, *args, **kwargs):
        self.slug = f'{self.owner.id}';
        return super().save(*args, **kwargs)

    def serve(self, request, *args, **kwargs):
        return redirect(f'{settings.FRONTEND_URL}/specialists/{self.slug}')

    def get_url_parts(self, *args, **kwargs):
        url_parts = super().get_url_parts(*args, **kwargs)

        # if url_parts is None:
        #     # in this case, the page doesn't have a well-defined URL in the first place -
        #     # for example, it's been created at the top level of the page tree
        #     # and hasn't been associated with a site record
        #     return None
        if settings.PRODUCTION:
            site_id, root_url, page_path = url_parts
            return site_id, root_url, f'/specialists/{self.slug}'
        else:
            return url_parts


class PersonalPageRelatedAccount(Orderable):
    GITHUB = 'Github'
    LINKEDIN = 'LinkedIn'
    INSTAGRAM = 'Instagram'
    FACEBOOK = 'Facebook'

    SOCIAL_NETWORKS = [
        GITHUB, LINKEDIN, INSTAGRAM, FACEBOOK
    ]

    SOCIAL_MEDIA_CHOICES = [
        (x, x) for x in SOCIAL_NETWORKS
    ]

    # SOCIAL_MEDIA_CHOICES = [
    #     (GITHUB, GITHUB),
    #     (LINKEDIN, LINKEDIN),
    #     (INSTAGRAM, INSTAGRAM),
    #     (FACEBOOK, FACEBOOK),
    # ]

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

    api_fields = [
        APIField("company"),
        APIField("location"),
        APIField('role'),
        APIField("begin"),
        APIField("end"),
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
