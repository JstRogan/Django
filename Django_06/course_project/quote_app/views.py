import random

from django.http import HttpRequest, HttpResponse


QUOTES = [
    "Knowledge is power.",
    "Practice makes progress.",
    "Code and learn every day.",
]


def random_quote_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(random.choice(QUOTES))
