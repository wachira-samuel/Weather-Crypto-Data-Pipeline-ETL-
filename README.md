# Building a FinTech ETL Pipeline with Python and PostgreSQL

In modern fintech systems, data engineering plays a critical role in collecting, processing and storing real-time financial and market data. This project demonstrates how to build a lightweight ETL (Extract, Transform, Load) pipeline using Python, external APIs, and PostgreSQL.

The Pipeline extracts:
1. Weather data from OpenWeatherMap API
2. Cryptocurrency market prices from the Binance API

The processed data is then loaded into a PostgreSQL database for storage and anlysis.

Project Architecture

                +------------------+
                | External APIs    |
                |------------------|
                | OpenWeatherMap   |
                | Binance API      |
                +---------+--------+
                          |
                          v
                +------------------+
                | Extract Layer    |
                | extract.py       |
                +---------+--------+
                          |
                          v
                +------------------+
                | Transformation   |
                | JSON Processing  |
                +---------+--------+
                          |
                          v
                +------------------+
                | Load Layer       |
                | load.py          |
                +---------+--------+
                          |
                          v
                +------------------+
                | PostgreSQL DB    |
                +------------------+



Technologies Used

    Technology	   Purpose

    Python	       ETL scripting
    
    PostgreSQL	   Data storage
    
    SQLAlchemy	   Database connection and ORM support
    
    Pandas	       Data inspection and analysis
    
    Requests	     API communication
    
    Binance        API	Cryptocurrency market data
    
    OpenWeatherMap API	Weather data source

Extract Layer

The extraction process is responsible for collecting raw data from external APIs.

1. Weather Data Extraction

The weather extraction function fetches live weather information using the OpenWeatherMap API.
```
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
```

Key Features

1. Uses REST API requests

2. Handles HTTP errors using raise_for_status()

3. Parses JSON responses

4. Extracts structured weather metrics


Data Collected
1. City name

2. Temperature

3. Humidity

Cryptocurrency Data Extraction

The crypto extraction function retrieves real-time cryptocurrency prices from Binance.

  
  ```
  def extract_crypto():
    url = f"https://api.binance.com/api/v3/ticker/price?"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return {
        "symbol": data["symbol"],
        "price": float(data["price"])
    }

```

Supported Crypto Symbols

    ```
    symbol = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOGEUSDT"]

    ```

Key Features

1. Fetches live crypto prices.

2. Converts price values to float for analytics.

3. Supports multiple cryptocurrency trading pairs

Load Layer

The loading process stores transformed data into PostgreSQL tables.

Database Connection

SQLAlchemy is used to establish a PostgreSQL connection.

    ```
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    engine = create_engine(DATABASE_URL)

    ```

Benefits of SQLAlchemy

1. Simplifies database connectivity.

2. Supports secure parameterized queries.

3. Improves scalability and maintainability


Loading Weather Data

    ```
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
    ```

Loading Cryptocurrency Data

    ```
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
    ```
Data Validation

After loading, Pandas is used to verify inserted records.

Weather Table Validation
   
    ```
    weather_df = pd.read_sql("SELECT * FROM weather_data;", engine)
    print(weather_df)
    ```
    
Crypto Table Validation

    ```
    crypto_df = pd.read_sql("SELECT * FROM binance_data;", engine)
    print(crypto_df)

    ```

This enables quick inspection of:

1. Record counts
  
2. Data quality

3. Schema consistency


This ETL pipeline demonstrates several real-world fintech engineering concepts:

    FinTech Need	              Implementation
    Real-time market data      	Binance API integration
    Data reliability          	Error handling
    Secure database operations	Parameterized SQL
    Data analytics readiness	  Structured PostgreSQL storage
    Automation potential	      ETL modularization


