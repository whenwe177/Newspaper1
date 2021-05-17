from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ContributorChangeForm,ContributorCreationForm
from .models import Contributor
# Register your models here.

class ContributorAdmin(UserAdmin):
    add_form = ContributorCreationForm
    form = ContributorChangeForm
    list_display = [
        "email",
        "username",
        "age",
        "gender",
    ]
    model = Contributor

admin.site.register(Contributor,ContributorAdmin)