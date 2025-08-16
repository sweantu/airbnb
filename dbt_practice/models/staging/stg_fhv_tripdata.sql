-- {{ config(materialized='view') }}
{{ config(materialized='table') }}

select *
from {{ source('staging','fhv_tripdata') }}
where dispatching_base_num is not null 

-- dbt build --select <model.sql> --vars '{'is_test_run: false}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}