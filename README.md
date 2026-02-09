# Data Engineering Foundations

This repository contains a 12-week guided introduction to Data Engineering for beginners with no technical background.

It's curriculum is designed to give a **strong foundation** in Data Engineering concepts and tools, with a focus on **practical experience** through weekly hands-on exercises. Each week builds on the previous one, gradually increasing complexity, and by the end, anyone should be comfortable designing, implementing, and maintaining basic data pipelines.

## Structure
Each folder represents one week of learning and contains:
- Concepts and explanations
- Diagrams or examples
- Assignments (where applicable)

## Goal
By the end of this program, the student should understand how data pipelines
are designed, built, and maintained using industry-standard tools.











---
---
---

---

## Week 3 — Python for Data Manipulation (Advanced Basics)

### Topics:

- Lists and Dictionaries in-depth
    - List comprehensions
    - Dictionary key/value manipulation
- File handling (Reading & Writing)
    - Working with CSV and JSON
- Error handling with `try` / `except`

### Hands-On:

- Write a script to read a JSON file, manipulate the data, and output it into a CSV
- Create functions to handle missing or malformed data in CSV files

---

## Week 4 — Introduction to SQL

### Topics:

- What is SQL? Why is it used in Data Engineering?
- Basic SQL Syntax: SELECT, WHERE, ORDER BY, LIMIT
- Understanding Databases and Tables
- Introduction to SQLite (or PostgreSQL)

### Hands-On:

- Create a simple table in SQLite/PostgreSQL
- Insert, update, and query data using SELECT and WHERE
- Run basic queries like finding records with specific conditions (e.g., all records where price > 100)

---

## Week 5 — SQL Intermediate

### Topics:

- GROUP BY, HAVING, and Aggregations (SUM, COUNT, AVG)
- JOINs (INNER JOIN, LEFT JOIN)
- Subqueries and Nested SELECTs

### Hands-On:

- Write queries to aggregate sales data by product category
- Write queries to join two tables (e.g., orders and customers)
- Use GROUP BY to get monthly statistics from a dataset

---

## Week 6 — Introduction to Data Engineering Pipelines

### Topics:

- What is an ETL pipeline?
- Introduction to ELT vs ETL
- Data Sources, Staging, Processing, and Target systems
- Why Data Quality and Monitoring Matter

### Hands-On:

- Create a simple Python script to act as an ETL pipeline:
    - Extract data from a CSV
    - Transform it by cleaning and aggregating
    - Load it into a SQLite/PostgreSQL table

---

## Week 7 — Introduction to PySpark

### Topics:

- What is PySpark? Why use it?
- Understanding Distributed Computing
- Spark Architecture (Driver, Executors, Jobs)
- PySpark vs Pandas

### Hands-On:

- Install Spark and run basic commands in PySpark
- Load data into a Spark DataFrame
- Perform basic transformations (filtering, adding columns)

---

## Week 8 — PySpark Basics

### Topics:

- Spark DataFrames and RDDs
- Transformations vs Actions
    - map(), filter(), reduce()
    - count(), collect(), show()
- Handling missing data in Spark

### Hands-On:

- Load a large CSV into Spark DataFrame
- Perform basic transformations on the DataFrame
- Write the transformed data back to disk in Parquet format

---

## Week 9 — Advanced PySpark

### Topics:

- Joins and Aggregations in PySpark
- Partitioning and Performance Optimization
- Spark SQL for querying DataFrames
- Caching and Persisting DataFrames for optimization

### Hands-On:

- Write a Spark script to join two large datasets and aggregate the data
- Experiment with partitioning and compare performance
- Cache a DataFrame for faster operations

---

## Week 10 — Introduction to Data Orchestration

### Topics:

- What is Data Orchestration? (Overview of NiFi or Airflow)
- Introduction to NiFi:
    - Processors, FlowFiles, and Connections
    - Building simple data flows in NiFi
- Why orchestration is critical to pipeline reliability
- Error handling and retries

### Hands-On:

- Build a simple NiFi pipeline that reads data from a file, processes it, and outputs to another file

---

## Week 11 — Building Real Data Pipelines

### Topics:

- Design a Complete Data Pipeline
    - From extraction to loading data into a target system (database or storage)
- Workflow Management: Scheduling and Dependencies
- Monitoring, Logging, and Troubleshooting Pipelines

### Hands-On:

- Create a real-time or batch pipeline using Python, SQL, and Spark (e.g., ingest and process event data)
- Use NiFi or Airflow to schedule and monitor the pipeline

---

## Week 12 — Capstone Project

### Goal:

- Build a **full end-to-end data pipeline** with real-world use cases.

### Topics:

- End-to-end pipeline architecture
- Integrating Python, SQL, Spark, and NiFi or Airflow
- Monitoring, alerting, and debugging pipelines

### Hands-On:

- Project: Create a pipeline that reads raw data from a file, processes it (e.g., clean, aggregate, enrich), and writes it to a target storage system (e.g., PostgreSQL, MinIO, or S3).
- Document the pipeline, including data flow, logic, and error handling.

---

### Final Assessment (End of Week 12):

- Present the project and walk through the architecture and the design decisions.
- Evaluate the candidate on:
    - Understanding of data flow and pipelines
    - Ability to manipulate data (SQL, Python, PySpark)
    - Debugging and troubleshooting
    - Use of orchestration tools

---

