from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Contributor

class ContributorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Contributor
        fields = (
            "username",
            "email",
            "age",
            "gender"
            )

class ContributorChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Contributor
        fields = (
            "username",
            "email",
            "age",
            "gender",
        )