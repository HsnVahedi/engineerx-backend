from django.core.exceptions import ValidationError
from wagtail.admin.forms import WagtailAdminPageForm


class PersonalPageForm(WagtailAdminPageForm):
    pass

    # def save(self, *args, **kwargs):
    #     self.instance.title = f'{self.instance.owner.first_name} {self.instance.owner.last_name}'
    #     return super().save(*args, **kwargs)

    def clean(self):
        pages = self.instance.__class__.objects.filter(owner=self.instance.owner)
        for page in pages:
            if page.pk and (not self.instance.pk):
                raise ValidationError('Personal page already exists', code='invalid')
        return super().clean()
