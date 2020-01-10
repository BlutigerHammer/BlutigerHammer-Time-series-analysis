import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pandas.plotting import register_matplotlib_converters  # FutureWarning

register_matplotlib_converters()  # FutureWarning


def plotting(data, sunrises, sunsets):
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

    y22 = y2.rolling(window=720).mean()
    ax2.plot(x, y22, 'k-')

    y3 = y1 * 0 + np.mean(y1)
    ax2.plot(x, y3, 'y-')
    ax1.plot(x, y3, 'y-')

    for i in sunrises:
        ax2.axvline(pd.Timestamp(i), color='r', alpha=0.5)
    for i in sunsets:
        ax2.axvline(pd.Timestamp(i), color='b', alpha=0.5)
    plt.xlim(x[0], x[len(x) - 1])

    plt.show()


