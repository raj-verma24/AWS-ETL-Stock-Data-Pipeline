# AWS-ETL-Stock-Data-Pipeline


## **🔹 Overview**  
This project implements a **scalable ETL pipeline** using AWS services to ingest, process, and analyze **stock market data**. It leverages **Lambda, S3, Glue, and Redshift** for end-to-end data processing.


## **🔹 AWS Services Used**  
✅ **AWS Lambda** → Fetches stock data automatically from an API  
✅ **Amazon S3** → Stores raw JSON and transformed data  
✅ **AWS Glue** → Crawls schema and processes data with PySpark  
✅ **Amazon Redshift** → Loads structured stock data for analytics  
✅ **IAM Roles & Policies** → Manages secure service access  



## **🔹 ETL Pipeline Architecture**  
**Data Flow:**  

Stock Price API → AWS Lambda → S3 → AWS Glue → Redshift

## **🔹 Folder Structure**

AWS-ETL-Stock-Data-Pipeline/
│── lambda_scripts/               # Lambda function for data ingestion
│   ├── fetch_stock_data.py
│── glue_etl_jobs/                # PySpark scripts for ETL processing
│   ├── stock_etl_job.py
│── redshift_sql/                 # SQL queries for Redshift data loading & analysis
│   ├── copy_to_redshift.sql
│   ├── queries.sql
│── iam_policies/                  # IAM role JSON policies for AWS services
│   ├── s3_redshift_access.json
│   ├── glue_execution_role.json
│── architecture_diagram/         # Visual representation of AWS pipeline
│   ├── aws_etl_pipeline.png
│── README.md                      # Project documentation
│── requirements.txt               # Dependencies for PySpark & AWS SDKs
│── LICENSE                        # License file (Optional)
│── .gitignore                     # Files to ignore in Git tracking


---

## **🔹 Setup & Deployment**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-github-username/AWS-ETL-Stock-Data-Pipeline.git
cd AWS-ETL-Stock-Data-Pipeline

2️⃣ Install Required Dependencie
```
Bash
pip install -r requirements.txt

```
3️⃣ Configure AWS Credentials
Ensure your AWS CLI is set up correctly:
```
Bash
aws configure
```

🔹 How It Works
🛠 1️⃣ Data Ingestion with AWS Lambda
- The Lambda function fetches stock price data every 5 minutes using an API
- Stores the raw JSON data in S3 (my-stock-data-bucket/raw/)
📌 Lambda Script: lambda_scripts/fetch_stock_data.py



🛠 2️⃣ Schema Detection with AWS Glue
- AWS Glue Crawler scans raw data in S3
- Automatically creates a structured table schema in AWS Glue Catalog
📌 Glue Catalog Table: stock_my_stock_data_bucket

🛠 3️⃣ ETL Processing with AWS Glue (PySpark)
- PySpark transformations extract timestamped stock prices
- Transformed data is stored in Parquet format in S3 (etl_output/)
📌 Glue ETL Script: glue_etl_jobs/stock_etl_job.py



🛠 4️⃣ Loading into Amazon Redshift
- Redshift loads structured stock data for advanced analytics
- Uses IAM Role to grant permissions
📌 Redshift COPY Command: redshift_sql/copy_to_redshift.sql


🔹 IAM Roles & Policies Configured
✔ LambdaExecutionRole → Grants Lambda access to write data into S3
✔ GlueExecutionRole → Allows Glue ETL jobs to read & process data
✔ RedshiftS3AccessRole → Enables Redshift to read transformed data from S3
✔ S3 Bucket Policy → Grants Redshift access via IAM
📌 See iam_policies/ for policy configurations

🔹 Future Enhancements
✅ Optimize PySpark transformations for better performance
✅ Implement AWS Step Functions to orchestrate ETL workflows
✅ Enable real-time stock trend predictions using AWS Athena

🔹 Conclusion
🔥 This AWS ETL pipeline successfully processes real-time stock data, enabling structured storage and analytics in Redshift!
📌 Want to discuss AWS-based ETL pipelines? Connect with me on LinkedIn! 🚀



