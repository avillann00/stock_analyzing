# import required modules
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse

# function that handles registering users
def register(request):
    # if the page sends back a response
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('about'))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
