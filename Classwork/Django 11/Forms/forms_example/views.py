from django.shortcuts import render, redirect

from forms_example.forms import ContactForm, FeedbackForm, NoteDraftForm, NoteForm


# Create your views here.

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect("contact_success")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def contact_success(request):
    return render(request, "contact_success.html")


def  feedback_page(request):
    form = FeedbackForm(request.POST or None)
    submitted_data = None
    if request.method == "POST" and form.is_valid():
        submitted_data = form.cleaned_data
    return render(request, "feedback.html", {"form": form, "submitted_data": submitted_data})

def  note_draft(request):
    if request.method == "POST":
        form = NoteDraftForm(request.POST)
        if form.is_valid():
            return redirect("feedback_page")
    else:
        form = NoteDraftForm()
    return render(request, "noteDraft.html", {"form": form})


def create_note(request):
    form = NoteForm(request.POST or None)
    submitted_data = None
    if request.method == "POST" and form.is_valid():
        submitted_data = form.cleaned_data
    return render(request, "create_note.html", {"form": form, "submitted_data": submitted_data})

