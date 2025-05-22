from django.shortcuts import render

def home(request):
    return render(request, 'lfphome3.html')

def about(request):
    return render(request, 'lfpabout.html')

def menu(request):
    return render(request, 'lfpfixedmenu.html')

def sustainability(request):
    return render(request, 'sustainability.html')   

def contact(request):
    return render(request, 'contact.html')

def references(request):
    return render(request, 'references.html')

def reservations(request):
    return render(request, 'reservation.html')