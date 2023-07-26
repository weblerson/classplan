from .user import User
from django.db import models


class UserActivationToken(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
    active = models.BooleanField()

    def __str__(self) -> str:
        return f'Token de {self.user.username} - {"Usado" if self.active else "Não Usado"}'
