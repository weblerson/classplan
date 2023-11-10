from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserActivationToken
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = User


@admin.register(UserActivationToken)
class UserActivationTokenAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Informação Pessoal', {'fields': ('user',)}),
        ('Token', {'fields': ('token',)})
    )

    readonly_fields = ['user', 'token']
