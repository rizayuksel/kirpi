from django.urls import path

from kirpi.trailers import views

urlpatterns = [
    path("v1/trailers/list/", views.ListTrailersView.as_view(), name="list_trailers"),
    path("v1/trailers/detail/<str:pk>/", views.DetailTrailerView.as_view(), name="trailer_detail"),
]