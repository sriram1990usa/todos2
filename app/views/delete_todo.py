from django.shortcuts import render , redirect
from django.contrib.auth import login as loginUser
from app.models.todo import TODO
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def delete_todo(request , id ):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('home')
