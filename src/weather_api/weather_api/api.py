import requests
from django.conf import settings
from django.http import JsonResponse


def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + settings.OPENWEATHER_API_KEY
    city = request.GET['city']

    r = requests.get(url.format(city)).json()

    if r['cod'] != 200:
        return JsonResponse({'message': 'Somemething went wrong', 'status': 'Error'})

    city_weather = {
        'city': city,
        'description': r['weather'][0]['description'],
        'avg_temp': r['main']['temp'],
        'min_temp': r['main']['temp_min'],
        'max_temp': r['main']['temp_max'],
        'humidity': r['main']['humidity'],
    }

    return JsonResponse(city_weather)
