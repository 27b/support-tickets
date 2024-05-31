from django.db import models
from django.contrib.auth.models import User

from common.models import TimeStampModelMixin


class Ticket(TimeStampModelMixin):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='comments', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
