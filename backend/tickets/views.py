from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from account.authentication import CustomTokenAuthentication
from common.permissions import IsOwnerOrSupport

from .models import Ticket
from .serializers import TicketModelSerializer


class IsOnlineAPIView(APIView):
    """
    Retrieve Online message.
    """
    def get(self, request):
        return Response({"status": "Online"})


class TicketListCreateAPIView(ListCreateAPIView):
    """
    Retrieve Ticket List.

    * Requires Token Authentication.
    * Only Authenticated users can create tickets.
    * Only Authenticated users can view their posts.
    """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketModelSerializer
    queryset = Ticket.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve Ticket.

    * Requires Token Authentication.
    * Only Ticket Owner or Support can modify view and modify the Ticket.
    """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsOwnerOrSupport]
    serializer_class = TicketModelSerializer
    queryset = Ticket.objects.all()
