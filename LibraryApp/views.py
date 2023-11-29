from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader 
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from .models import Book, Customer, Loan, Author

"""
INSERT   : create()
SELECT   : all(), get()
WHERE    : filter()
                  __gt, __lt, __gte, __lte, __startswith, __endswith
ORDER BY : order_by()
LIMIT    : [:n], [n:]

Les méthodes prédefinies de django: save(), delete()

"""


def index(request):
    context = {"books": Book.objects.all().order_by("title")}
    return render(request, "LibraryApp/index.html", context)

def show(request, book_id):
    context = {"book": get_object_or_404(Book, pk=book_id)}
    return render(request, "LibraryApp/show.html", context)

def add(request):
    pass

def edit(request):
    pass

def remove(request):
    pass