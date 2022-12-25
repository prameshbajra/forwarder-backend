import json
from utilities import send_email


def lambda_handler(event, context):
    event_body = json.loads(event['body'])
    sender_address = event_body['sender_address']
    receiver_address = event_body['receiver_address']
    message = event_body['message']
    is_email_sent = send_email(sender_address=sender_address,
                               receiver_address=receiver_address,
                               message=message)
    return is_email_sent