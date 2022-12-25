import json
from utilities import send_email


def lambda_handler(event, context):
    event_body = json.loads(event['body'])
    sender_address = event_body['sender_address']
    device_details = json.loads(event_body['device_details'])
    message = event_body['message']
    print(event_body)
    is_email_sent = send_email(sender_address=sender_address,
                               device_details=device_details,
                               message=message)
    return is_email_sent