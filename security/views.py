
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import uuid

# Create your views here.


def demoUser(request):
    uuidstr = str(uuid.uuid4())
    pwuuidstr = str(uuid.uuid4())
    userobj = User.objects.create_user(username=uuidstr, password=pwuuidstr)
    userobj.save()
    user2 = authenticate(username=uuidstr, password=pwuuidstr)
    if user2 is not None:
        login(request, user2)
        return redirect('/')