from wagtail.users import forms as wagtail_forms

from django.contrib.auth import get_user_model

User = get_user_model()


class UserEditForm(wagtail_forms.UserEditForm):
    class Meta:
        model = User
        fields = wagtail_forms.UserEditForm.Meta.fields
        widgets = wagtail_forms.UserEditForm.Meta.widgets


class UserCreationForm(wagtail_forms.UserCreationForm):
    class Meta:
        model = User
        fields = wagtail_forms.UserCreationForm.Meta.fields
        widgets = wagtail_forms.UserCreationForm.Meta.widgets
