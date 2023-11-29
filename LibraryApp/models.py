from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail

class Customer(models.Model):
    name = models.CharField(max_length=60,verbose_name="Nom")
    username = models.CharField(max_length=60, verbose_name="Prenom")
    job = models.CharField(max_length=100, verbose_name="Profession")
    postal =  models.CharField(max_length=50, verbose_name="Adresse postale")
    email = models.EmailField(max_length=254, verbose_name="E-mail")
    registration_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date d'enregistrement")
    
    def __str__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        db_table = "Client"
    
class Author(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nom")
    username = models.CharField(max_length=60, verbose_name="Prenom")
    nationality = models.CharField(verbose_name="Nationalité")
    date_of_birth = models.DateField(verbose_name="Date de naissance")
    
    def __str__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        db_table = "Auteur"
    
class Category(models.Model):
    code = models.CharField(max_length=50)
    label = models.CharField(max_length=100, verbose_name="Etiquette")
    
    def __str__(self) -> str:
        return self.label
    
    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"
        db_table = "Categorie"
    
class Book(models.Model):
    isbn =models.CharField(max_length=50, verbose_name="ISBN")
    title = models.CharField(max_length=100, verbose_name="Titre")
    creation_date = models.DateField(verbose_name="Date de parution")
    total_exemplaires = models.IntegerField(default=1, verbose_name="Nombre total d'exemplaire")
    authors = models.ManyToManyField(Author, verbose_name="Auteur")
    registration_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date d'enregistrement")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Categorie", null=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
        db_table = "Livre"
    
class Loan(models.Model):
    begin_date = models.DateTimeField(default=timezone.now, verbose_name="Date d'emprunt")
    end_date = models.DateField(verbose_name="Delai")
    loan_durarion = models.IntegerField(default=14, verbose_name="Durée de prêt")
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, verbose_name="Client")
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, verbose_name="Livre")
    
    def __str__(self) -> str:
        return self.begin_date
    
    def __str__(self) -> str:
        return self.end_date
    
    def est_en_retard(self):
        return_date = self.end_date + timedelta(days=self.loan_durarion)
        return return_date < timezone.now().date()
    
    def sendMail():
        message = 'Contenu du message'
        send_mail(
            'Sujet du message',
            message,
            'narcisse.layibe@facsciences-uy1.cm',
            ['destinataire@example.com'],
            fail_silently=False,
        )
    
    class Meta:
        verbose_name = "Emprunt"
        verbose_name_plural = "Emprunts"
        db_table = "Emprunt"