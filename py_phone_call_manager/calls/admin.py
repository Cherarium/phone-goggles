from django.contrib import admin
from django.utils import timezone
from .models import CallEvent

# Admin configuration for the CallEvent model.
class CallEventAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('call_id', 'event', 'calling_number', 'called_number', 'created_at', 'get_call_status', 'get_duration')
    # Filters for the admin list view    
    list_filter = ('event',)
    # Search fields for the admin list view
    search_fields = ('call_id', 'calling_number', 'called_number')

    def get_call_status(self, obj): 
    # Returns the call status based on the event type.
        
        if obj.event == 'INITIATE':
            return 'Missed Outbound'
        elif obj.event == 'ANSWER':
            return 'Completed Inbound'
        elif obj.event == 'DISCONNECT':
            return 'Completed Outbound'
        else:
            return 'Unknown'

    # Customizes the display name for the 'get_call_status' function
    get_call_status.short_description = 'Call Status'

    def get_duration(self, obj):
    #  Returns the duration of the call in seconds for completed calls.
    # Logic to calculate the duration of the call
        if obj.event == 'DISCONNECT':
            delta = timezone.now() - obj.created_at
            return int(delta.total_seconds())
        else:
            return None
    # Customizes the display name for the 'get_duration' function
    get_duration.short_description = 'Duration (seconds)'

# Register the CallEvent model with the custom admin configuration
admin.site.register(CallEvent, CallEventAdmin)