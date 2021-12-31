def hello_world(event, context):
    name = event['queryStringParameter']['name']
    name = "Hello--" + name 
    return {'status': 200, 'message': name}