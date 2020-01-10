def average(data):
    x = data.groupby('TimeOfDay').mean()
    print(round(x.loc['day', 'CountRate'], 0))
    print(round(x.loc['night', 'CountRate'], 0))
