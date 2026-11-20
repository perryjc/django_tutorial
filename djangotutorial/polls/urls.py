from django.urls import path

from . import views

# gets the code from "views.py" and makes a page from it named "index"
urlpatterns = [
    path("", views.index, name="index"),
]