import datetime as dt

import pandas as pd


def read_data(path):
    data = pd.read_csv(path, sep=',')
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], utc=False)
    print(type(data['Timestamp'][6]))

    return data


def correcting_data(path):
    data = pd.read_csv(path, sep=',', usecols=['Timestamp', 'CorrectedCountRate[cts/min]'])
    data.rename(columns={'CorrectedCountRate[cts/min]': 'CountRate'}, inplace=True)
    data.to_csv('data\\OULU_all_1day_corrected')


def add_day_night(data, sunrises, sunsets):
    # adding do dataframe column which contain information that it is day or night
    data['TimeOfDay'] = 'night'
    k1 = 0
    for i, j in zip(sunrises, sunsets):
        for k in range(k1, len(data['Timestamp']) - 1):
            if dt.datetime.strptime(i, '%Y-%m-%dT%H:%M:%SZ') < data['Timestamp'][k].tz_convert(None) \
                    < dt.datetime.strptime(j, '%Y-%m-%dT%H:%M:%SZ'):
                data.loc[[k], ['TimeOfDay']] = 'day'
            k1 += 1
    data.to_csv('data\\OULU_march_1min_corrected')


def delete_empty_data(data):
    data = data[data['CountRate'] != 0]
    # data = data[data['CountRate'] < 7000]  # delete big magnetic storms
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], utc=False)
    return data
