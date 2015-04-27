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
print "\n"
print "PD :"
print b
print "\n"

from main_algorithm import MainAlgorithm

m = MainAlgorithm()

win = m.sliding_windows(b)

disList = m.euc_distance(win,a)

sel = m.select_matrix(win,disList)

print "Sliding Windows :"
print win
print "\n"
print "Euclidian Distances :"
print disList
print "\n"
print "Closest Matrix :"
print sel
print "\n"


print "precipitation VC :"
testing_main_algorithm = m.variation_vector(a, "prcp")
print "\n"
print "tmax VC :"
testing_main_algorithm = m.variation_vector(a, "tmax")
print "\n"
print "tmin VC :"
testing_main_algorithm = m.variation_vector(a, "tmin")

print "\n\n"

print "precipitation VP :"
testing_main_algorithm = m.variation_vector(sel, "prcp")
print "\n"
print "tmax VP :"
testing_main_algorithm = m.variation_vector(sel, "tmax")
print "\n"
print "tmin VP :"
testing_main_algorithm = m.variation_vector(sel, "tmin")