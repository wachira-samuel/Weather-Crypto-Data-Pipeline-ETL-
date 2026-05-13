def transform_weather(data):
    return {
        "city": data["city"],
        "temperature": round(data["temperature"], 2),
        "humidity": int(data["humidity"])
    }

def transform_crypto(data):
    return {
        "symbol": data["symbol"],
        "price": round(data["price"], 2)
    }