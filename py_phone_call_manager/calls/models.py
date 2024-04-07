import uuid
from django.db import models

class CallEvent(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    call_id = models.CharField(max_length=255)
    event = models.CharField(max_length=20)
    calling_number = models.CharField(max_length=20)
    called_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(null=True, blank=True)  # Add the duration field

    def __str__(self):
        return f"CallEvent {self.call_id}"
