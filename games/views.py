from django.shortcuts import render, redirect
from games.forms import EmailUserCreationForm


def home(request):
    return render(request, 'home.html')


def snake(request):
    return render(request, 'snake.html')


def paint(request):
    return render(request, 'paint.html')

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    #form.first_name.TextInput(attrs={'class': 'form-control',
     #                               'placeholder': 'your email *'})
    return render(request, "registration/register.html", {
        'form': form,
    })
