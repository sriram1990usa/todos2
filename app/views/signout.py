from django.shortcuts import render , redirect
from django.contrib.auth import login as loginUser , logout

def signout(request):
    logout(request)
    return redirect('login')