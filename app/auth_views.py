from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator


@method_decorator(login_not_required, name="dispatch")
class CustomLoginView(LoginView):
    template_name = "auth/login.html"


@method_decorator(login_not_required, name="dispatch")
class CustomLogoutView(LogoutView):
    template_name = "auth/logout.html"
