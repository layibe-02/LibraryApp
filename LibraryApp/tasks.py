from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Loan

@shared_task
def send_late_reminder_email():
    """
    Tâche Celery pour envoyer des rappels par e-mail pour les livres en retard.
    """
    # Récupérer tous les emprunts en retard
    overdue_loans = Loan.objects.filter(end_date__lt=timezone.now(), rendered=False)

    for loan in overdue_loans:
        subject = 'Rappel de retard pour le livre'
        message = f"Le livre '{loan.book.title}' doit être rendu avant la date limite."
        from_email = 'libraryappweb@gmail.com'
        to_email = [loan.customer.email]

        # Envoyer l'e-mail
        send_mail(subject, message, from_email, to_email)

        # Ajouter des logs si nécessaire
        # logger.info(f"Email de rappel envoyé à {loan.customer.email} pour le livre {loan.book.title}.")
