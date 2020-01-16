import numpy as np
import time
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
import matplotlib.pyplot as plt

def naive_methods(data):
    '''
    x = data.groupby('TimeOfDay')
    print(round(x.mean().loc['day', 'CountRate'], 0))
    print(round(x.std().loc['day', 'CountRate'], 0))
    print(round(x.max().loc['day', 'CountRate'], 0))

    print(round(x.mean().loc['night', 'CountRate'], 0))
    print(round(x.std().loc['night', 'CountRate'], 0))
    print(round(x.min().loc['night', 'CountRate'], 0))
    '''

    ''' autocorelation and partial autocorelation
    # plot_acf(data['CountRate']) # autocorrelation is small because noise is too big
    # plt.show()
    plot_pacf(data['CountRate']) # , lags=100)
    plt.show()
    '''
