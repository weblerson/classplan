from django.db.models.signals import post_save
from django.db import IntegrityError
from django.dispatch import receiver
from .models import User
from django.conf import settings
from hashlib import sha256

from .models import UserActivationToken

from decouple import config

from utils import Utils


@receiver(post_save, sender=User, dispatch_uid='send_email_user_register')
def send_user_email(sender, instance, created, **kwargs):

    if created:
        subject = 'Classplan - Confirmação de Conta'
        token = sha256(f'{instance.get_full_name()}::{instance.email}'.encode()).hexdigest()
        domain = config('DOMAIN', cast=str)

        confirmation_link = f'{domain}/auth/confirm/{token}'

        try:
            user_token = UserActivationToken.objects.create(
                user=instance,
                token=token
            )
            user_token.save()

        except IntegrityError as e:
            print(f'Error: {e}')

            return

        context = {
            'full_name': instance.get_full_name(),
            'platform_name': 'Classplan',
            'confirmation_link': confirmation_link
        }

        return Utils.send_email(
            template_path=settings.USER_CREATION_TEMPLATE_PATH,
            subject=subject,
            to=[instance.email],
            **context
        )
