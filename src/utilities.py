import os
import boto3
import traceback

SES_CLIENT = boto3.client('ses')
SENDER_EMAIL = os.environ.get("sender_email", "")
RECEIVER_EMAIL = os.environ.get("receiver_email", "")


def send_email(receiver_address: str, sender_address: str,
               message: str) -> bool:
    try:
        if SENDER_EMAIL is "" or RECEIVER_EMAIL is "":
            print("Either Sender or Receiver email is empty")
            print("Sender email: ", SENDER_EMAIL)
            print("Recevier email : ", RECEIVER_EMAIL)
            return False
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
                            <strong>
                                Received from : {receiver_address}<br>
                                Sender Address: {sender_address} <br>
                                <br>
                                Message: {message}
                                <br><br>
                            </strong>
                        </html>
                        ''',
                    },
                },
                'Subject': {
                    'Charset':
                    'UTF-8',
                    'Data':
                    f'Message from: {sender_address} in number {receiver_address}',
                },
            },
            Source=SENDER_EMAIL,
        )
        print("Response from SES : ", response)
        return True
    except Exception as e:
        traceback.format_exc()
        return False