from django.conf import settings
from django.db import models
from django.shortcuts import redirect
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TagBase, ItemBase
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.api import APIField
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from posts.blocks import SectionsBlock
from accounts.models import PersonalPage
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.users.models import UserProfile


class PostTag(TagBase):
    pass


class TaggedPost(ItemBase):
    tag = models.ForeignKey(
        PostTag, related_name="tagged_posts", on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        to='posts.PostPage',
        on_delete=models.CASCADE,
        related_name='tagged_items'
    )


class PostsPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['posts.PostPage']

    content_panels = []
    promote_panels = []
    settings_panels = []


class PostPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    sections = StreamField(SectionsBlock())
    tags = ClusterTaggableManager(through=TaggedPost, blank=True)

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
            'has_personal_page': PersonalPage.objects.filter(owner__id=self.owner.id).exists()
        }

    api_fields = [
        APIField('image', serializer=ImageRenditionField('min-1500x200')),
        APIField('image_16x9', serializer=ImageRenditionField('fill-1600x900-c70', source='image')),
        APIField('sections'),
        APIField('tags'),
        APIField('owner_info'),
        APIField('owner'),
    ]

    parent_page_types = ['posts.PostsPage']
    subpage_types = []

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('sections'),
        FieldPanel('tags')
    ]
    promote_panels = []
    settings_panels = []

    def serve(self, request, *args, **kwargs):
        return redirect(f'{settings.FRONTEND_URL}/posts/{self.slug}')

    def get_url_parts(self, *args, **kwargs):
        url_parts = super().get_url_parts(*args, **kwargs)

        # if url_parts is None:
        #     # in this case, the page doesn't have a well-defined URL in the first place -
        #     # for example, it's been created at the top level of the page tree
        #     # and hasn't been associated with a site record
        #     return None
        if settings.PRODUCTION:
            site_id, root_url, page_path = url_parts
            return site_id, root_url, f'/posts/{self.slug}'
        else:
            return url_parts
