from django.db import models


class TimeStampModelMixin(models.Model):
    """Implement created_at and udated_at methods."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
