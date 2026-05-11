from django.contrib import admin

from app.models import Author, Book, Borrowing, Category, Exemplar, StudentProfile

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "birthdate")
    search_fields = ("firstname", "lastname")
    list_filter = ("birthdate",)


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "publication_date")
    search_fields = ("title",)
    list_filter = ("publication_date", "author", "category")
    filter_horizontal = ("author", "category")


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("exemplar", "student", "borrow_date", "return_date")
    search_fields = (
        "exemplar__book__title",
        "student__user__username",
        "student__user__last_name",
        "student__user__first_name",
    )
    list_filter = ("borrow_date", "return_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


class ExemplarAdmin(admin.ModelAdmin):
    list_display = ("book", "state", "available", "barcode")
    search_fields = ("book__title", "barcode")
    list_filter = ("state", "available")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrowing, BorrowingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Exemplar, ExemplarAdmin)
admin.site.register(StudentProfile)
