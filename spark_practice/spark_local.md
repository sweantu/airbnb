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
    --output=data/report-2021

./sbin/stop-worker.sh
./sbin/stop-master.sh
```
