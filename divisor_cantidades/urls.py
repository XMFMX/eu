from django.urls import path
from divisor_cantidades import views

urlpatterns = [
    path("", views.divisor_cantidades, name="divisor_cantidades")
]
