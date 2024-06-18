# work/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Главная страница")

def data(request):
    return HttpResponse("Страница дата")

def test(request):
    return HttpResponse("Страница тест")
