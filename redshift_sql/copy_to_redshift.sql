COPY stock_prices 
FROM 's3://my-stock-data-bucket/etl_output/'
IAM_ROLE 'arn:aws:iam::YOUR_ACCOUNT_ID:role/RedshiftS3AccessRole'
FORMAT AS PARQUET;