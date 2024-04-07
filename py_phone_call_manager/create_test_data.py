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