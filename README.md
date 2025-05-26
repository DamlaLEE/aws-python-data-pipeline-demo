# 🧱 Order-He E-commerce Data Pipeline Project

### A hands-on project to build a full data pipeline from scratch to BI using AWS and Python

---

## 1. Project Overview

This project simulates a data pipeline for a fictional e-commerce service called 'Order-He'. It builds data storage (RDS, DW) and a data mart (DM) to create dashboards using BI tools.

- This project is designed for data engineering beginners to implement a production-level pipeline from scratch.

* **Goal**: To create and manage structured service data through reusable code and folder structuring for easy maintenance.

### Main Tech Stack

- **Python 3.10**, **SQL (MySQL, PostgreSQL)**
  - Libraries: `pymysql`, `yaml`, `pandas`
- **AWS Services**
  - **AWS Redshift (Serverless)**
  - **AWS S3**

---

## 2. 📁 Project Structure
```text
project_for_data_pipeline/
|
├── config/ # Database configuration and SQL query storage
│ ├── db_info.yml # DB connection info (host, dbname, user, etc.) 
│ ├── sql_queries.py # Collection of SQL queries (e.g., table creation)
│
├── data/ # Folder for storing data files (CSV, etc.)
│
├── scripts/ # Execution scripts
│ ├── create_db_and_tables.py # Script to create DB and tables
│
├── utils/ # Utility functions
│ ├── db_helper.py # Redshift connection and SQL execution utilities
│
├── main.ipynb # Main project notebook
├── README.md # English README
├── README.ko.md # Korean README
```

<Note: This file is excluded from GitHub for security reasons but included here for structure reference>

---

## 3. Summary of Data Pipeline Flow

**End-to-end data pipeline flow**:  
[data_pipeline](images/data_pipeline_chart_ver1.png)

```text
[AWS RDS workgroup creation] → [ETL process with Python] → [Backup to S3] → [AWS Redshift data warehouse creation & data load] → [Data mart creation in Redshift]
```

## 4. Step-by-Step Implementation [Tools Used]
### Step 1: [AWS] Create AWS Redshift Warehouse

- Create a Serverless Redshift instance from the AWS Console.
- Tip: Store connection credentials (host, dbname, user, password, etc.) separately in a .yml file to enhance security.

---

### Step 2: [VSCode] Connect to Redshift using Python

Use the pymysql library to connect to Redshift from Python.

- Example Python code for connection:
```python
import pymysql

conn = pymysql.connect(
    host="your-host-name",
    dbname="dev",
    user="your-username",
    password="your-password",
    port="5439"
)
cur = conn.cursor()
```

---

### Step 3: [VSCode] Create Tables (order, customer, product)

Create each table using SQL. Below is an example for the order table:

```SQL
CREATE TABLE order (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    amount INT
);
```
- The customer and product tables are created in a similar SQL format.

---

### Step 4: [VSCode] Load Data (CSV → Redshift)

Use `pandas` to load local CSV files
(or load dictionaries or lists defined in `data/initial_data.py`)
and insert them into Redshift using either SQL `INSERT` queries or the `COPY` command.

---

### Step 5: [AWS] Backup to AWS S3

Upload the loaded data or original CSV files to an S3 bucket for backup.

---

### Step 6: [AWS] Create and Save Data Mart

Use SQL within Redshift to create summary tables (Data Mart).  
- Join the order table with customer and product tables to construct an integrated dataset.

---

### Step 7: [Looker Studio] Create Dashboards Using BI Tool
[Dashboard_looker studio](images/looker_studio_dashboard.PNG)
Connect Redshift’s data mart to `Looker Studio` and build dashboards for visualization.
*actualy

---
## 5. 🧨 Key Issues Encountered During the Project

### 1️⃣ RDS Connection Failure – Missing Security Group Rule

- **Issue**:  
  Unable to connect to RDS (MySQL) from Python

- **Example Error Message**:  
```text
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server...")
```
- **Cause**:
    The current IP address was not allowed in the Inbound Rules of the RDS security group

- **Solution**:
    1. Go to the RDS Console → Click the instance → Check VPC Security Group
    2. In the Security Group → Go to Inbound Rules → Add a rule:

        - Type: MySQL/Aurora
        - Port: 3306
        - Source: Your IP address or 0.0.0.0/0

    3. Save the rule and retry the Python connection

### 2️⃣ S3 → Redshift COPY Failure – Missing IAM Role Permissions

- **Issue**:  
  The `COPY` command failed in Redshift Query Editor due to insufficient permissions.

- **Example Error Message**:  
```text
AmazonS3: Access Denied
```

- **Cause**:  
  The IAM Role attached to Redshift Serverless did not have permission to access the S3 bucket.

- **Solution**:  
  1. Go to the AWS Console → IAM → Roles  
  2. Select the IAM Role assigned to Redshift  
  3. Click **Add permissions** → Search for and add the `AmazonS3ReadOnlyAccess` policy  
  4. Retry the `COPY` command in Redshift after the policy is attached

### 3️⃣ BI Tool Connection Failure – Serverless Redshift Blocks Public Access

- **Issue**:  
  BI tools 'Looker Studio' failed to connect to Redshift.

- **Example Error Message**:  
  Connection timeout or authentication failure

- **Cause**:  
  Redshift Serverless does not allow public network access by default.

- **Alternative Solution**:  
  1. Export data from Redshift using the Query Editor and save it as a CSV file  
  2. Upload the CSV directly to the BI tool (e.g., Metabase, Looker Studio)  
  3. Perform visualization based on the uploaded data

- **Extra Tip**:  
  Granting public access requires additional setup (VPC, IAM, Security Group).  
  For practice or testing purposes, using CSV import is often the most efficient approach.

---
## 6. Appendix

- **Author**: DS_Yujin LEE  
- **Project Duration**: April 28, 2025 – May 3, 2025  
- **Development Environment**: Python 3.10, AWS Redshift Serverless, Jupyter Notebook  
- **Data Used**: Synthetic datasets generated using Python scripts
