import json
import boto3

def send_email(subject, body, sender, recipient):
    ses_client = boto3.client('ses', region_name='us-east-1')
    response = ses_client.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [recipient]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )
    return response

def lambda_handler(event, context):
    # TODO implement
    try:
        # Replace the following with your own sender and recipient email addresses.
        sender_email = 'rehman.liaqat@netsoltech.com'
        recipient_email = 'rehman.liaqat@netsoltech.com'
        subject = 'Temperature exceed Alert!'
        body = 'This is an alert email sent from AWS Lambda using Amazon SES.'

        response = send_email(subject, body, sender_email, recipient_email)

        return {
            'statusCode': 200,
            'body': json.dumps('Email Alert sent successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error sending email: {}'.format(str(e)))
        }
