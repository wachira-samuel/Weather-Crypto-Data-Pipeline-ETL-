from sqlalchemy import create_engine, text
import pandas as pd


# Create connection string
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create engine
engine = create_engine(DATABASE_URL)



def load_to_postgres(weather, crypto):
    with engine.connect() as connection:

        # WEATHER INSERT
        connection.execute(
            text("""
                INSERT INTO weather_data (city, temperature, humidity)
                VALUES (:city, :temperature, :humidity)
            """),
            {
                "city": weather["city"],
                "temperature": weather["temperature"],
                "humidity": weather["humidity"]
            }
        )

        # CRYPTO INSERT
        connection.execute(
            text("""
                INSERT INTO crypto_data (symbol, price)
                VALUES (:symbol, :price)
            """),
            {
                "symbol": crypto["symbol"],
                "price": crypto["price"]
            }
        )

        connection.commit()

# Check weather_data table
print("WEATHER DATA")
weather_df = pd.read_sql("SELECT * FROM weather_data;", engine)
print(weather_df)
print(f"Total weather records: {len(weather_df)}\n")

# Check crypto_data table
print("=" * 60)
print("CRYPTO DATA")
crypto_df = pd.read_sql("SELECT * FROM binance_data;", engine)
print(crypto_df)
print(f"Total crypto records: {len(crypto_df)}\n")