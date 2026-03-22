# # End-to-End Data Engineering Pipeline (API to SQLite)
🚀 Project Level: Level 1 (Foundational Data Engineering Pipeline)

## Overview
Built an end-to-end data pipeline to ingest, transform, and store product data from an external API.

## 🎯 Objective

To simulate a real-world data engineering pipeline including ingestion, transformation, and storage for downstream analytics.

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

## 📊 Sample Query Output

| category | avg_price |
|----------|----------|
| beauty   | 45.2     |



