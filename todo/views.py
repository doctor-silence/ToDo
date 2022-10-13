from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def signupuser(request):

    return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
