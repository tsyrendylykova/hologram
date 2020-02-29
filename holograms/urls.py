from django.urls import path
from . import views

urlpatterns = [
    path('', views.holograms, name='holograms'),
    path('fa30n', views.fa30n, name="fa30n"),
    path('fa42hd', views.fa42hd, name="fa42hd"),
    path('fa65n', views.fa65n, name="fa65n"),
    path('fa70n', views.fa70n, name="fa70n"),
    path('fa85n', views.fa85n, name="fa85n"),
    path('fa100n', views.fa100n, name="fa100n"),
]