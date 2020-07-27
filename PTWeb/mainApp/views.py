from django.shortcuts import render


def home(request):
    return render(request, 'mainApp/home.html')


def contact(request):
    return render(request, 'mainApp/contact.html')


def offer(request):
    return render(request, 'mainApp/offer.html')