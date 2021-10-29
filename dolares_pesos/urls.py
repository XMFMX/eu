from django.urls import path
from dolares_pesos import views

urlpatterns = [
    path("", views.dolares_pesos, name="dolares_pesos")
]
