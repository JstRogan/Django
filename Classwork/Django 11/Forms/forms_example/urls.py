from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path("", views.contact_page, name="contact_page"),
    path("success/", views.contact_success, name="contact_success"),
    path("create-note/", views.create_note, name="create_note"),

]