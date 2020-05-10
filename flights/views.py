from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Flight, Passenger
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request,"flights/index.html",context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk = flight_id)
    except Flight.DoesNotExists:
        raise Http404("Flight does not exist.")

    context = {
        "flight":flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html", context )

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)

    except Passenger.DoesNotExists:
        return render(request, "flights/error.html", {"message": "No Passenger. "})

    except Flight.DoesNotExists:
        return render(request, "flights/error.html",{"message": "No Flight"})

    except KeyError:
        return render(request,"flights/error.html", {"message": "No Selection. "})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight",args=(flight_id,)))
