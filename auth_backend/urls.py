from os import name
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path, re_path
from rest_framework import permissions

from rest_auth.registration.views import RegisterView, VerifyEmailView
from rest_auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
    LogoutView,
)
from allauth.account.views import ConfirmEmailView as AllauthConfirmEmailView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


def empty_view(request):
    return HttpResponse("")


schema_view = get_schema_view(
    openapi.Info(
        title="Login API",
        default_version="v1",
        description="Login and registration",
        terms_of_service="https://google.com/policies/terms/",
        contact=openapi.Contact(email="contacts@yoursite.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/authentication/password/reset",
        PasswordResetView.as_view(),
        name="rest_password_reset",
    ),
    path(
        "api/authentication/password/reset/confirm",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    path("api/authentication/login", LoginView.as_view(), name="rest_login"),
    path("api/authentication/logout", LogoutView.as_view(), name="rest_logout"),
    path(
        "api/authentication/password/change",
        PasswordChangeView.as_view(),
        name="rest_password_change",
    ),
    path(
        "api/password-reset/<uidb64>/<token>/",
        empty_view,
        name="password_reset_confirm",
    ),
    path(
        "api/authentication/registration/", RegisterView.as_view(), name="rest_register"
    ),
    path(
        "api/authentication/registration/verify_email/",
        VerifyEmailView.as_view(),
        name="rest_verify_email",
    ),
    path(
        "api/authentication/registration/account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    re_path(
        r"^api/authentication/registration/account-confirm-email/(?P<key>[-:\w]+)/$",
        AllauthConfirmEmailView.as_view(),
        name="allauth_account_confirmation",
    ),
    path(
        "api/docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="documentation",
    ),
]
