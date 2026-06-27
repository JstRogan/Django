from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "sport/home.html")


def football(request: HttpRequest) -> HttpResponse:
    return render(request, "sport/football.html")


def hockey(request: HttpRequest) -> HttpResponse:
    return render(request, "sport/hockey.html")


def basketball(request: HttpRequest) -> HttpResponse:
    return render(request, "sport/basketball.html")
