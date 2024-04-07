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
