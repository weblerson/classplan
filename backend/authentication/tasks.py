from celery import shared_task

from django.core.mail import BadHeaderError

from utils import Utils


@shared_task(name='send_email', bind=True, max_retries=5, default_retry_delay=5)
def send_email_task(self, template_path: str, subject: str, to: list[str], **kwargs) -> None:
    try:

        return Utils.send_email(template_path, subject, to, **kwargs)

    except BadHeaderError as e:
        self.retry(countdown=2 * self.request.retries)

        raise BadHeaderError(e)
