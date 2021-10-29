from django.urls import path
from prensacables_segun_medida import views

urlpatterns = [
    path("", views.prensacables_segun_medida, name="prensacables_segun_medida")
]
