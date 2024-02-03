from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
     path("edit/<int:id>/", views.edit_contact, name="edit_contact"),
     path("delete/<int:id>/", views.delete_contact, name="delete_contact"),
      path("details/<int:id>/", views.contact_details, name="contact_details"),
]
