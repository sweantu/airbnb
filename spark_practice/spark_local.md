#### how to run spark locally

#### check spark master in http://localhost:8080/

```bash
cd $SPARK_HOME
./sbin/start-master.sh
URL="spark://gcp-practice.asia-southeast1-b.c.gcp-practice-16925.internal:7077"
./sbin/start-worker.sh ${URL}

jupyter nbconvert --to=script 06_spark_sql.ipynb

python spark_local.py \
    --input_green=data/pq/green/2020/* \
    --input_yellow=data/pq/yellow/2020/* \
    --output=data/report-2020

spark-submit \
    --master=${URL} \
    spark_local.py \
    --input_green=data/pq/green/2021/* \
    --input_yellow=data/pq/yellow/2021/* \
    --output=data/report-2021

./sbin/stop-worker.sh
./sbin/stop-master.sh
```
