from accounts.models import PersonalPages
from home.models import HomePage


def create_personal_accounts_page(owner):
    if PersonalPages.objects.exists():
        return
    accounts_page = PersonalPages(title='Personal Pages', owner=owner)
    home_page = HomePage.objects.first()
    home_page.add_child(instance=accounts_page)
    accounts_page = PersonalPages.objects.get(slug=accounts_page.slug)
    accounts_page.save()
    accounts_page.save_revision().publish()
