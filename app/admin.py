from django.contrib import admin

from app.models import Author, Book, Borrowing, Category, Exemplar, StudentProfile

# Register your models here.


admin.site.register([Author, Book, Borrowing, Category, Exemplar, StudentProfile])
