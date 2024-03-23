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
    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-{:02d}.csv.gz'
    fhv_dtypes = {
                'dispatching_base_num': str,
                'PUlocationID': pd.Int64Dtype(),
                'DOlocationID': pd.Int64Dtype(),
                'SR_Flag':pd.Int64Dtype(),
                'Affiliated_base_number': str
            }
    parse_dates = ['pickup_datetime', 'dropOff_datetime']

    fhv_2019_data = pd.DataFrame()

    for month in range (1, 2):
        url = base_url.format(month)
        current_month_data = pd.read_csv(url, sep=",", compression="gzip", dtype=fhv_dtypes, parse_dates=parse_dates )
        fhv_2019_data = pd.concat([fhv_2019_data, current_month_data], ignore_index=True)
    
    return fhv_2019_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
