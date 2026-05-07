from django.urls import path

from . import views


urlpatterns = [
    path("", views.notes_list, name="notes_list"),
    path("notes/<int:note_id>/", views.note_detail, name="note_detail"),
    path("notes/<int:note_id>/delete", views.note_delete, name="note_delete"),
]
