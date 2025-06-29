from django.shortcuts import render
from reference.models import Listing

def home(request):
    return render(request, 'lfphome3.html')

def about(request):
    return render(request, 'lfpabout.html')

def menu(request):
    return render(request, 'newmenu3.html')

def sustainability(request):
    return render(request, 'sustainability.html')   

def contact(request):
    return render(request, 'contact.html')

def references(request):
    listings = Listing.objects.all()
    return render(request, 'ref.html', {'listings': listings})

def reservations(request):
    return render(request, 'reservation.html')

    #