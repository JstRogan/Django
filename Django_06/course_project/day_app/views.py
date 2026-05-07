from datetime import datetime

from django.http import HttpRequest, HttpResponse


def current_day_view(request: HttpRequest) -> HttpResponse:
    current_day = datetime.now().strftime("%A")
    return HttpResponse(f"Today is {current_day}")
