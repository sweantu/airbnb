#!/usr/bin/env python
# coding: utf-8


import argparse

from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

parser = argparse.ArgumentParser()
parser.add_argument("--input_green", required=True)
parser.add_argument("--input_yellow", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
input_green = args.input_green
input_yellow = args.input_yellow
output = args.output

credentials_location = "/home/sweantu/.keys/airbnb-468005-b68cd81995fd.json"

conf = (
    SparkConf()
    .setMaster("local[*]")
    .setAppName("test")
    .set("spark.jars", "gcs-connector-hadoop3-latest.jar")
    .set("spark.hadoop.google.cloud.auth.service.account.enable", "true")
    .set(
        "spark.hadoop.google.cloud.auth.service.account.json.keyfile",
        credentials_location,
    )
)


sc = SparkContext(conf=conf)

hadoop_conf = sc._jsc.hadoopConfiguration()

hadoop_conf.set(
    "fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS"
)
hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", credentials_location)
hadoop_conf.set("fs.gs.auth.service.account.enable", "true")


spark = SparkSession.builder.config(conf=sc.getConf()).getOrCreate()


df_green = spark.read.parquet(input_green)
df_yellow = spark.read.parquet(input_yellow)

df_green = df_green.withColumnRenamed(
    "lpep_pickup_datetime", "pickup_datetime"
).withColumnRenamed("lpep_dropoff_datetime", "dropoff_datetime")
df_yellow = df_yellow.withColumnRenamed(
    "tpep_pickup_datetime", "pickup_datetime"
).withColumnRenamed("tpep_dropoff_datetime", "dropoff_datetime")

common_columns = []
yellow_columns = set(df_yellow.columns)

for col in df_green.columns:
    if col in yellow_columns:
        common_columns.append(col)

df_green_sel = df_green.select(common_columns).withColumn(
    "service_type", F.lit("green")
)


df_yellow_sel = df_yellow.select(common_columns).withColumn(
    "service_type", F.lit("yellow")
)


df_trips_data = df_green_sel.unionAll(df_yellow_sel)

df_trips_data.createOrReplaceTempView("trips_data")

df_result = spark.sql("""
SELECT
    -- Revenue grouping 
    PULocationID AS revenue_zone,
    date_trunc('month', pickup_datetime) AS revenue_month,
    service_type, 

    -- Revenue calculation 
    SUM(fare_amount) AS revenue_monthly_fare,
    SUM(extra) AS revenue_monthly_extra,
    SUM(mta_tax) AS revenue_monthly_mta_tax,
    SUM(tip_amount) AS revenue_monthly_tip_amount,
    SUM(tolls_amount) AS revenue_monthly_tolls_amount,
    SUM(improvement_surcharge) AS revenue_monthly_improvement_surcharge,
    SUM(total_amount) AS revenue_monthly_total_amount,

    -- Additional calculations
    AVG(passenger_count) AS avg_monthly_passenger_count,
    AVG(trip_distance) AS avg_monthly_trip_distance
FROM trips_data
GROUP BY 1,2,3
""")

df_result.coalesce(1).write.parquet(output, mode="overwrite")