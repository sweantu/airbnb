CREATE OR REPLACE EXTERNAL TABLE `airbnb_468005_dataset.external_yellow_tripdata`
OPTIONS (
  format = 'CSV',
  uris = ['gs://airbnb-468005-bucket/dbt_practice/yellow/yellow_tripdata_2020-*.csv.gz']
);

CREATE OR REPLACE TABLE airbnb_468005_dataset.yellow_tripdata AS
SELECT * FROM airbnb_468005_dataset.external_yellow_tripdata;

CREATE OR REPLACE EXTERNAL TABLE `airbnb_468005_dataset.external_green_tripdata`
OPTIONS (
  format = 'CSV',
  uris = ['gs://airbnb-468005-bucket/dbt_practice/green/green_tripdata_2020-*.csv.gz']
);

CREATE OR REPLACE TABLE airbnb_468005_dataset.green_tripdata AS
SELECT * FROM airbnb_468005_dataset.external_green_tripdata;

CREATE OR REPLACE EXTERNAL TABLE `airbnb_468005_dataset.external_fhv_tripdata`
OPTIONS (
  format = 'CSV',
  uris = ['gs://airbnb-468005-bucket/dbt_practice/fhv/fhv_tripdata_2020-*.csv.gz']
);

CREATE OR REPLACE TABLE airbnb_468005_dataset.fhv_tripdata AS
SELECT * FROM airbnb_468005_dataset.external_fhv_tripdata;

