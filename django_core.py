from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import exceptions
from rest_framework.serializers import as_serializer_error
from rest_framework.views import exception_handler


def custom_exception_handler(exc, ctx):
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))
    response = exception_handler(exc, ctx)
    # If unexpected error occurs (server error, etc.)
    if response is None:
        return response
    return response


"""
exception_handler is a function that takes an exception and a context as arguments and returns a response.
"""

# from django.core.exceptions import PermissionDenied
# from django.core.exceptions import ValidationError as DjangoValidationError
# from django.http import Http404
# from rest_framework import exceptions
# from rest_framework.serializers import as_serializer_error
# from rest_framework.views import exception_handler


def drf_default_with_modifications_exception_handler(exc, ctx):
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
    response = exception_handler(exc, ctx)
    # If unexpected error occurs (server error, etc.)
    if response is None:
        return response
    if isinstance(exc.detail, (list, dict)):
        response.data = {"detail": response.data}
    return response


"""
Exemplary usage of the function:"""
from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import Http404
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.serializers import as_serializer_error
from rest_framework.views import exception_handler
from styleguide_example.core.exceptions import ApplicationError


def hacksoft_proposed_exception_handler(exc, ctx):
    """
    {
        "message": "Error message",
        "extra": {}
    }
    """
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = exception_handler(exc, ctx)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        if isinstance(exc, ApplicationError):
            data = {"message": exc.message, "extra": exc.extra}
            return Response(data, status=400)

        return response

    if isinstance(exc.detail, (list, dict)):
        response.data = {"detail": response.data}

    if isinstance(exc, exceptions.ValidationError):
        response.data["message"] = "Validation error"
        response.data["extra"] = {"fields": response.data["detail"]}
    else:
        response.data["message"] = response.data["detail"]
        response.data["extra"] = {}

    del response.data["detail"]

    return response


"""
EMAIL SERVICE
"""

from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from styleguide_example.common.services import model_update
from styleguide_example.core.exceptions import ApplicationError
from styleguide_example.emails.models import Email


@transaction.atomic
def email_send(email: Email) -> Email:
    if email.status != Email.Status.SENDING:
        raise ApplicationError(
            f"Cannot send non-ready emails. Current status is {email.status}"
        )

    subject = email.subject
    from_email = "styleguide-example@hacksoft.io"
    to = email.to

    html = email.html
    plain_text = email.plain_text

    msg = EmailMultiAlternatives(subject, plain_text, from_email, [to])
    msg.attach_alternative(html, "text/html")

    msg.send()

    email, _ = model_update(
        instance=email,
        fields=["status", "sent_at"],
        data={"status": Email.Status.SENT, "sent_at": timezone.now()},
    )
    return email


"""
EMAIL SERVICE TASK HANDLER (CELERY)
"""

from celery import shared_task
from styleguide_example.emails.models import Email


@shared_task
def email_send(email_id):
    email = Email.objects.get(id=email_id)
    from styleguide_example.emails.services import email_send

    email_send(email)


from django.db import transaction

# ... more imports here ...
from styleguide_example.emails.tasks import email_send as email_send_task


@transaction.atomic
def user_complete_onboarding(user: User) -> User:
    # ... some code here
    email = email_get_onboarding_template(user=user)
    transaction.on_commit(lambda: email_send_task.delay(email.id))
    return user


"""
TASK ERROR HANDLING (CELERY)
"""
from celery import shared_task
from celery.utils.log import get_task_logger
from styleguide_example.emails.models import Email

logger = get_task_logger(__name__)


def _email_send_failure(self, exc, task_id, args, kwargs, einfo):
    email_id = args[0]
    email = Email.objects.get(id=email_id)

    from styleguide_example.emails.services import email_failed

    email_failed(email)


@shared_task(bind=True, on_failure=_email_send_failure)
def email_send(self, email_id):
    email = Email.objects.get(id=email_id)

    from styleguide_example.emails.services import email_send

    try:
        email_send(email)
    except Exception as exc:
        # https://docs.celeryq.dev/en/stable/userguide/tasks.html#retrying
        logger.warning(f"Exception occurred while sending email: {exc}")
        self.retry(exc=exc, countdown=5)


"""
Periodic tasks (CELERY)
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from django_celery_beat.models import (
    CrontabSchedule,
    IntervalSchedule,
    PeriodicTask,
)
from project.app.tasks import some_periodic_task


class Command(BaseCommand):
    help = f"""
    Setup celery beat periodic tasks.
    Following tasks will be created:
    - {some_periodic_task.name}
    """

    @transaction.atomic
    def handle(self, *args, **kwargs):
        print("Deleting all periodic tasks and schedules...\n")
        IntervalSchedule.objects.all().delete()
        CrontabSchedule.objects.all().delete()
        PeriodicTask.objects.all().delete()
        periodic_tasks_data = [
            {
                "task": some_periodic_task,
                "name": "Do some peridoic stuff",
                # https://crontab.guru/#15_*_*_*_*
                "cron": {
                    "minute": "15",
                    "hour": "*",
                    "day_of_week": "*",
                    "day_of_month": "*",
                    "month_of_year": "*",
                },
                "enabled": True,
            },
        ]
        for periodic_task in periodic_tasks_data:
            print(f'Setting up {periodic_task["task"].name}')
            cron = CrontabSchedule.objects.create(**periodic_task["cron"])
            PeriodicTask.objects.create(
                name=periodic_task["name"],
                task=periodic_task["task"].name,
                crontab=cron,
                enabled=periodic_task["enabled"],
            )
