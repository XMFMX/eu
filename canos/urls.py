from django.urls import path
from canos import views

urlpatterns = [
    path("", views.canos, name="canos")
]
