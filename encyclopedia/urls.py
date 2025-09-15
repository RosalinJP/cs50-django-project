from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #req1 to add wiki/TITLE
    path(f"wiki/<str:title>",views.entry, name="entry")
]
