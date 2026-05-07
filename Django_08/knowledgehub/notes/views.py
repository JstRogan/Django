from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.middleware.csrf import get_token

from . import data


def notes_list(request: HttpRequest) -> HttpResponse:
    notes = data.list_notes()
    items = ""
    for note in notes:
        items += (
            f'<li><a href="/notes/{note["id"]}/">{note["title"]}</a> '
            f'<a href="/notes/{note["id"]}/delete">Delete</a></li>'
        )
    return HttpResponse(f"<h1>Notes</h1><ul>{items}</ul>")


def note_detail(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)
    if note is None:
        return HttpResponse("<h1>Note not found</h1>", status=404)

    html = (
        f"<h1>{note['title']}</h1>"
        f"<p>{note['body']}</p>"
        f"<p>Tag: {note['tag']}</p>"
        f'<p><a href="/notes/{note_id}/delete">Delete note</a></p>'
        f'<p><a href="/">Back to list</a></p>'
    )
    return HttpResponse(html)


def note_delete(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)
    if note is None:
        return HttpResponse("<h1>Note not found</h1>", status=404)

    if request.method == "POST":
        data.delete_note(note_id)
        return redirect("notes_list")

    csrf_token = get_token(request)
    html = (
        "<h1>Delete note?</h1>"
        f"<p>{note['title']}</p>"
        f'<form method="post" action="/notes/{note_id}/delete">'
        f'<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">'
        '<button type="submit">Yes, delete</button>'
        f'<a href="/notes/{note_id}/"> Cancel</a>'
        "</form>"
    )
    return HttpResponse(html)
