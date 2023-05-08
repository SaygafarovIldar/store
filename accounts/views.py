from django.shortcuts import render, HttpResponse

# Create your views here.


def login_view(request):
    return HttpResponse("login page")


def registration_view(request):
    return HttpResponse("registration page")
