from django.shortcuts import redirect
from django.contrib.auth import login as loginUser
from app.models.todo import TODO
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')