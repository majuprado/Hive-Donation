from django.urls import path
from . import views

urlpatterns = [    
    path("index", views.index, name="index"),
    path("sobre", views.sobre, name="sobre"),
    path("equipe", views.equipe, name="equipe")
]