import file_operator as fo
import sun_hours as sh
import visualiation as v
import data_analysis as da

# preparing data day-night analysis
sunrises, sunsets = sh.sunrise_sunset()
fo.correcting_data('data\\OULU_march_1min')
data1 = fo.read_data('data\\OULU_march_1min_corrected')
fo.add_day_night(data1, sunrises, sunsets)

# day-night analysis
v.plotting(data1)
da.naive_methods(data1)
v.autocorrelation(data1)
v.partial_correlation(data1)
v.localized_regression(data1)


# preparing data all years of operation university of Oulu lab analysis
fo.correcting_data('data\\OULU_all_1day')
data2 = fo.read_data('data\\OULU_all_1day_corrected')
data2 = fo.delete_empty_data(data2)

# long term analysis
v.plotting(data2)
da.naive_methods(data2)
v.autocorrelation(data2)
v.partial_correlation(data2)
v.localized_regression(data2)


