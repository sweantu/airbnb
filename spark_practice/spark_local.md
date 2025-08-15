#### how to run spark locally

#### check spark master in http://localhost:8080/

```bash
cd $SPARK_HOME
./sbin/start-master.sh
URL=spark://instance-20250814-112447.us-central1-c.c.airbnb-468005.internal:7077
./sbin/start-worker.sh ${URL}

jupyter nbconvert --to=script 06_spark_sql.ipynb

python spark_local.py \
    --input_green=data/pq/green/2021/* \
    --input_yellow=data/pq/yellow/2021/* \
    --output=data/report-2021

spark-submit \
    --master=${URL} \
    spark_local.py \
    --input_green=data/pq/green/2021/* \
    --input_yellow=data/pq/yellow/2021/* \
    --output=data/report-2021-2

python spark_local_gcs.py \
    --input_green=gs://airbnb-468005-bucket/spark_practice/data/pq/green/*/* \
    --input_yellow=gs://airbnb-468005-bucket/spark_practice/data/pq/yellow/*/* \
    --output=gs://airbnb-468005-bucket/spark_practice/data/report-2021

spark-submit \
    --master=${URL} \
    --jars /home/sweantu/code/airbnb/spark_practice/gcs-connector-hadoop3-latest.jar \
    spark_local_gcs.py \
    --input_green=gs://airbnb-468005-bucket/spark_practice/data/pq/green/*/* \
    --input_yellow=gs://airbnb-468005-bucket/spark_practice/data/pq/yellow/*/* \
    --output=gs://airbnb-468005-bucket/spark_practice/data/report-2021-2

wget https://storage.googleapis.com/spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.36.1.jar
spark-submit \
    --master=${URL} \
    --jars /home/sweantu/code/airbnb/spark_practice/gcs-connector-hadoop3-latest.jar,/home/sweantu/code/airbnb/spark_practice/spark-bigquery-with-dependencies_2.12-0.36.1.jar \
    spark_local_gcs_bigquery.py \
    --input_green=gs://airbnb-468005-bucket/spark_practice/data/pq/green/*/* \
    --input_yellow=gs://airbnb-468005-bucket/spark_practice/data/pq/yellow/*/* \
    --output_bq=airbnb-468005:airbnb_468005_dataset.report_2021

./sbin/stop-worker.sh
./sbin/stop-master.sh
```
