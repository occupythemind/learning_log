from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed

def register(request):
    '''create a new user'''
    if request.method != 'POST':
        # display a blank form
        form = UserCreationForm()
    else:
        # data is submitted, methos is post
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    context={'form':form}
    return render(request, 'registration/register.html', context)

@login_required
def log_out(request):
    '''Just return the logout page'''
    return render(request, 'registration/loggedout.html')