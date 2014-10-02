from django.contrib.auth.decorators import login_required
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
            return redirect("home.html")
    else:
        form = EmailUserCreationForm()

    #form.first_name.TextInput(attrs={'class': 'form-control',
     #                               'placeholder': 'your email *'})
    return render(request, "registration/register.html", {
        'form': form,
    })

def logout(request):
    return render(request, 'registration/logout.html')

@login_required
def profile(request):
    if not request.user.is_authenticated():
        return redirect("login")

    return render(request, 'registration/profile.html', {})