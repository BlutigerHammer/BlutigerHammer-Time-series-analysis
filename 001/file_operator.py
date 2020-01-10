import pandas as pd
import datetime as dt


def read_data(path):
    data = pd.read_csv(path, sep=',')
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], utc=False)

    return data


def correcting_data(path, sunrises, sunsets):
    # data['TimeOfDay'] = '?'
    # data['TimeOfDay'] = data['TimeOfDay'].replace('?', 'night')
    data = pd.read_csv(path, sep=',', usecols=['Timestamp', 'CorrectedCountRate[cts/min]'])
    data.rename(columns={'CorrectedCountRate[cts/min]': 'CountRate'}, inplace=True)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], utc=False)

    # adding do dataframe column which time is day or night
    data['TimeOfDay'] = 'night'
    for i, j in zip(sunrises, sunsets):
        for k in range(len(data['Timestamp']) - 1):
            if dt.datetime.strptime(i, '%Y-%m-%dT%H:%M:%SZ') < data['Timestamp'][k].tz_convert(None) \
                    < dt.datetime.strptime(j, '%Y-%m-%dT%H:%M:%SZ'):
                data.loc[[k], ['TimeOfDay']] = 'day'
    data.to_csv('data\\OULU_march_1min_corrected')
