import json
import boto3

def lambda_handler(event, context):
   # Create an SNS client
    sns = boto3.client('sns')
    records = event['Records']
    booking_detail=json.loads(records[len(records)-1]['body'])
    # set topic ARN
    arn_topic = 'arn:aws:sns:us-east-1:708645370762:sendBookingToEmail'
    print(json.loads(booking_detail))
    booking_detail=json.loads(booking_detail)
    
    message = """
        New Booking !!
    
        First Name: {} 
        SurName: {} 
        Email: {}
        Phone: {}
        Arrival Date: {}
        Total Nights: {}
        Total Guests: {}
        Notes: {}
        """.format(booking_detail["firstName"], booking_detail["surName"],booking_detail["email"], booking_detail["phone"], booking_detail["arrivalDate"], booking_detail["numOfNights"], booking_detail["numOfGuests"], booking_detail["notes"]) 

    # send message to sns
    response = sns.publish(
        TopicArn=arn_topic,
        Message=message
    )
    
    # Print the response
    print(response['MessageId'])
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notificatio sent to Manager')
    }
