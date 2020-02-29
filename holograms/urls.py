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
    path('gobo20', views.gobo20, name="gobo20"),
    path('gobo30', views.gobo30, name="gobo30"),
    path('gobo50', views.gobo50, name="gobo50"),
    path('gobo80', views.gobo80, name="gobo80")
]