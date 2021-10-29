from django.urls import path
from pesos_dolares import views

urlpatterns = [
    path("", views.pesos_dolares, name="pesos_dolares")
]
