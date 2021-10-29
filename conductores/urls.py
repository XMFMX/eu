from django.urls import path
from conductores import views

urlpatterns = [
    path("", views.conductores, name="conductores")
]
