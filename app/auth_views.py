from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = "auth/login.html"


class CustomLogoutView(LogoutView):
    template_name = "auth/logout.html"

    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
