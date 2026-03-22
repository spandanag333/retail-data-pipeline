# # End-to-End Data Engineering Pipeline (API to SQLite)
🚀 Project Level: Level 1 (Foundational Data Engineering Pipeline)

## Overview
Built an end-to-end data pipeline to ingest, transform, and store product data from an external API.

## 🎯 Objective

To build a scalable end-to-end data pipeline that ingests data from an external API, transforms it into a structured format, and loads it into a database for analytical querying.

## 🏗️ Architecture

API → Raw JSON → Pandas → CSV → SQLite → SQL Queries

## Features
- API-based data ingestion using Python
- Data transformation using Pandas
- Data storage in SQLite database
- SQL-based data analysis
- Logging and error handling

## Tech Stack
- Python
- Pandas
- SQL (SQLite)
- REST API

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run pipeline:
   python scripts/run_pipeline.py

## 📊 Sample Output

Example SQL Query:
SELECT category, AVG(price) as avg_price FROM products GROUP BY category;

Output:

| category | avg_price |
|----------|----------|
| beauty   | 45.2     |
| groceries| 23.1     |


## 🔄 Future Improvements

- Integrate with Azure Data Lake for cloud storage
- Replace SQLite with MySQL or Snowflake
- Implement scheduling using Airflow or Cron
- Add data validation and monitoring
