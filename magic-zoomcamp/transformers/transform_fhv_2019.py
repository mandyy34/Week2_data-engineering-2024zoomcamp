if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer

def transform(data, *args, **kwargs):
    df = data
    df['pickup_date'] = df['pickup_datetime'].dt.date
    df['dropOff_date'] = df['dropOff_datetime'].dt.date
    return df
