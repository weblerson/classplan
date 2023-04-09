from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = User
