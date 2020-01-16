import pandas as pd
import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess
import matplotlib.pyplot as plt


def autocorelation(data):

    # Multiplicative Decomposition
    result_mul = seasonal_decompose(data['value'], model='multiplicative', extrapolate_trend='freq')

    # Additive Decomposition
    result_add = seasonal_decompose(data['value'], model='additive', extrapolate_trend='freq')

    # Plot
    plt.rcParams.update({'figure.figsize': (10, 10)})
    result_mul.plot().suptitle('Multiplicative Decompose', fontsize=22)
    result_add.plot().suptitle('Additive Decompose', fontsize=22)
    plt.show()

def localized_regression(data):
    '''
    df_loess_5 = pd.DataFrame(lowess(data['CountRate'], np.arange(len(data['CountRate']), frac=0.05)[:, 1],
                              index=data['Timestamp'], columns=['value'])
    df_loess_15 = pd.DataFrame(lowess(data['CountRate'], np.arange(len(data['CountRate']), frac=0.15)[:, 1],
                               index=data['Timestamp'], columns=['value'])
    '''
    # lowess_5 = lowess(data['CountRate'], data['Timestamp'], frac=0.05)
    # lowess_15 = lowess(data['CountRate'], data['Timestamp'], frac=0.15)
    lowess_30 = lowess(data['CountRate'], data['Timestamp'], frac=0.30)
    # lowess_1 = lowess(data['CountRate'], data['Timestamp'], frac=0.01)
    lowess_x = list(zip(*lowess_30))[0]
    lowess_y = list(zip(*lowess_30))[1]

    plt.plot(lowess_x, lowess_y, '-')
    plt.show()