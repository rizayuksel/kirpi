from django.urls import path

from kirpi.paramaters import views

urlpatterns = [
    path("v1/paramaters/price/<str:pk>/", views.PriceView.as_view(), name="price"),
]
