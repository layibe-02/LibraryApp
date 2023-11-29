from django.template.loader import render_to_string
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Loan, Book, Customer

@shared_task
def envoyer_emails_retard():
    emprunts_en_retard = Loan.objects.filter(est_en_retard=True)

    for emprunt in emprunts_en_retard:
        Customer = emprunt.Customer
        Customer = emprunt.Book

        sujet = 'Rappel : Retour du livre en retard'
        message = f"Cher {Customer.name},\n\nLe livre '{Book.title}' emprunté le {emprunt.end_date.strftime('%d/%m/%Y')} est en retard. Veuillez le retourner dès que possible.\n\nCordialement,\nVotre bibliothèque"

        send_mail(sujet, message, 'narcisse.layibe@facsciences-uy1.cm', [Customer.email])
'''        
@shared_task
def envoyer_emails_retard():
    emprunts_en_retard = Loan.objects.filter(est_en_retard=True)

    for emprunt in emprunts_en_retard:
        Customer = emprunt.customer
        Book = emprunt.Book

        sujet = 'Rappel : Retour du livre en retard'
        contexte = {
            'client': Customer,
            'livre': Book,
            'emprunt': emprunt,
        }
        message = render_to_string('email_retard.txt', contexte)

        send_mail(sujet, message, 'narcisse.layibe@facsciences-uy1.cm', [Customer.email], fail_silently=False)
'''