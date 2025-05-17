from django.shortcuts import render

def home(request):
    return render(request, 'lfphome2.html')