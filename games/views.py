from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def snake(request):
    return render(request, 'snake.html')


def paint(request):
    return render(request, 'paint.html')