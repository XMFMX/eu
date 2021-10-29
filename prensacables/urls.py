from django.urls import path
from prensacables import views

urlpatterns = [
    path("", views.prensacables, name="prensacables")
]
