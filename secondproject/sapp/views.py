from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    data = {
        'caption': "Parrot Django"
    }
    return render(request, 'sapp/home.html', data)
     # return HttpResponse("<h1>Home page</h1>")

def data(request):
    return render(request, 'sapp/data.html')
    # return HttpResponse("<h1>Data page</h1>")

def uses(request):
    return render(request, 'sapp/uses.html')
    # return HttpResponse("<h1>Test page</h1>")

def compare(request):
    return render(request, 'sapp/compare.html')

def apps(request):
    return render(request, 'sapp/apps.html')
