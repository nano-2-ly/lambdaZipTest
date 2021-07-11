import bcrypt

def lambda_handler(event, context):
        
    _body = json.loads(event['body']) 
    return {
        'statusCode': 200,
        'body': bcrypt.hashpw("hello", bcrypt.gensalt())
    }

