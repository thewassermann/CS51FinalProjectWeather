import numpy

class weather_data:

	CD_matrix = numpy.empty([9,5])
	PD_matrix = numpy.empty([16, 5])

	def make_CD (self, csv) :
		CD_matrix = numpy.genfromtxt('CD.csv', delimiter=',')

	def make_PD (self, csv) :
		PD_matrix = numpy.genfromtxt('PD.csv', delimiter=',')

	def get_PD (self) :
		self.make_CD
		return PD_matrix

	def get_CD (self) :
		self.make_PD
		return CD_matrix