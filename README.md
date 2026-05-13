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



Tehcnologies Used

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

Weather Data Extraction

The weather extraction function fetches live weather information using the OpenWeatherMap API.
