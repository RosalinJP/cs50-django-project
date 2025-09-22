from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #req1 to add wiki/TITLE
    path("wiki/search", views.search, name="search"),
    path("wiki/new", views.new,name="new"),
    path("wiki/edit", views.edit,name="edit"),
    path("wiki/save", views.save,name="save"),
    path("wiki/random", views.random,name="random"),
    path("wiki/<str:title>",views.entry, name="entry")
   
    
]
