from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/home.html")


def football(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/football.html")


def hockey(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/hockey.html")


def basketball(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/basketball.html")
