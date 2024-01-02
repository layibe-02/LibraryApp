from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test     
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader 
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from .models import Book, Customer, Loan, Author, Category
from django.contrib import messages
from .forms import BookForm, LoanForm, AuthorForm, CustomerForm, CategoryForm, SearchBookForm, SearchCategoryForm, SearchCustomerForm, SearchAuthorForm, SearchLoanForm

#______________________________________________________________________________________________________

def index(request):
    return render(request, "LibraryApp/index.html")

def is_visitor(user):
    return user.groups.filter(name = "Visiteurs").exists()

from .tasks import send_late_reminder_email
def email_task(request):
    result = send_late_reminder_email.delay()
    return render(request, 'LibraryApp/email_task.html', {'result': result})

def email_task_result(request, task_id):
    resultat = send_late_reminder_email.AsyncResult(task_id)
    
    if resultat.ready():
        return render(request, 'LibraryApp/email_task_result.html', {'resultat': resultat})
    return render(request, 'LibraryApp/email_task_result.html', {'resultat': 'result not ready yet'})


#------------------------------------------------------------------------------------------------------

@login_required
@permission_required("LibraryApp.add_book")
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            form = BookForm()
            # Rediriger vers la page d'index après l'enregistrement du livre
            return redirect("LibraryApp:add_book")
    else:
        form = BookForm()

    context = { "form" : form }
    return render(request, "LibraryApp/add_book.html", context)

@login_required
@permission_required("LibraryApp.add_author")
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            form = AuthorForm()
            return redirect("LibraryApp:add_author")
    else:
        form = AuthorForm()
        
    context = {"form": form}
    return render(request, "LibraryApp/add_author.html", context)

@login_required
@permission_required("LibraryApp.add_loan")
def add_loan(request):
    error_message = None

    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            
            # Vérifier si le livre a des exemplaires disponibles
            if loan.book.total_exemplaires > 0:
                # Décrémenter le nombre d'exemplaires disponibles
                loan.book.total_exemplaires -= 1
                loan.book.save()

                loan.save()
                form = LoanForm()
                return redirect("LibraryApp:add_loan")
            else:
                # Ajouter un message d'erreur au formulaire
                error_message = "Désolé, tous les exemplaires de ce livre sont empruntés."
                form.add_error(None, error_message)
    else:
        form = LoanForm()

    context = {"form": form, "error_message": error_message}
    return render(request, "LibraryApp/add_loan.html", context)
 
@login_required     
@permission_required("LibraryApp.add_customer")  
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            form = CustomerForm()
            return redirect("LibraryApp:add_customer")
    else:
        form = CustomerForm()
        
    context = {"form":form}
    return render(request,"LibraryApp/add_customer.html", context)

@login_required
@permission_required("LibraryApp.add_category")
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryForm()
            return redirect("LibraryApp:add_category")
    else:
        form = CategoryForm()
        
    context = {"form":form}
    return render(request,"LibraryApp/add_category.html", context)
#------------------------------------------------------------------------------------------------------

@login_required   
def show_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {"book": book}
    return render(request, "LibraryApp/show_book.html", context)

@login_required
@permission_required("LibraryApp.change_customer")
def show_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {"customer": customer}
    return render(request, "LibraryApp/show_customer.html", context)

#------------------------------------------------------------------------------------------------------

@login_required
def book_list(request):
    form = SearchBookForm(request.GET)
    books = Book.objects.all().order_by("title")

    if form.is_valid():
        search_query_book = form.cleaned_data.get('search_query_book')

        if search_query_book:
            # Filtrez les livres par titre, isbn
            books = books.filter(
                Q(title__icontains=search_query_book) | 
                Q(isbn__icontains=search_query_book)
            )
            
    context = {
        'books': books,
        'form': form,
    }
    return render(request, "LibraryApp/book_list.html", context)

@login_required
def loan_list(request):
    form = SearchLoanForm(request.GET)
    loans = Loan.objects.all().order_by("-begin_date")
    
    if form.is_valid():
        search_query_loan = form.cleaned_data.get('search_query_loan')

        if search_query_loan:
            loans = loans.filter(
                Q(rendered__icontains=search_query_loan) | 
                Q(customer__name__icontains=search_query_loan) | 
                Q(book__title__icontains=search_query_loan)
            )

    context = {
        'loans': loans,
        'form': form,
    }
    return render(request, "LibraryApp/loan_list.html", context) 

@login_required
def author_list(request):
    form = SearchAuthorForm(request.GET)
    authors = Author.objects.all().order_by("name")
    
    if form.is_valid():
        search_query_author = form.cleaned_data.get('search_query_author')

        if search_query_author:
            authors = authors.filter(
                Q(name__icontains=search_query_author) | 
                Q(username__icontains=search_query_author) | 
                Q(nationality__icontains=search_query_author) | 
                Q(date_of_birth__icontains=search_query_author)
            )

    context = {
        'authors': authors,
        'form': form,
    }
    return render(request, "LibraryApp/author_list.html", context)

@login_required
def customer_list(request):
    form = SearchCustomerForm(request.GET)
    customers = Customer.objects.all().order_by("-registration_date")
    
    if form.is_valid():
        search_query_customer = form.cleaned_data.get('search_query_customer')

        if search_query_customer:
            customers = customers.filter(
                Q(name__icontains=search_query_customer) | 
                Q(username__icontains=search_query_customer) |
                Q(job__icontains=search_query_customer) |
                Q(postal__icontains=search_query_customer) |
                Q(email__icontains=search_query_customer)
            )

    context = {
        'customers': customers,
        'form': form,
    }
    return render(request, "LibraryApp/customer_list.html", context)

@login_required
def category_list(request):
    form = SearchCategoryForm(request.GET)
    categories = Category.objects.all().order_by('label')
    
    if form.is_valid():
        search_query_category = form.cleaned_data.get('search_query_category')

        if search_query_category:
            categories = categories.filter(
                Q(code__icontains=search_query_category) | 
                Q(label__icontains=search_query_category)
            )

    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, "LibraryApp/category_list.html", context)
    
#------------------------------------------------------------------------------------------------------

@login_required
@permission_required("LibraryApp.change_loan")
def edit_loan(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)

    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            # Vérifier si le statut de rendu a changé
            if loan.rendered != form.cleaned_data['rendered'] and form.cleaned_data['rendered']:
                # Le livre a été rendu, incrémenter le nombre d'exemplaires
                loan.book.total_exemplaires += 1
                loan.book.save()

            form.save()
            return redirect('LibraryApp:loan_list')
    else:
        form = LoanForm(instance=loan)

    context = {
        'form': form,
        'loan': loan,
    }
    return render(request, 'LibraryApp/edit_loan.html', context)

@login_required
@permission_required("LibraryApp.change_customer")
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('LibraryApp:customer_list')
    else:
        form = CustomerForm(instance=customer)

    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'LibraryApp/edit_customer.html', context)

@login_required
@permission_required("LibraryApp.change_book")
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('LibraryApp:book_list')
    else:
        form = BookForm(instance=book)

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'LibraryApp/edit_book.html', context)

@login_required
@permission_required("LibraryApp.change_author")
def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('LibraryApp:author_list')
    else:
        form = AuthorForm(instance=author)

    context = {
        'form': form,
        'author': author,
    }
    return render(request, 'LibraryApp/edit_author.html', context)

@login_required
@permission_required("LibraryApp.change_category")
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('LibraryApp:category_list')
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'LibraryApp/edit_category.html', context)

#------------------------------------------------------------------------------------------------------

@login_required
@permission_required("LibraryApp.delete_loan")
def delete_loan(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)

    if request.method == 'POST':
        loan.delete()
        return redirect('LibraryApp:loan_list')

    context = {'loan': loan}
    return render(request, 'LibraryApp/delete_loan.html', context)

@login_required
@permission_required("LibraryApp.delete_customer")
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        customer.delete()
        return redirect('LibraryApp:customer_list')

    context = {'customer': customer}
    return render(request, 'LibraryApp/delete_customer.html', context)

@login_required
@permission_required("LibraryApp.delete_book")
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('LibraryApp:book_list')

    context = {'book': book}
    return render(request, 'LibraryApp/delete_book.html', context)

@login_required
@permission_required("LibraryApp.delete_author")
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        author.delete()
        return redirect('LibraryApp:author_list')

    context = {'author': author}
    return render(request, 'LibraryApp/delete_author.html', context)

@login_required
@permission_required("LibraryApp.delete_category")
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        category.delete()
        return redirect('LibraryApp:category_list')

    context = {'category': category}
    return render(request, 'LibraryApp/delete_category.html', context)