from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (RegisterUser, UserLogin, UpdatePasswordView, ResetPasswordView)

urlpatterns = [
    # Auth user
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),

    path("update-password/", UpdatePasswordView.as_view(), name="password_update"),
    path("reset/<uidb64>/<token>/", ResetPasswordView.as_view(), name="reset"),

]
