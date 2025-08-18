## Evaluation Criteria

- Problem description: Problem is well described and it's clear what the problem the project solves. Airbnb in NYC.
- Cloud: The project is developed in the cloud and IaC tools are used. Ubuntu 22 VM in GCP and Terraform for GCS and Bigquery.
- Data ingestion (choose either batch or stream)
  - Batch / Workflow orchestration: End-to-end pipeline: multiple steps in the DAG, uploading data to data lake. Kestra downloads csv files, use pandas to clean and convert data to parquet, and uploads to GCS
- Data warehouse: Tables are partitioned and clustered in a way that makes sense for the upstream queries (with explanation). Create tables from parquet files in GCS with approriate partition and cluster.
- Transformations (dbt, spark, etc): Tranformations are defined with dbt, Spark or similar technologies. First, I will use dbt to transform to star schema. Then I use looker to create 2 dashboards. Finally, I use Spark to perform complex tranformation like UDF.
- Dashboard: A dashboard with 2 tiles
- Reproducibility: Instructions are clear, it's easy to run the code, and the code works

## Plan 1 month

- Week 1: Creating a pipeline for processing this dataset and putting it to a datalake
- Week 2: Creating a pipeline for moving the data from the lake to a data warehouse
- Week 3: Transforming the data in the data warehouse: prepare it for the dashboard
- Week 4: Put it all together
- 5 days: Review and optimize
