from django.urls import path
from prensacables_segun_conductor import views

urlpatterns = [
    path("", views.prensacables_segun_conductor, name="prensacables_segun_conductor")
]
