from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #req1 to add wiki/TITLE
    path("wiki/search", views.search, name="search"),
    path("wiki/<str:title>",views.entry, name="entry"),
    
]
