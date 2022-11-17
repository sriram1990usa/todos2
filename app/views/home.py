from django.shortcuts import render , redirect
from django.contrib.auth import login as loginUser
from app.forms import TODOForm
from app.models.todo import TODO
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})

