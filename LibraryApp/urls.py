from django.urls import path

from . import views

app_name = "LibraryApp"

urlpatterns = [
    path("", views.index, name="index"), # library/
    path("<int:book_id>/", views.show, name="show"), # library/id/
    path("ajouter-livre/", views.add, name="add"), # library/ajouter-livre/
    path("ajouter-livre/", views.edit, name="edit"), # library/modifier-livre/
    path("supprimer-livre/", views.remove, name="delete"), # library/suppimer-livre/
]