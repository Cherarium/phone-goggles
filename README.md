# super-duper-phone-goggles
This repository hosts a RESTful API built with Python and Django, designed to efficiently manage phone call states.

## Features
1. Capture real-time phone call events from an external system and store them.
2. Provide a detailed call history for any given phone number.
   
## Part 1 - Event Processing
Implement an API endpoint to handle the following event attributes:

- event_id: Unique identifier for the event.
- call_id: Unique identifier for the call.
- event: Values can be INITIATE, ANSWER, or DISCONNECT.
- calling_number: Calling phone number in E.164 format.
- called_number: Called phone number in E.164 format.
- created_at: Date of the event.

**Event Behaviors:**
**"INITIATE" and "ANSWER" Events:**
- These events are occasionally marked with a dash `-`, indicating their immediate nature. This possibly indicates calls that have not yet been completed. They occur promptly, reflecting the initiation and answering of phone calls.

**"DISCONNECT" Events:**
- In contrast, `DISCONNECT` events are distinguished by a set amount of seconds until a call is terminated. When a call is `DISCONNECTED`, you calculate the duration by subtracting the `created_at` timestamp of the `DISCONNECT` event from the `created_at` timestamp of the `INITIATE` event.

**Interpreting `-` Duration in Ongoing Calls:**
- If you're seeing `-` for duration in `initiate` and `answer` events, it might indicate that these calls are still ongoing or have not yet been completed at the time the test data was generated.

**Real-World Insight:**
In a real-world scenario, the duration field would primarily be meaningful for `DISCONNECT` events. This is when a call reaches its conclusion, providing the complete information needed to calculate the duration of the call.


## Part 2 - Call History
Expose the call history for a phone number, including:

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

  **Setup**
1. Clone the repository:
```
git clone https://github.com/Cherarium/super-duper-phone-goggles
cd super-duper-phone-goggles
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
Endpoint: http://127.0.0.1:8000/admin/calls/callevent/
![image](https://github.com/Cherarium/super-duper-phone-goggles/assets/55898764/ecc16a3f-3342-41bf-949a-d846b83bea29)

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
