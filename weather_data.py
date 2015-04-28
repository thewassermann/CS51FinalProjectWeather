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

	def extract_yesterday (self, matrix, return_val) :
		column_array = np.hsplit(matrix, 3)

		prcp_list = column_array[0].flatten().tolist()
		tmax_list = column_array[1].flatten().tolist()
		tmin_list = column_array[2].flatten().tolist()

		if (return_val is "prcp") :
			return prcp_list[6]
		elif (return_val is "tmax") :
			return tmax_list[6]
		elif (return_val is "tmin") :
			return tmin_list[6] 
		else :
			print "Invalid, ya done fucked up"