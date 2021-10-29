from django.urls import path
from gabexel import views

urlpatterns = [
    path("", views.gabexel, name="gabexel")
]
