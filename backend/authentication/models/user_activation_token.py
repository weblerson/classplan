from .user import User
from django.db import models


class UserActivationToken(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'Token de {self.user.username}'
