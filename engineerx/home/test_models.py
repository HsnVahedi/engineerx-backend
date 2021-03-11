from wagtail.tests.utils import WagtailPageTests

from home.models import PostPage, HomePage


class PostPageTestCase(WagtailPageTests):
    def test_post_pages_parents(self):
        self.assertAllowedParentPageTypes(
            PostPage, {HomePage}
        )

    def test_home_page_children(self):
        self.assertAllowedSubpageTypes(
            HomePage, {PostPage}
        )
