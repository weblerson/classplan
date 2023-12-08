from django.db import models

from authentication.models import User


class Space(models.Model):

    image = models.ImageField(upload_to='/media/home/spaces')
    title = models.CharField(max_length=32, blank=False, default='Sem Título')
    objective = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
