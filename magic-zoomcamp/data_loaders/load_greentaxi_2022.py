import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{:02d}.parquet'
    
    taxi_dtypes = {
                'VendorID': pd.Int64Dtype(),
                'passenger_count': pd.Int64Dtype(),
                'trip_distance': float,
                'RatecodeID':pd.Int64Dtype(),
                'store_and_fwd_flag':str,
                'PULocationID':pd.Int64Dtype(),
                'DOLocationID':pd.Int64Dtype(),
                'payment_type':pd.Int64Dtype(),
                'fare_amount': float,
                'extra':float,
                'mta_tax':float,
                'tip_amount':float,
                'tolls_amount':float,
                'improvement_surcharge':float,
                'total_amount':float,
                'congestion_surcharge':float,
                'ehail_fee':float,
                'trip_type':pd.Int64Dtype()

            }
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    green_tripdata_2022_data = pd.DataFrame()

    for month in range (1, 13):
        url = base_url.format(month)
        current_month_data = pd.read_parquet(url)
        green_tripdata_2022_data = pd.concat([green_tripdata_2022_data, current_month_data], ignore_index=True)
    
    return green_tripdata_2022_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
