from django.contrib.auth.models import User
from django.db import models


from rest_framework.serializers import ModelSerializer, ListField, HyperlinkedRelatedField

from .models import Ticket, Comment


class UserTicketSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(ModelSerializer):
    account = UserTicketSerializer(source="user", read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'account']


class TicketModelSerializer(ModelSerializer):
    account = UserTicketSerializer(source="user", read_only=True)
    comment = CommentSerializer(source="comments", read_only=True, many=True)

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'account', 'comment']