from decouple import config



BASE_URL = config('BASE_URL')

def global_variables(request):
    return {
        'BASE_URL': BASE_URL,
    }