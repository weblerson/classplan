from django.contrib import admin

from .models import Space, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Tarefa', {'fields': ('name', 'is_done')}),
        ('Relação', {'fields': ('space',)})
    )

    readonly_fields = ('space',)


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Informações', {'fields': ('image', 'title', 'objective', 'user')}),
        ('Privacidade', {'fields': ('is_private', 'is_personal')}),
        ('Parceiros', {'fields': ('partners',)})
    )

    readonly_fields = ('user', 'is_personal')
