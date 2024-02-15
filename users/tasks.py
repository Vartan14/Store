import uuid

from celery import shared_task
from django.utils.timezone import now
from datetime import timedelta
from users.models import User, EmailVerification


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expiration_date = now() + timedelta(days=2)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expires_at=expiration_date)
    record.send_verification_email()
