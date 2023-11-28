from django.contrib import admin
from .models import Customer, Category, Book, Loan, Author

@admin.register(Book)
class BooKAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author')
    list_filter = ['category']
    search_fields = ['title', 'category', 'author']
    list_per_page = 12
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'nationality')
    list_filter = ['nationality']
    search_fields = ['name', 'nationality', 'username']
    list_per_page = 12
    
@admin.register(Customer)    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'job', 'email', 'postal') 
    list_filter = ['job']
    search_fields = ['name', 'username', 'job', 'email', 'postal']
    list_per_page = 12
    

@admin.register(Category)    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'label')
    search_fields = ['code', 'label']
    list_per_page = 12
    
 
@admin.register(Loan)    
class LoanAdmin(admin.ModelAdmin):
    list_display = ('begin_date', 'end_date', 'customer', 'book')
    list_filter = ['book']
    search_fields = ['begin_date', 'end_date', 'customer', 'book']
    list_per_page = 12
    
     
