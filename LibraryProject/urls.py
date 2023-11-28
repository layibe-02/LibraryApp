from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("library/", include("LibraryApp.urls")),
    path("admin/", admin.site.urls),
]