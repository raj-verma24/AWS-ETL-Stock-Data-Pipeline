import boto3
import requests
import json
import os
from datetime import datetime

# Initialize AWS S3 & SSM client
s3 = boto3.client("s3")
ssm = boto3.client("ssm")

# Get API Key from AWS Parameter Store
api_key = ssm.get_parameter(Name="/stock_api_key", WithDecryption=True)['Parameter']['Value']
api_url = f"https://api.example.com/stock_prices?api_key={api_key}"

# S3 Bucket & Folder Path
s3_bucket = "my-stock-data-bucket"
s3_key_prefix = "raw/stock_data"

def lambda_handler(event, context):
    try:
        # Fetch stock price data using API key
        response = requests.get(api_url)
        response.raise_for_status()
        stock_data = response.json()
        
        # Generate timestamped filename
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        s3_key = f"{s3_key_prefix}_{timestamp}.json"

        # Upload JSON file to S3
        s3.put_object(
            Bucket=s3_bucket,
            Key=s3_key,
            Body=json.dumps(stock_data),
            ContentType="application/json"
        )
        
        print(f"✅ Successfully stored stock data in S3: {s3_key}")
        return {"status": "success", "file": s3_key}
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching stock data: {e}")
        return {"status": "failed", "error": str(e)}