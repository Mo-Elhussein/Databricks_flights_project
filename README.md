# ✈️ Databricks Flights Project

## 📌 Overview
This project demonstrates a **Data Engineering pipeline** implemented on **Databricks Lakehouse** using the **Medallion Architecture (Bronze, Silver, Gold layers)**.  
The goal is to process raw flight-related data (airports, flights, passengers, and bookings) and transform it into clean, analytics-ready datasets.

---

## 🏗️ Project Structure
```
DataBricks_flights_project/
│── BronzeLayer.dbc           # Bronze layer notebook (raw ingestion)
│── Dlt_Silver_Pipline.py     # Delta Live Tables pipeline for Silver layer
│── GoldDims.dbc              # Gold layer (dimensions)
│── GoldFact.dbc              # Gold layer (fact table)
│── Setup.dbc                 # Environment setup notebook
│── src_parameters.dbc        # Project parameters
│── rawdata/                  # Raw CSV files (incremental + full loads)
│     ├── dim_airports.csv
│     ├── dim_airports_increment.csv
│     ├── dim_flights.csv
│     ├── dim_flights_increment.csv
│     ├── dim_passengers.csv
│     ├── dim_passengers_increment.csv
│     ├── fact_bookings.csv
│     ├── fact_bookings_increment.csv
```

---

## ⚙️ Tech Stack
- **Databricks** (for Lakehouse & notebooks)
- **Delta Lake / Delta Live Tables (DLT)**
- **Apache Spark (PySpark)**
- **Python**
- **CSV (raw data source)**

---

## 🚀 Pipeline Flow
1. **Bronze Layer**: Ingest raw CSV files into Delta tables without transformations.
2. **Silver Layer**: Apply data cleaning, transformations, and incremental loads using **DLT**.
3. **Gold Layer**: Create **dimension tables** and **fact tables** ready for analytics (e.g., bookings, flights, airports, passengers).
4. **Analytics / BI**: Gold tables can be used for dashboards and reporting.

---

## ▶️ How to Run
1. Import the `.dbc` notebooks into your **Databricks Workspace**.
2. Upload the `rawdata/` folder to **DBFS** or mount it from external storage.
3. Run `Setup.dbc` to configure parameters & environment.
4. Run the pipeline in order:
   - `BronzeLayer.dbc`
   - `Dlt_Silver_Pipline.py`
   - `GoldDims.dbc` & `GoldFact.dbc`
5. Query Gold layer tables for insights.

---

## 📊 Example Use Cases
- Track flight bookings trends over time.
- Analyze passenger traffic by airport.
- Monitor flight volumes & incremental updates.
- Provide clean datasets for BI dashboards.

---


