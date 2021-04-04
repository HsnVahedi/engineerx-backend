from django.core.exceptions import ValidationError
from wagtail.admin.forms import WagtailAdminPageForm


class PersonalPageForm(WagtailAdminPageForm):
    
    def clean(self):
        pages = self.instance.__class__.objects.filter(owner=self.instance.owner)
        for page in pages:
            if page.pk and (not self.instance.pk):
                raise ValidationError('Personal page already exists', code='invalid')
        return super().clean()
