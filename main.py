from extract import extract_weather, extract_crypto
from transform import transform_weather, transform_crypto
from load import load_to_postgres

def run_pipeline():
    print("Starting ETL pipeline...")

    # Extract
    weather_raw = extract_weather()
    crypto_raw = extract_crypto()

    # Transform
    weather_clean = transform_weather(weather_raw)
    crypto_clean = transform_crypto(crypto_raw)

    # Load
    load_to_postgres(weather_clean, crypto_clean)

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()