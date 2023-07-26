import string

from django.core.mail import EmailMultiAlternatives, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

import random
import string


class Utils:

    @staticmethod
    def send_email(template_path: str, subject: str, to: list[str], **kwargs) -> None:

        html_content = render_to_string(template_path, kwargs)
        text_content = strip_tags(html_content)

        try:
            msg = EmailMultiAlternatives(
                subject, text_content, settings.EMAIL_HOST_USER, to
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

        except BadHeaderError as e:
            print(f'Error: {e}')

    @staticmethod
    def create_random_password() -> str:

        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        _string = f'{letters}{numbers}{symbols}'

        password = ''.join(random.choices(_string, k=64))

        return password
