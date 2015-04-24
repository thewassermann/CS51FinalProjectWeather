# from stat_calc import get_variation
# from weather_data import prev_day
# class main:

# 	def finishing_move (sef, get_variation, prev_day):
# 			'add variation and prev_day conditions'

from weather_data import WeatherData

w = WeatherData()

a = w.make_CD('CD.csv')
b = w.make_PD('PD.csv')

print a
print b

from main_algorithm import MainAlgorithm

m = MainAlgorithm()

win = m.sliding_windows(b)

disList = m.euc_distance(win,a)

sel = m.select_matrix(win,disList)

print m
print win
print disList
print sel