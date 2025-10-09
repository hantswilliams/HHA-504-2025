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

    if request_args and 'age' in request_args:
        response_age = request_args['age']
    else:
        response_age = 'You did not enter an age into the argument'

    if request_args and 'wbc' in request_args:
        response_wbc = request_args['wbc']
    else:
        response_wbc = 'You did not enter a wbc into the argument'

    age_in_10years = float(response_age) + 10 if response_age.isdigit() else 'N/A'

    wbc_abnormal_normal = 'abnormal' if response_wbc != 'N/A' and (float(response_wbc) < 4.0 or float(response_wbc) > 11.0) else 'normal'

    response = f"Response: First name: {response_firstname}; Last name: {response_lastname}; Age in 10 years: {age_in_10years}; WBC count is {wbc_abnormal_normal}"

    return response
