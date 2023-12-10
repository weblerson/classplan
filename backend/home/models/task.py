from django.db import models

from .space import Space


class Task(models.Model):

    name = models.CharField(max_length=64, blank=False, default='Sem nome')
    is_done = models.BooleanField(default=False)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Task of {self.space.user.username}: {self.name}'
