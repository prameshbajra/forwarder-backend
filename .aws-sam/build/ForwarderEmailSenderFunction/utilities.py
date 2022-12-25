import os
from typing import Any
import boto3
import traceback

SES_CLIENT = boto3.client('ses')
SENDER_EMAIL = os.environ.get('sender_email', '')
RECEIVER_EMAIL = os.environ.get('receiver_email', '')


def send_email(device_details: Any, sender_address: str, message: str) -> bool:
    try:
        if SENDER_EMAIL == '' or RECEIVER_EMAIL == '':
            return False
        device_details_string = ''
        for key, value in device_details.items():
            device_details_string += f'<b>{key}</b> : <i>{value}</i> <br>'
        response = SES_CLIENT.send_email(
            Destination={
                'ToAddresses': [RECEIVER_EMAIL],
            },
            ReplyToAddresses=[RECEIVER_EMAIL],
            Message={
                'Body': {
                    'Html': {
                        'Charset':
                        'UTF-8',
                        'Data':
                        f'''
                        <html>
                            <h3>
                                Sender Address: {sender_address} <br>
                                <br>
                                Message: {message}
                            </h3>
                            <br><br>
                            <h3> Device Details </h3>
                            <hr>
                            {device_details_string}
                            <hr>
                        </html>
                        ''',
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': f'SMS from: {sender_address}',
                },
            },
            Source=SENDER_EMAIL,
        )
        print('Response from SES : ', response)
        return True
    except Exception as e:
        traceback.format_exc()
        return False