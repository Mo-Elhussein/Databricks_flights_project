from pyspark.sql.functions import *
from pyspark.sql.types import *
import dlt

## booking data
@dlt.view (
    name = "transformed_bookings"
)


def transformed_bookings():
    df = spark.readStream.format("delta").load("/Volumes/workspace/bronze/bronzevolume/bookings/data/")\
                         .withColumn("modefieddate", current_timestamp())\
                         .drop("_rescued_data")
    return df
dlt.create_streaming_table(name = "silver_bookings")

dlt.create_auto_cdc_flow(
    target = "silver_bookings",
    source=  "transformed_bookings",
    keys = ["booking_id"],
    sequence_by = col("modefieddate"),
    stored_as_scd_type = 1
)


#flight data

@dlt.view (
    name = "transformed_flights"
)


def transformed_flights():
    df = spark.readStream.format("delta").load("/Volumes/workspace/bronze/bronzevolume/flights/data/")\
                         .withColumn("modefieddate", current_timestamp())\
                         .drop("_rescued_data")
    return df
dlt.create_streaming_table(name = "silver_flights")

dlt.create_auto_cdc_flow(
    target = "silver_flights",
    source=  "transformed_flights",
    keys = ["flight_id"],
    sequence_by = col("modefieddate"),
    stored_as_scd_type = 1
)


#airport data

@dlt.view (
    name = "transformed_airports"
)


def transformed_airports():
    df = spark.readStream.format("delta").load("/Volumes/workspace/bronze/bronzevolume/airports/data/")\
                         .withColumn("modefieddate", current_timestamp())\
                         .drop("_rescued_data")
    return df
dlt.create_streaming_table(name = "silver_airports")

dlt.create_auto_cdc_flow(
    target = "silver_airports",
    source=  "transformed_airports",
    keys = ["airport_id"],
    sequence_by = col("modefieddate"),
    stored_as_scd_type = 1
)

#passenger data

@dlt.view (
    name = "transformed_passengers"
)


def transformed_passengers():
    df = spark.readStream.format("delta").load("/Volumes/workspace/bronze/bronzevolume/customers/data/")\
                         .withColumn("modefieddate", current_timestamp())\
                         .drop("_rescued_data")
    return df
dlt.create_streaming_table(name = "silver_passengers")

dlt.create_auto_cdc_flow(
    target = "silver_passengers",
    source=  "transformed_passengers",
    keys = ["passenger_id"],
    sequence_by = col("modefieddate"),
    stored_as_scd_type = 1
)

#bussiness data

@dlt.table (
    name = "silver_bussiness"
)

def silver_bussiness():
    df = dlt.readStream("silver_bookings")\
                       .join(dlt.readStream("silver_flights"), ["flight_id"])\
                       .join(dlt.readStream("silver_airports"), ["airport_id"])\
                       .join(dlt.readStream("silver_passengers"), ["passenger_id"])\
                       .drop("modefieddate")
                       
    return df
                       
                   












