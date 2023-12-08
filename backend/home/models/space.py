from django.db import models

from authentication.models import User


class Space(models.Model):

    image = models.ImageField(upload_to='/media/home/spaces', default='default.jpg')
    title = models.CharField(max_length=32, blank=False, default='Filmes, séries etc.')
    objective = models.TextField(default='Assistir coisas legais')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)
    is_personal = models.BooleanField(default=False)
    partners = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return f'Space of {self.user.username}'
