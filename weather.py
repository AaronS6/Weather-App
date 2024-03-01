import requests

api_key = ""


def get_weather(city, country):
    complete_url = "http://api.openweathermap.org/data/2.5/weather?" + f"q={city},{country}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return round(temperature)
    else:
        return None


