
WEATHER_API_KEY = "e584942171c98d6aa12d872ea04f3187"
#CITY = "Nairobi"
import os
from dotenv import load_dotenv

load_dotenv()

# News API key
NEWS_API_KEY = os.getenv("e584942171c98d6aa12d872ea04f3187")

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT")
}