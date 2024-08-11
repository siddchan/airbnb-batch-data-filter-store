import json

def lambda_handler(event, context):
    try:
        print('Event: ', event)
        print('context: ', context)
        print(event)
        message =  json.loads(event[0]['body'])
        print(message)
        if (message['startDate'] == message['endDate']):
            message = {}
        return {
            'message': message
        }
    except Exception as e:
        return {
            'Error message': str(e)
        }
