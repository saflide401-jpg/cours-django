from django.db import models


# Create your models here.
class Author(models.Model):
    firstname = models.CharField("Prénom", max_length=100)
    lastname = models.CharField("Nom", max_length=100)
    birthdate = models.DateField("Date de naissance", null=True)
    biography = models.TextField("Biographie", null=True, blank=True)


class Category(models.Model):
    name = models.CharField("Nom", max_length=100)
    description = models.TextField("Description", null=True, blank=True)


class Book(models.Model):
    title = models.CharField("Titre", max_length=200)
    author = models.ManyToManyField(Author, related_name="books")
    category = models.ManyToManyField(Category, related_name="books")
    publication_date = models.DateField("Date de publication", null=True)
    summary = models.TextField("Résumé", null=True, blank=True)
    isbn = models.CharField("ISBN", max_length=20, null=True, blank=True)
    cover_image = models.ImageField(
        "Image de couverture", upload_to="covers/", null=True, blank=True
    )


class Exemplar(models.Model):
    STATES = [
        ("new", "Neuf"),
        ("good", "Bon état"),
        ("used", "Usagé"),
        ("damaged", "Endommagé"),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="exemplars")
    state = models.CharField("État", max_length=10, choices=STATES, default="new")
    available = models.BooleanField("Disponible", default=True)
    barcode = models.CharField("Code-barres", max_length=50, unique=True)


class StudentProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    matricule = models.CharField("Matricule/INE", max_length=20, unique=True)
    birthdate = models.DateField("Date de naissance", null=True)


class Borrowing(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    exemplar = models.ForeignKey(
        Exemplar, on_delete=models.CASCADE, related_name="borrowings"
    )
    borrow_date = models.DateField("Date d'emprunt", auto_now_add=True)
    return_date = models.DateField("Date de retour", null=True, blank=True)
    librarian = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="processed_borrowings",
    )
    comments = models.TextField("Commentaires", null=True, blank=True)
