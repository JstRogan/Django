NOTES = [
    {
        "id": 1,
        "title": "Django routes",
        "body": "Path helps create readable urls.",
        "tag": "Django",
        "category": "backend",
    },
    {
        "id": 2,
        "title": "Templates",
        "body": "Templates show data in html pages.",
        "tag": "HTML",
        "category": "frontend",
    },
    {
        "id": 3,
        "title": "Views",
        "body": "Views process request and return response.",
        "tag": "Python",
        "category": "backend",
    },
]


def list_notes():
    return NOTES


def get_note(note_id):
    for note in NOTES:
        if note["id"] == note_id:
            return note
    return None


def delete_note(note_id):
    for index, note in enumerate(NOTES):
        if note["id"] == note_id:
            del NOTES[index]
            return True
    return False
