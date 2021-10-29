from django.urls import path
from genrod import views

urlpatterns = [
    path("", views.genrod, name="genrod")
]
