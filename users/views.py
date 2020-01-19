from django.shortcuts import render
from .models import *
# Create your views here.



def userlist(request):
    userlist = CustomUser.objects.all()
  
    # userlist = 'ss'
    return render(request, 'user_list.html' , {'userlist': userlist})
