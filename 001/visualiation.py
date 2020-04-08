import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters  # FutureWarning
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.nonparametric.smoothers_lowess import lowess

register_matplotlib_converters()  # FutureWarning


def plotting(data, sunrises=None, sunsets=None):
    x = data['Timestamp'].values
    y1 = data['CountRate'].values

    gs = gridspec.GridSpec(2, 1)
    ax1 = plt.subplot(gs[0, 0])
    plt.xlim(x[0], x[len(x) - 1])
    ax1.plot(x, y1, 'k-')

    ax2 = plt.subplot(gs[1, 0])
    y2 = pd.DataFrame(y1)
    # y2 = y2.rolling(window=60).mean()
    # ax2.plot(x,y2,'g-')

    y22 = y2.rolling(window=720).mean()  # 720min = 12h - expected seasonal duration
    ax2.plot(x, y22, 'k-')

    y3 = y1 * 0 + np.mean(y1)
    ax2.plot(x, y3, 'y-')
    ax1.plot(x, y3, 'y-')

    if sunrises or sunsets is not None:
        for i in sunrises:
            ax2.axvline(pd.Timestamp(i), color='r', alpha=0.5)
        for i in sunsets:
            ax2.axvline(pd.Timestamp(i), color='b', alpha=0.5)
        plt.xlim(x[0], x[len(x) - 1])

    plt.show()


def localized_regression(data, fraction=0.05):
    lowess = lowess(data['CountRate'], data['Timestamp'], frac=0.01)
    lowess_x = list(zip(*lowess))[0]
    lowess_y = list(zip(*lowess))[1]

    plt.plot(lowess_x, lowess_y, '-')
    plt.show()


def autocorrelation(data):
    plot_acf(data['CountRate'])
    plt.show()


def partial_correlation(data):
    plot_pacf(data['CountRate'])  # , lags=100)
    plt.show()
