import numpy as np

class WeatherData:        

	# CD_matrix = numpy.empty([9,5])
	# PD_matrix = numpy.empty([16, 5])

	def make_CD (self, csv) :
		return np.genfromtxt(csv, delimiter=',')

	def make_PD (self, csv) :
		return np.genfromtxt(csv, delimiter=',')

	def get_PD (self) :
		return self.make_PD

	def get_CD (self) :
		return self.make_CD
