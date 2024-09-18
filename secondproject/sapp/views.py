from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')
    # return HttpResponse("<h1>Home page</h1>")


def data(request):
    return render(request, 'data.html')
    # return HttpResponse("<h1>Data page</h1>")


def test(request):
    return render(request, 'test.html')
    # return HttpResponse("<h1>Test page</h1>")
