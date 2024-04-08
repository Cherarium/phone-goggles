# phone-goggles
This repository hosts a RESTful API built with Python and Django, designed to efficiently manage phone call states.

Instead of relying on traditional databases like PostgreSQL or SQLite, this app utilizes Python scripts to generate random data.

The data used for testing and populating the API endpoints is randomly generated using Python scripts. 

This approach offers several advantages:

**1. Flexibility and Speed:**
- Python scripts allow for quick and flexible data generation without the need to set up and maintain a separate database system.
- Changes to the data schema or structure can be easily accommodated by modifying the Python scripts.

**2. Isolation and Independence:**
- Test data generation is independent of external dependencies, reducing the complexity of setting up testing environments.
- Developers can work in isolated environments without worrying about the state of a shared database.

**3. Reduced Overhead and Dependencies:**
- Eliminates the need for managing and maintaining additional database instances solely for testing purposes.
- Developers can focus more on writing and testing code, rather than managing databases.

## **Features**
1. Capture real-time phone call events from an external system and store them.
2. Provide a detailed call history for any given phone number.
   
## Part 1 - Event Processing
Implements an API endpoint to handle the following event attributes:

- event_id: Unique identifier for the event.
- call_id: Unique identifier for the call.
- event: Values can be INITIATE, ANSWER, or DISCONNECT.
- calling_number: Calling phone number in E.164 format.
- called_number: Called phone number in E.164 format.
- created_at: Date of the event.

**Event Behaviors:**
**"INITIATE" and "ANSWER" Events:**
- These events are occasionally marked with a dash `-`, indicating their immediate nature. This possibly indicates calls that have not yet been completed.

**"DISCONNECT" Events:**
- In contrast, `DISCONNECT` events are distinguished by a set amount of seconds until a call is terminated. When a call is `DISCONNECTED`, you calculate the duration by subtracting the `created_at` timestamp of the `DISCONNECT` event from the `created_at` timestamp of the `INITIATE` event.

**Interpreting `-` Duration in Ongoing Calls:**
- If you're seeing `-` for duration in `initiate` and `answer` events, it might indicate that these calls are still ongoing or have not yet been completed at the time the test data was generated.

**Real-World Insight:**
In a real-world scenario, the duration field would primarily be meaningful for `DISCONNECT` events. This is when a call reaches its conclusion, providing the complete information needed to calculate the duration of the call.


## Part 2 - Call History
Exposes the call history for a phone number, including:

- Call time.
- Counterparty phone number.
- Call status (Completed Inbound, Missed Inbound, Completed Outbound, Missed Outbound).
- Duration in seconds for completed calls.

## Installation
**Requirements**
- Python
- Django
- pylance
- Faker
- Djangorestframework

## **Setup**
1. Clone the repository:
```
git clone https://github.com/Cherarium/phone-goggles
cd py_phone_call_manager
```
2. Create and activate a virtual environment:
```
python3 -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
3. Install dependencies:
```
python -m pip install Django
pip install pylance Faker djangorestframework
```

## Usage
Endpoints

- Event Processing:
  - Endpoint: /process-events/
  - Attributes: event_id, call_id, event, calling_number, called_number, created_at.
- Call History:
  - Endpoint: /call-history/<input_phone_number>/

**Authentication**
The API uses Token Authentication. To create a superuser account:
```
python manage.py createsuperuser
```
Follow the prompts to set a username and password.

## Accessing Call History
![image](https://github.com/Cherarium/super-duper-phone-goggles/assets/55898764/ecc16a3f-3342-41bf-949a-d846b83bea29)

Django Admin CallEvent Interface: http://127.0.0.1:8000/admin/calls/callevent/


Example request: 
```
GET /call-history/+1234567890/
```
Example Response:
```
[
  {
    "call_time": "2024-04-01T12:00:00Z",
    "counterparty_number": "+9876543210",
    "call_status": "Completed Outbound",
    "duration": 120
  },
  {
    "call_time": "2024-04-02T10:00:00Z",
    "counterparty_number": "+1112223333",
    "call_status": "Missed Inbound",
    "duration": null
  }
]
```
**NOTE:**
 
**Clarification on Generated Data Source:**

The provided examples for requests/responses are based on data generated from a Python script `(create_test_data.py)` rather than a traditional database.

In this context, the expected outcomes may differ from standard database-driven results.

**Expected Outcome with Database Backend:**

If the application were to utilize a backend database such as SQLite or PostgreSQL, the examples provided (above) would align with the expected responses noted.

And, the endpoints would continue to return the defined JSON structures as demonstrated (in the examples). 


## Error Handling

**HTTP Status Codes**
- 200 OK: Successful request.
- 400 Bad Request: Invalid request parameters.
- 401 Unauthorized: Missing or invalid authentication token.
- 404 Not Found: Resource not found.
 
**Error Responses**
- Error responses will be in JSON format, providing details about the error.

## Data Generation & Deployment
To generate test data, run:
```
python create_test_data.py
```
This script uses the faker library to create random phone call events.
The generated data will be visible in the Django admin portal.

**Deployment Steps**

Set environment variables.
Start the development server:
```
python manage.py runserver
```
The API will be accessible at: http://127.0.0.1:8000/admin/ after logging in with your superuser credentials.

## References
Django Documentation: https://docs.djangoproject.com/en/stable/

E.164 Format Specification: https://en.wikipedia.org/wiki/E.164


## CODE ANALYSIS
**create_test_data.py**

This script creates random test data for the `CallEvent` model, simulating various phone call scenarios for testing the API.

```python
import os
import random
import django
import uuid

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'py_phone_call_manager.settings')
django.setup()

# Import the CallEvent model from the calls app
from calls.models import CallEvent

# Import Faker for generating fake data
from faker import Faker

# Initialize Faker
fake = Faker()

# Function to create test data
def create_test_data():
    for _ in range(50):  # Create 50 random call events for testing
        event = random.choice(['INITIATE', 'ANSWER', 'DISCONNECT'])  # Choose a random event type
        calling_number = fake.phone_number()  # Generate a random phone number for caller
        called_number = fake.phone_number()  # Generate a random phone number for callee
        created_at = fake.date_time_this_year()  # Generate a random date-time within the current year
        call_id = str(uuid.uuid4())  # Generate a unique UUID for call_id
        event_id = str(uuid.uuid4())  # Generate a unique UUID for event_id

        # Generate a random duration for all events
        duration = random.randint(1, 30)  # Random duration between 1 and 30 seconds

        # Create a new CallEvent object with the generated data
        CallEvent.objects.create(
            event_id=event_id,
            call_id=call_id,
            event=event,
            calling_number=calling_number,
            called_number=called_number,
            created_at=created_at,
            duration=duration  # Assign the random duration
        )

if __name__ == '__main__':
    create_test_data()
    print("Test data created successfully.")
```

**models.py**

This script defines the structure and characteristics of the data stored for each phone call event in the API. 

It ensures that each call event has a unique identifier, captures relevant information such as event type, phone numbers, timestamps, and duration (if available). 

```python
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
```

**calculate_call_history.py**

`calculate_call_history.py` complements `create_test_data.py` by analyzing `CallEvent` instances in the API. 

It computes call statuses ('Completed', 'Missed Inbound', 'Missed Outbound', 'Initiated') and durations, offering insights into the API's functionality. 

And together with `create_test_data.py`, it forms a cycle for generating test data and extracting metrics, aiding in API testing. 

```python
from calls.models import CallEvent
from datetime import timedelta

def calculate_call_status(events):
    
    # Determines call status based on 'INITIATE', 'ANSWER', 'DISCONNECT' events.
    # Args: events (dict): Dictionary of call event timestamps.
    # Returns: str: Call status ('Completed', 'Missed Inbound', 'Missed Outbound', 'Initiated', 'Unknown').

    if 'INITIATE' in events and 'ANSWER' in events and 'DISCONNECT' in events:
        return 'Completed'
    elif 'INITIATE' in events and 'ANSWER' in events and 'DISCONNECT' not in events:
        return 'Missed Inbound'
    elif 'INITIATE' in events and 'ANSWER' not in events and 'DISCONNECT' in events:
        return 'Missed Outbound'
    elif 'INITIATE' in events and 'ANSWER' not in events and 'DISCONNECT' not in events:
        return 'Initiated'
    else:
        return 'Unknown'

def calculate_duration(events):
    
    # Calculates call duration from 'INITIATE', 'ANSWER', 'DISCONNECT' timestamps.
    # Args: events (dict): Dictionary of call event timestamps.    
    # Returns: int: Call duration in seconds, or None if timestamps are missing.

    initiate_time = events.get('INITIATE')
    answer_time = events.get('ANSWER')
    disconnect_time = events.get('DISCONNECT')

    if initiate_time and answer_time and disconnect_time:
        duration = disconnect_time - answer_time
        return duration.total_seconds()
    else:
        return None

def process_call_history():
    
   # Processes CallEvent data to compute call status and duration.
   
    all_calls = CallEvent.objects.all().order_by('created_at')

    for call in all_calls:
        events = {
            'INITIATE': None,
            'ANSWER': None,
            'DISCONNECT': None
        }

        if call.event == 'INITIATE':
            events['INITIATE'] = call.created_at
        elif call.event == 'ANSWER':
            events['ANSWER'] = call.created_at
        elif call.event == 'DISCONNECT':
            events['DISCONNECT'] = call.created_at

        call_status = calculate_call_status(events)
        duration_seconds = calculate_duration(events)

        # Prints call details: time, counterparty number, status, duration.
        print("Call Time:", call.created_at)
        print("Counterparty Phone Number:", call.called_number)  # Assuming called_number is the second party
        print("Call Status:", call_status)
        print("Duration (seconds):", duration_seconds)
        print("---------------------------------------")

if __name__ == '__main__':
    process_call_history()
```


**admin.py**

This script controls the Django admin interface for the `CallEvent` model.

It specifies the fields to display, adds filters and search functionality, and provides custom methods to calculate the call status and duration for each `CallEvent`

```python
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
```
