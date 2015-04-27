# from stat_calc import get_variation
# from weather_data import prev_day
# class main:

# 	def finishing_move (sef, get_variation, prev_day):
# 			'add variation and prev_day conditions'

from weather_data import WeatherData

w = WeatherData()

a = w.make_CD('CD.csv')
b = w.make_PD('PD.csv')

print "CD :"
print a
print "PD :"
print b

from main_algorithm import MainAlgorithm

m = MainAlgorithm()

win = m.sliding_windows(b)

disList = m.euc_distance(win,a)

sel = m.select_matrix(win,disList)

print "Sliding Windows :"
print win
print "Euclidian Distances :"
print disList
print "Closest Matrix :"
print sel

testing_main_algorithm = m.variation_vector(sel, None)
testing_main_algorithm = m.variation_vector(sel, "prcp")
testing_main_algorithm = m.variation_vector(sel, "tmax")
testing_main_algorithm = m.variation_vector(sel, "tmin")