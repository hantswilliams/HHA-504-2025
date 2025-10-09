import functions_framework

@functions_framework.http
def hha504functiontest(request):

    request_args = request.args

    if request_args and 'first_name' in request_args:
        response_firstname = request_args['first_name']
    else:
        response_firstname = 'You did not enter a first_name into the argument'
    
    if request_args and 'last_name' in request_args:
        response_lastname = request_args['last_name']
    else:
        response_lastname = 'You did not enter a enter name into the argument'


    response = f"Response: First name: {response_firstname}; Last name: {response_lastname}"

    return response
