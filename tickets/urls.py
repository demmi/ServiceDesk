from django.urls import path, include

from tickets.views import TicketsView

urlpatterns = [
    path('', TicketsView)
]
