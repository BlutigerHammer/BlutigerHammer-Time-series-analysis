import file_operator as fo
import sun_hours as sh
import visualiation as v
import data_analysis as da
import testing

# sunrises_sunsets = sh.sunrise_sunset()
# fo.correcting_data('data\\OULU_march_1min')
# fo.add_day_night(data, sunrises_sunsets)

# fo.correcting_data('data\\OULU_all_1day')

data = fo.read_data('data\\OULU_all_1day_corrected')
# data = fo.read_data('data\\OULU_march_1min_corrected')

# v.plotting(data)
# data = fo.delete_empty_data(data)
# v.plotting(data1)
# testing.localized_regression(data)
# v.autocorrelation(data)
# v.partial_correlation(data)
# v.localized_regression(data)
v.violin_chart(data)
# da.naive_methods(data)
# da.xxx(data)

