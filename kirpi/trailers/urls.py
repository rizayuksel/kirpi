from django.urls import path

from kirpi.trailers import views

urlpatterns = [
    path("v1/trailers/", views.ListCreateTrailersView.as_view(), name="list_trailers"),
    path("v1/trailers/detail/<str:pk>/", views.DetailTrailerView.as_view(), name="trailer_detail"),
    path("v1/trailers/count/", views.TrailerCountView.as_view(), name="trailer_count"),
    path("v1/trailers/bill/<str:pk>/", views.TrailerBillView.as_view(), name="trailer_bill"),
]