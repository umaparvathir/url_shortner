import json
from api.url_shortner_api import lambda_handler

# If long_url is empty
def test_lambda_handler_fail_1():

    event = {}
    event['body'] = '{"long_url":""}'

    response = lambda_handler(event, context={})

    assert response["statusCode"] == 400
    assert response["body"] == '{"success": false, "message": "long_url value is not provided or empty", "code": 400}'

# If no event passed
def test_lambda_handler_fail_2():

    event = {}
    event['body'] = None

    response = lambda_handler(event, context={})
    
    assert response["statusCode"] == 500
    assert response["body"] == '{"success": false, "message": "Internal Server Error", "code": 500}'

def test_lambda_handler_success():

    event = {}
    event['body'] = '{"long_url":"https://www.gramann-ahrberg.de/filialen/filialen/"}'

    response = lambda_handler(event, context={})
    response_body = json.loads(response["body"])
    
    assert response["statusCode"] == 200
    assert response_body["success"] == True