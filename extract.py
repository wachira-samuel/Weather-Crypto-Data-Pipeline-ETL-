import requests
from config import WEATHER_API_KEY

def extract_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    }

def extract_crypto():
    url = f"https://api.binance.com/api/v3/ticker/price?"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return {
        "symbol": data["symbol"],
        "price": float(data["price"])
    }
symbol= ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOGEUSDT"]