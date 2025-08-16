{{
    config(
        materialized='table'
    )
}}

with dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)
select trips_unioned.dispatching_base_num, 
    trips_unioned.pickup_datetime,
    trips_unioned.dropoff_datetime,
    trips_unioned.PUlocationid, 
    pickup_zone.borough as pickup_borough, 
    pickup_zone.zone as pickup_zone, 
    trips_unioned.DOlocationid,
    dropoff_zone.borough as dropoff_borough, 
    dropoff_zone.zone as dropoff_zone,
    trips_unioned.sr_flag, 
    trips_unioned.Affiliated_base_number,
    EXTRACT(YEAR FROM TIMESTAMP(trips_unioned.pickup_datetime)) AS year,
    EXTRACT(MONTH FROM TIMESTAMP(trips_unioned.pickup_datetime)) AS month
from {{ ref('stg_fhv_tripdata') }} as trips_unioned
inner join dim_zones as pickup_zone
on trips_unioned.PUlocationid = pickup_zone.locationid
inner join dim_zones as dropoff_zone
on trips_unioned.DOlocationid = dropoff_zone.locationid