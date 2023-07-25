from django.core.mail import EmailMultiAlternatives, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


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
