from pyspark.sql.functions import col, explode
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StockETLJob").getOrCreate()
df_raw = spark.read.json("s3://my-stock-data-bucket/raw/")

df_exploded = df_raw.selectExpr("explode(`time series (5min)`) as time_series_data")
df_flattened = df_exploded.select(
    col("time_series_data.key").alias("trade_time"),
    col("time_series_data.value.close").alias("stock_price")
)

df_flattened.write.mode("overwrite").parquet("s3://my-stock-data-bucket/etl_output/")
