import functions_framework

@functions_framework.http
def interpret_wbc(request):

    request_args = request.args

    if request_args and 'wbc' in request_args:
        response_wbc = request_args['wbc']
    else:
        response_wbc = 'You did not enter a wbc into the argument'

    try:
        wbc_value = float(response_wbc)
        if wbc_value < 4.0 or wbc_value > 11.0:
            wbc_interpretation = 'abnormal'
        else:
            wbc_interpretation = 'normal'
    except ValueError:
        wbc_interpretation = 'invalid input'

    response = wbc_interpretation
    
    return response