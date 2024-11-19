from django.shortcuts import redirect, render
from . models import Menu, MenuType, Chefs, Table, Reservation
from .forms import ReservationForm
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def home(request):
     menus = Menu.objects.all()
     menu_types = MenuType.objects.all()
     chef = Chefs.objects.all()
     
     context = {
        'menus': menus,
        'menu_types': menu_types,
        'chef' :chef,
    }
     return render(request, 'index.html', context)



def book(request):
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(request, "Your reservation was successful!")
            return redirect('home')
        else:
            messages.error(request, "There was an error with your reservation. Please try again.")
    else:
        reservation_form = ReservationForm()
    
    context = {'reservation_form': reservation_form}
    return render(request, 'booking.html', context)

def menu(request):
     menus = Menu.objects.all()
     menu_types = MenuType.objects.all()
     
     context = {
        'menus': menus,
        'menu_types': menu_types,
    }
     
     return render(request, 'menu.html', context)