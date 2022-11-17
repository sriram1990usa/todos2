from django.urls import path
#from app.views import home, signup, login, add_todo, delete_todo, change_todo, signout 

from app.views.home import home 
from app.views.signup import signup 
from app.views.login import login 
from app.views.add_todo import add_todo 
from app.views.delete_todo import delete_todo 
from app.views.change_todo import change_todo
from app.views.signout import signout 

urlpatterns = [
   path('' , home , name='home' ),   
   path('signup/' , signup ), 
   path('login/' ,login  , name='login'), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('change-status/<int:id>/<str:status>' , change_todo ), 
   path('logout/' , signout )
]