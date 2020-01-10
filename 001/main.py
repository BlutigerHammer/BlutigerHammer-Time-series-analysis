import file_operator as fo
import sun_hours as sh
import visualiation as v
import data_analysis as da
import testing


sunrises, sunsets = sh.sunrise_sunset()
# fo.correcting_data('data\\OULU_march_1min', sunrises, sunsets)
data = fo.read_data('data\\OULU_march_1min_corrected')
# v.plotting(data, sunrises, sunsets)
da.average(data)
