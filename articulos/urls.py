from django.urls import path
from articulos import views

urlpatterns = [
    path('conseguir_subtipo', views.conseguir_subtipo, name='conseguir_subtipo'),
    path("", views.articulos, name="articulos")
]
