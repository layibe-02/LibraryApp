from django.urls import path
from . import views

app_name = 'LibraryApp'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('list/', views.book_list, name='book_list'),
    path('loan_list/', views.loan_list, name='loan_list'),
    path('author_list/', views.author_list, name='author_list'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_loan/', views.add_loan, name='add_loan'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('show/<int:book_id>/', views.show, name='show'),
    path('show_customer/<int:customer_id>/', views.show_customer, name='show_customer'),
    path('edit_loan/<int:loan_id>', views.edit_loan, name='edit_loan'),
    path('edit_customer/<int:customer_id>', views.edit_customer, name='edit_customer'),
    path('edit_book/<int:book_id>', views.edit_book, name='edit_book'),
    path('edit_author/<int:author_id>', views.edit_author, name='edit_author'),
    path('delete_loan/<int:loan_id>/', views.delete_loan, name='delete_loan'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('delete_author/<int:author_id>/', views.delete_author, name='delete_author'),
    path('category_list/', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
]
