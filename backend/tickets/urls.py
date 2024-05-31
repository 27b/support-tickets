from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.IsOnlineAPIView.as_view()),
    path("tickets", views.TicketListCreateAPIView.as_view()),
    path("tickets/<int:pk>", views.TicketRetrieveUpdateDestroyAPIView.as_view())
]