# Weather API Assessment

We are going to leverage the OpenWeather API Free Tier account which enables us to get weather information per city.

## Project Setup

Project Requirements:
- Python 3.7
- pip3
- Pipenv
- Postman

1. pipenv install
2. pipenv shell
3. Run `cd src/weather_api`
4. Run `python manage.py runserver`
5. Submit a GET Request on Postman to `http://localhost:8000/api/weather` with Params `city` of any City value.
