import random

from django.http import HttpRequest, HttpResponse

quotes = [
    "Знание — сила.",
    "Век живи — век учись.",
    "Делу время, потехе час.",
    "Терпение и труд всё перетрут.",
    "Повторение — мать учения.",
]


def random_quote(request: HttpRequest) -> HttpResponse:
    return HttpResponse(random.choice(quotes))
