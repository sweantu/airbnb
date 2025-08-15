#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('ls -la ~/.keys')


# In[6]:


get_ipython().system('gcloud auth activate-service-account --key-file "/home/sweantu/.keys/airbnb-468005-b68cd81995fd.json"')


# In[7]:


get_ipython().system('gsutil -m cp -r data/pq/ gs://airbnb-468005-bucket/spark_practice/data/pq')


# In[9]:


get_ipython().system('wget https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar')


# In[10]:


import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext


# In[11]:


credentials_location = "/home/sweantu/.keys/airbnb-468005-b68cd81995fd.json"

conf = SparkConf() \
    .setMaster('local[*]') \
    .setAppName('test') \
    .set("spark.jars", "gcs-connector-hadoop3-latest.jar") \
    .set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", credentials_location)


# In[12]:


sc = SparkContext(conf=conf)

hadoop_conf = sc._jsc.hadoopConfiguration()

hadoop_conf.set("fs.AbstractFileSystem.gs.impl",  "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", credentials_location)
hadoop_conf.set("fs.gs.auth.service.account.enable", "true")


# In[13]:


spark = SparkSession.builder \
    .config(conf=sc.getConf()) \
    .getOrCreate()


# In[14]:


df_green = spark.read.parquet('gs://airbnb-468005-bucket/spark_practice/data/pq/green/*/*')


# In[15]:


df_green.show()


# In[16]:


df_green.count()


# In[17]:


df_yellow = spark.read.parquet('gs://airbnb-468005-bucket/spark_practice/data/pq/yellow/*/*')


# In[18]:


df_yellow.count()


# In[19]:


df_green = df_green \
    .withColumnRenamed('lpep_pickup_datetime', 'pickup_datetime') \
    .withColumnRenamed('lpep_dropoff_datetime', 'dropoff_datetime')


# In[20]:


df_yellow = df_yellow \
    .withColumnRenamed('tpep_pickup_datetime', 'pickup_datetime') \
    .withColumnRenamed('tpep_dropoff_datetime', 'dropoff_datetime')


# In[21]:


common_columns = []
yellow_columns = set(df_yellow.columns)

for col in df_green.columns:
    if col in yellow_columns:
        common_columns.append(col)


# In[22]:


from pyspark.sql import functions as F


# In[23]:


df_green_sel = df_green \
    .select(common_columns) \
    .withColumn('service_type', F.lit('green'))


# In[24]:


df_yellow_sel = df_yellow \
    .select(common_columns) \
    .withColumn('service_type', F.lit('yellow'))


# In[25]:


df_trips_data = df_green_sel.unionAll(df_yellow_sel)


# In[26]:


df_trips_data.groupBy('service_type').count().show()


# In[27]:


df_trips_data.createOrReplaceTempView('trips_data')


# In[28]:


spark.sql("""
SELECT * FROM trips_data LIMIT 10;
""").show()


# In[29]:


spark.sql("""
SELECT
    service_type,
    count(1)
FROM
    trips_data
GROUP BY service_type;
""").show()


# In[31]:


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


# In[32]:


df_result.show()


# In[34]:


df_result.coalesce(1).write.parquet('gs://airbnb-468005-bucket/spark_practice/data/report/revenue/', mode='overwrite')


# In[35]:


df_report = spark.read.parquet('gs://airbnb-468005-bucket/spark_practice/data/report/revenue/')


# In[36]:


df_report


# In[37]:


df_report.count()


# In[38]:


df_report.show()


# In[ ]:




