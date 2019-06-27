from django.contrib import admin

# Register your models here.
from book.models import Author, Book, Category

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
#admin.site.register(Genre)
