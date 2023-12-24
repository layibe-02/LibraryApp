from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Loan

@shared_task
def send_late_reminder_email():
    # Récupérer tous les emprunts en retard
    overdue_loans = Loan.objects.filter(end_date__lt=timezone.now(), rendered=False)

    for loan in overdue_loans:
        subject = 'Rappel de retard pour le livre'
        message = f"Le livre {loan.book.title} doit être rendu avant la date limite."
        from_email = 'libraryappweb@gmail.com'
        to_email = [loan.customer.email]

        send_mail(subject, message, from_email, to_email)
