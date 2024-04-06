# super-duper-phone-goggles
This is a RESTful API using Python/Django to manage phone call states.

## The API has two main functions:

1. Capture real-time phone call events from an external system, and store them in a database.
2. Provide access to comprehensive call history for a given phone number.

**Part 1 - Event Processing:** 

Implement an API endpoint to process events for the following attributes:
- event_id: Unique identifier for the event.
- call_id: Unique identifier for the call.
- event: Values can be INITIATE, ANSWER, or DISCONNECT.
- calling_number: Calling phone number in E.164 format.
- called_number: Called phone number in E.164 format.
- created_at: Date of the event.

**Part 2 - Call History**

Expose call history for a given phone number.
Each record includes:
Call time.
Counterparty phone number.
Call status (Completed Inbound, Missed Inbound, Completed Outbound, Missed Outbound).
Duration in seconds for completed calls.

## **Installation**
```
Requirements:
- Python
- Django
- pylance
- Faker
- Djangorestframework
```
**Setup:**

Clone the repository: git clone https://github.com/Cherarium/super-duper-phone-goggles
- Navigate to the project directory: `cd super-duper-phone-goggles`
- Create a virtual environment: `python3 -m venv venv`

Activate the virtual environment:
- On Windows: `venv\Scripts\activate`
- On macOS/Linux: `source venv/bin/activate`
- Install dependencies: `python -m pip install Django`, `pip install pylance`, `pip install Faker` `pip install djangorestframework`

## **Usage:**

Endpoints:
Endpoint for processing phone call events.

Attributes:
- event_id
- call_id
- event
- calling_number
- called_number
- created_at.

Endpoint for accessing call history(s): `http://127.0.0.1:8000/admin/calls/callevent/`

![image](https://github.com/Cherarium/super-duper-phone-goggles/assets/55898764/59224218-e0ea-4598-add3-a112f5e25132)

**The API uses Token Authentication.**
To create a superuser account input:
```
python manage.py createsuperuser
```
Then follow the prompts to set a username and password.

## **Call History:**
Endpoint: /call-history/<input_phone_number>/
Attributes:
- call_time: Time of the call.
- counterparty_number: Counterparty phone number.
- call_status: Status of the call (Completed Inbound, Missed Inbound, Completed Outbound, Missed Outbound).
- duration: Duration in seconds for completed calls.

**Example:**
Expected Request: 
```
GET /call-history/+1234567890/
```
Expected Response: 
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
