from posts.models import PostsPage
from home.models import HomePage


def create_posts_page(owner):
    if PostsPage.objects.exists():
        return
    posts_page = PostsPage(title='Posts', owner=owner)
    home_page = HomePage.objects.first()
    home_page.add_child(instance=posts_page)
    posts_page = PostsPage.objects.get(slug=posts_page.slug)
    posts_page.save()
    posts_page.save_revision().publish()
