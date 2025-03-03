import requests
from django.http import JsonResponse


def send_sms(request):
    url = "https://rest.nexmo.com/sms/json"
    payload = {
        "from": "Vonage APIs",
        "text": "A text message sent using the Vonage SMS API",
        "to": "254791869732",
        "api_key": "0f4031b8",
        "api_secret": "Q1bDcP2t6Lof5VnF"
    }

    response = requests.post(url, data=payload)

    return JsonResponse(response.json())  # Return response as JSON
