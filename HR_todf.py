import pandas as pd
from pandas import json_normalize
import json

def HR_todf(file_loc):
    with open(file_loc) as f:
        json_object = json.load(f)
    hrdf = pd.DataFrame()
    for date in list(json_object.keys()):
        df = json_normalize(json_object[date]['activities-heart-intraday']['dataset'])
        if df.shape != (0, 0):
            df['date'] = pd.to_datetime(f'{date}')
            df['date_time'] = pd.to_datetime(f'{date} ' + df['time'])
            df = df[['date_time', 'date', 'time', 'value']]
            hrdf=pd.concat((hrdf,df), sort=False)
    return hrdf
