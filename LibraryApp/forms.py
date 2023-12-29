from django import forms
from .models import Book, Loan, Author, Customer, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'date_publication', 'total_exemplaires', 'authors', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajoutez des attributs de classe, des styles CSS, etc., selon vos besoins
        self.fields['isbn'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez l\'ISBN'})
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez le titre'})
        self.fields['date_publication'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Entrez l\'année'})
        self.fields['total_exemplaires'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Entrez le nombre d\'exemplaires'})
        self.fields['authors'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['begin_date', 'end_date', 'customer', 'book', 'rendered']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['begin_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez la date d\'emprunt'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez la date de retour'})
        self.fields['customer'].widget.attrs.update({'class': 'form-control'})
        self.fields['book'].widget.attrs.update({'class': 'form-control'})
        self.fields['rendered'].widget.attrs.update({'class': 'form-check-input'})
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'username', 'nationality', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez le nom'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez le prénom'})
        self.fields['nationality'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez la nationalité'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez la date de naissance'})
        

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'username', 'job', 'postal', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez le nom'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez le prénom'})
        self.fields['job'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez la profession'})
        self.fields['postal'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez l\' adresse'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez l\'email'})
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['code', 'label']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez le code'})
        self.fields['label'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Saisissez l\'étiquette'})
    

class SearchBookForm(forms.Form):
    search_query_book = forms.CharField(label='Rechercher un livre', max_length=100, required=False)
    
class SearchAuthorForm(forms.Form):
    search_query_author = forms.CharField(label='Rechercher un auteur', max_length=100, required=False)
    
class SearchCustomerForm(forms.Form):
    search_query_customer = forms.CharField(label='Rechercher un client', max_length=100, required=False)

class SearchCategoryForm(forms.Form):
    search_query_category = forms.CharField(label='Rechercher une catégorie', max_length=100, required=False)
    
class SearchLoanForm(forms.Form):
    search_query_loan = forms.CharField(label='Rechercher un emprunt', max_length=100, required=False)