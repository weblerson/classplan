from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self) -> str:
        return self.username


class UserActivationToken(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'Token de {self.user.username}'
