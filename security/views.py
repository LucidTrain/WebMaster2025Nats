
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import uuid

# Create your views here.


def demologout(request):
    userobj = request.user
    userobj.delete()
    return redirect('/')


def demoUser(request):
    uuidstr = str(uuid.uuid4())
    pwuuidstr = str(uuid.uuid4())
    userobj = User.objects.create_user(username=uuidstr, password=pwuuidstr)
    userobj.save()
    user2 = authenticate(username=uuidstr, password=pwuuidstr)
    if user2 is not None:
        user2.first_name = "Demo"
        user2.last_name = "User"
        user2.email = uuidstr + "@example.com"
        user2.save()
        login(request, user2)
        return redirect('/')
