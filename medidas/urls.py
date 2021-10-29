from django.urls import path
from medidas import views

urlpatterns = [
    path("", views.medidas, name="medidas")
]
