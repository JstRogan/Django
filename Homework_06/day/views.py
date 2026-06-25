from datetime import datetime

from django.http import HttpRequest, HttpResponse

days = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]


def current_day(request: HttpRequest) -> HttpResponse:
    day = days[datetime.now().weekday()]
    return HttpResponse(day)
