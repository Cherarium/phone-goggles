from rest_framework import serializers
from .models import CallEvent

class CallEventSerializer(serializers.ModelSerializer):
    # Serializer for the CallEvent model.
    class Meta:
        # Meta class to define the model and fields for serialization.
        model = CallEvent
        fields = ['event_id', 'call_id', 'event', 'calling_number', 'called_number', 'created_at']
        # Specify the fields to include in the serialized representation
