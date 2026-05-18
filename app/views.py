from django.shortcuts import render
from django.utils.timezone import now
from django.views.generic import TemplateView, DetailView
from django.db.models import Count

from app.models import Book, Exemplar, Borrowing

# Create your views here.


class HomeView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # select count(*) from app_borrowing where return_date = null;
        emprunts_actifs = Borrowing.objects.filter(return_date__isnull=True)
        # select count(*) from app_borrowing where return_date = null and expected_return_date < current_date;
        retards = Borrowing.objects.filter(
            return_date__isnull=True, expected_return_date__lt=now()
        )
        # select count(*) from app_exemplar where not in (select exemplar_id from app_borrowing where return_date = null);
        exemplaires_disponibles = Exemplar.objects.filter(
            available=True, borrowings__return_date__isnull=True
        )
        top_books = Book.objects.annotate(
            nb_emprunts=Count("exemplars__borrowings")
        ).order_by("-nb_emprunts")[:10]

        if hasattr(user, "student_profile") and user.student_profile is not None:
            emprunts_actifs = emprunts_actifs.filter(student=user.student_profile)
            retards = retards.filter(student=user.student_profile)

        context["stats"] = {
            "emprunts_actifs": emprunts_actifs.count(),
            "retards": retards.count(),
            "exemplaires_dispo": exemplaires_disponibles.count(),
            "reservations": 0,
        }

        context["top_livres"] = top_books

        context["retards_recents"] = retards[:10]
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "catalogue/livre_detail.html"
