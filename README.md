# super-duper-phone-goggles
A RESTful API using Python/Django to manage phone call states.

The API has two main functions:

1. Capture real-time phone call events from an external system, "System B", and store them in a database.
2. Provide access to comprehensive call history for a given phone number.

**Part 1 - Event Processing:**

Implement an API endpoint to process events for the following attributes:
- event_id: Unique identifier for the event.
- call_id: Unique identifier for the call.
- event: Values can be INITIATE, ANSWER, or DISCONNECT.
- calling_number: Calling phone number in E.164 format.
- called_number: Called phone number in E.164 format.
- created_at: Date of the event.

**Part 2 - Call History:**

Expose call history for a given phone number.
Each record includes:
Call time.
Counterparty phone number.
Call status (Completed Inbound, Missed Inbound, Completed Outbound, Missed Outbound).
Duration in seconds for completed calls.
