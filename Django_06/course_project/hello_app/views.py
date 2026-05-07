from django.http import HttpRequest, HttpResponse


def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, World!")
