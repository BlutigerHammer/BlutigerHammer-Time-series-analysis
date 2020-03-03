import numpy as np
from skyfield import almanac
from skyfield import api


def sunrise_sunset():
    e = api.load('de421.bsp')
    ts = api.load.timescale()
    bluffton = api.Topos('65.02 N', '25.47 E')  # Oulu coordinates
    t0 = ts.utc(2019, 3, 1, 0)
    t1 = ts.utc(2019, 4, 1, 0)
    t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(e, bluffton))

    sunrises = np.array(t.utc_iso()[::2])  # gets every element which index is even
    sunsets = np.array(t.utc_iso()[1::2])  # gets every element which index is odd
    # sunrises_sunsets = pd.DataFrame({'sunrises':sunrises, 'sunsets':sunsets})
    return sunrises, sunsets
