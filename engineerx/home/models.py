from wagtail.core.models import Page


class HomePage(Page):
    parent_page_types = []
    subpage_types = ['posts.PostsPage', 'accounts.PersonalPages']
