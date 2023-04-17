import json
import boto3

def lambda_handler(event, context):
    # Create an SNS client
    sqs = boto3.client('sqs')
    sqs_url="https://sqs.us-east-1.amazonaws.com/708645370762/booking-sqs"
    bookingDetail=event['body']
    
    message_json = json.dumps(bookingDetail)
    
    # send the message as json to sqs
    response = sqs.send_message(
        QueueUrl=sqs_url,
        MessageBody=message_json
    )
    
    # print message 
    print(response['MessageId'])
    
    # return response back to API
    return {
        'statusCode': 200,
        'body': json.dumps("Notification successfully sent to SQS")
    }
