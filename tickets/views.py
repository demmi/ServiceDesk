from django.http import HttpResponse
from django.shortcuts import render


def TicketsView(response):
    return render(response, 'tickets/index.html')
