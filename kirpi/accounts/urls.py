from django.urls import path

from kirpi.accounts import views

urlpatterns = [
    path("v1/users/me/", views.LoginView.as_view(), name="my_user_details"),
]