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
pvc = m.variation_vector(a, "prcp")
print pvc
print "\n"
print "tmax VC :"
xvc = m.variation_vector(a, "tmax")
print xvc
print "\n"
print "tmin VC :"
nvc = m.variation_vector(a, "tmin")
print nvc

print "\n\n"

print "precipitation VP :"
pvp = m.variation_vector(sel, "prcp")
print pvp
print "\n"
print "tmax VP :"
xvp = m.variation_vector(sel, "tmax")
print xvp
print "\n"
print "tmin VP :"
nvp = m.variation_vector(sel, "tmin")
print nvp
print "\n"


from stat_calc import StatCalc

s = StatCalc()

vprcp = s.variation_helper(pvc, pvp)
print vprcp
vtmax = s.get_variation(xvc, xvp)
print vtmax
vtmin = s.get_variation(nvc, nvp)
print vtmin