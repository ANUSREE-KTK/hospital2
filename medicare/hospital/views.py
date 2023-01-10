from django.shortcuts import render

from .models import Departments,Doctors,Booking
from . import models
from .forms import BookingForm

# Create your views here.

def department(request):
    dict_dpt={
        'dept': Departments.objects.all()
    }
    return render(request,'department.html',dict_dpt)


def doctors(request):
    dict_docs ={
        'doctors' :Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmations.html')

    forms = BookingForm()
    dict_form={
        'form':forms
    }
    return render(request,'booking.html',dict_form) 


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')




