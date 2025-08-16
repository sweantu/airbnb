## References

- [Github](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main?tab=readme-ov-file)
- [Youtube](https://www.youtube.com/watch?v=-zpVha7bw5A&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

## Evaluation Criteria

- Problem description: Problem is well described and it's clear what the problem the project solves
- Cloud: The project is developed in the cloud and IaC tools are used
- Data ingestion (choose either batch or stream)
  - Batch / Workflow orchestration: End-to-end pipeline: multiple steps in the DAG, uploading data to data lake
  - Stream: Using consumer/producers and streaming technologies (like Kafka streaming, Spark streaming, Flink, etc)
- Data warehouse: Tables are partitioned and clustered in a way that makes sense for the upstream queries (with explanation)
- Transformations (dbt, spark, etc): Tranformations are defined with dbt, Spark or similar technologies
- Dashboard: A dashboard with 2 tiles
- Reproducibility: Instructions are clear, it's easy to run the code, and the code works
