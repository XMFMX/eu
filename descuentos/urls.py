from django.urls import path
from descuentos import views

urlpatterns = [
    path("", views.descuentos, name="descuentos")
]
