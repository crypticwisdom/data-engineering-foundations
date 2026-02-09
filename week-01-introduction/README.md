### Week 1 — Introduction to Data Engineering

### Objectives:

* Understand what Data Engineering is
* Understand how data flows in real systems
* Understand the Data Lifecycle
* Understand where tools fit (without using them)

---

### Topics:

### 1. What is Data Engineering?

**Data Engineering** is the design, development, and maintenance of systems that collect, move, store, and transform data so it can be reliably used by other systems, analysts, and decision-makers.

In simple terms, a Data Engineer builds the *infrastructure and pipelines* that allow data to flow from where it is generated to where it is consumed.

Data Engineers work with different forms of data such as:

* CSV files
* JSON files
* Parquet files
* Avro files
* SQL database dumps

These formats represent how data is stored and exchanged between systems.

---

#### What problem Data Engineering solves

Modern systems generate massive amounts of data from many sources. Without Data Engineering:

* Data would be scattered across systems
* Data would be slow to access
* Data would be unreliable or inconsistent
* Data would be unusable for analytics or machine learning

Data Engineering solves these problems by:

* Ensuring data is collected correctly
* Making data available at the right time
* Ensuring data quality and consistency
* Making data scalable and performant

---

#### Differences between:

**Data Engineering**

* Focuses on building data pipelines and infrastructure
* Ensures data is reliable, scalable, and available
* Works mostly behind the scenes

**Data Science**

* Focuses on extracting insights and building predictive models
* Uses data prepared by Data Engineers
* Works on statistics, machine learning, and experimentation

**Data Analysis**

* Focuses on querying and visualizing data
* Produces reports and dashboards
* Answers business questions using existing data

---

#### Roles & Responsibilities of a Data Engineer

A Data Engineer is responsible for:

* Inspecting incoming data for correctness and completeness
* Ensuring data is stored in optimized formats for downstream use cases (e.g., Parquet, Avro)
* Designing and building data pipelines
* Monitoring data pipelines for failures or delays
* Ensuring data is available, accurate, and performant for consumption

---

#### Real-world use cases

Data Engineering is used in many industries, including:

* **Banking transactions:** processing millions of financial records securely
* **E-commerce orders:** tracking purchases, payments, and deliveries
* **User activity tracking:** clicks, views, and interactions in applications
* **Telecom data:** call records, network usage, and performance metrics
* **Energy data:** sensor data from power grids and smart meters

---

### 2. Basic Data Concepts

#### What is data?

Data is a **raw fact** or observation that by itself may not have meaning until it is processed and interpreted.

Examples:

* A number: `100`
* A timestamp: `2025-01-01 10:00`
* A message: `"payment successful"`

---

#### Types of data

**Structured data**

* Organized into rows and columns
* Uses a predefined and strict schema
* Examples: CSV files, database tables, Parquet files

**Semi-structured data**

* Does not follow a rigid table structure
* Has a schema, but it is flexible
* Examples: JSON, XML

**Unstructured data**

* No predefined schema
* Harder to query directly
* Examples: images, videos, audio files, text documents

---

#### Common data formats (high level)

* **CSV:** simple text-based format, easy to read but limited
* **JSON:** flexible and human-readable, commonly used for APIs
* **Parquet:** columnar storage format optimized for analytics
* **Avro:** compact binary format with schema support, often used in streaming

*(Conceptual understanding only — no syntax or file handling yet)*

---

### 3. What is a Data Pipeline?

#### What is a pipeline?

A data pipeline is a system that ingests, moves, transforms, and stores data from one or more sources to a destination where it can be used.

---

#### Why pipelines exist

Pipelines exist to:

* Automate data movement
* Standardize data processing
* Ensure consistency and reliability
* Reduce manual handling of data

---

#### Types of pipelines

**Batch pipeline**

* Processes data in groups or batches
* Runs at scheduled intervals
* Example: Spark for batch processing

**Streaming pipeline**

* Processes data in real or near real time
* Handles continuous data flow
* Example: Kafka for streaming

**Micro-batch pipeline**

* A hybrid approach
* Processes small batches at very short intervals

---

#### Typical data flow

1. Raw data
2. Cleaned data
3. Aggregated data
4. Analytics and reporting

(Diagrams should be used here to visualize the flow.)

---

### 4. The Data Engineering Ecosystem (High Level)

#### Small data vs Big data

**Small data**

* Data that can fit on a single machine
* Tools for processing: Pandas, Python, SQL

**Big data**

* Data too large or complex for a single machine
* Tools for processing: Spark, Flink, NiFi, Kafka

---

#### Where tools fit conceptually

* **Data ingestion:** reading data from sources (files, databases, APIs)
* **Processing:** cleaning, transforming, and enriching data
* **Storage:** storing processed data for future use
* **Orchestration:** scheduling, monitoring, and managing pipelines (NiFi, Airflow)

---

#### Where data lives

* Databases: Organized row and column structure where data are stored. 
  * (MongoDB, PostgreSQL, MySQL, SQLite, CosmosDB, MSSQL, MariaDB)
  * NoSQL and SQL
  * These are OLTP (Online Transaction Processing)

* Data Warehouses: Is an optimized storage unit, used for storage and querying millions of data efficiently.
  * OLAP: Online Analytical Process

OLTP and OLAP.


Later we will discuss about: Object Storage, Data Lake, Lakehouse (Delta Lake, Iceberge, Hudi)
---

### 5. The Data Engineering Lifecycle

The Data Engineering lifecycle describes how data moves from creation to consumption.

1. **Generation:** data is produced by applications, sensors, or users
2. **Storage:** raw data is stored safely
3. **Ingestion:** data is collected into processing systems
4. **Transformation:** data is cleaned, structured, and enriched
5. **Serving:** data is made available for analytics, reporting, or applications


Generation -> Storage -> Ingest into Pipeline ->  Transform in Pipeline and Store -> Serving Downstream users
---

#### Undercurrents (cross-cutting concerns)

These concepts apply across the entire lifecycle:

* **Security:** protecting data from unauthorized access
* **Data Management:** organizing and governing data
* **Data Operations:** operational practices for reliable data systems
* **Data Architecture:** designing scalable and maintainable systems
* **Orchestration:** coordinating and scheduling data workflows
* **Software Engineering:** applying best practices like version control and testing

---




#### Data Engineering tools (overview)

Popular languages in Data Realm: Python, Java, Scala, R

* **Small data tools:** Python, Pandas, SQL, Dask
* **Big data tools:** Apache Spark, Apache NiFi, Apache Flink
* **Cloud Data Engineering platforms:** AWS, Azure, GCP

**Tools to be covered in this program:**

* Python
* Git
* Pandas
* SQL
* Docker
* Spark
* NiFi
* Flink


Assignment:
- When do we call a data small or big?