# bookjoin/bookjoin/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("books.urls")),  # mount the app at the site root
]
