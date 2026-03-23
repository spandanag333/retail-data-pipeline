# End-to-End Data Engineering Pipeline (API to SQLite)

🚀 **Project Level:** Level 1 (Foundational Data Engineering Pipeline)

---

## 📖 Overview

This project demonstrates a complete end-to-end data engineering pipeline that ingests product data from an external API, transforms it into a structured format, and loads it into a relational database for analytical querying.

---

## 🎯 Objective

To design and implement a scalable data pipeline that:
- Extracts data from an external API  
- Transforms semi-structured JSON into structured data  
- Loads the processed data into a database  
- Enables SQL-based analysis for insights  

---

## 🏗️ Architecture


API → Raw JSON → Pandas Transformation → CSV → SQLite → SQL Queries


---

## ⚙️ Features

- API-based data ingestion using Python  
- Data transformation and cleaning using Pandas  
- Storage of processed data in SQLite database  
- SQL-based querying for analysis  
- Basic logging and error handling  

---

## 🛠️ Tech Stack

- **Programming:** Python  
- **Data Processing:** Pandas  
- **Database:** SQLite  
- **Data Source:** REST API  

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the pipeline:
  ```bash
   python scripts/run_pipeline.py
```
---
## 📊 Sample Output
SQL Query

```sql
SELECT category, AVG(price) as avg_price 
FROM products 
GROUP BY category;
```

📸
![SQL Output](output/sql_query_output.png)

---
## 📌 Key Learnings
- Built a batch data ingestion pipeline using an external API
- Transformed semi-structured JSON data into structured format
- Applied data cleaning and transformation using Pandas
- Loaded processed data into a relational database for querying
- Gained hands-on experience with end-to-end data pipeline design 
---
## 🔄 Future Improvements
- Integrate cloud storage (Azure Data Lake / AWS S3)
- Replace SQLite with production-grade databases (MySQL / Snowflake)
- Implement pipeline scheduling (Airflow / Cron)
- Add robust data validation and monitoring
- Introduce configuration-driven pipeline design



