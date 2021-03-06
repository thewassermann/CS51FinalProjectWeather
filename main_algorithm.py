'bulk of the algorithm is computed here'
# from weather_data import get_CD, get_PD

import numpy as np

class MainAlgorithm:

	def sliding_windows (self, PD) :
		'uses iterative process to create 8 sliding windows from PD'
		'present them as a list'
		# Ok here's how we'll do this
		# PD should be in the form of a 14 x 4 matrix already SO
		w = []
		for i in xrange (0, 8) :
			w.append(np.vstack((PD[i],PD[i+1],PD[i+2],PD[i+3],PD[i+4],PD[i+5],PD[i+6])))
		return w

	def euc_distance (self, w, CD) :
		'uses iterative process to compute euclidian distance of each sliding window with CD'
		'present as list'
		ed = []
		for i in xrange(0, 8) :
			ed.append(np.linalg.norm(CD - w[i]))
		return ed


	def select_matrix (self, w, euc_list) :
		'Wi = Corresponding_Matrix(Min.(euc_distancei))'
		'for each matrix'
		m = min(euc_list)
		index = [i for i, j in enumerate(euc_list) if j == m]
		return w[index[0]]

	def variation_vector(self, matrix, return_vector):
		' turns 7 x 3 matrix into 4 6 x 1 matrices. i will represent this as'
		' a 6 x 3 matrix, and produce a function that can parse this'

		column_array = np.hsplit(matrix, 3)

		prcp_list = column_array[0].flatten().tolist()
		tmax_list = column_array[1].flatten().tolist()
		tmin_list = column_array[2].flatten().tolist()

		prcp_list_helper = [0] + prcp_list[0:6]
		tmax_list_helper = [0] + tmax_list[0:6]
		tmin_list_helper = [0] + tmin_list[0:6]

		var_prcp = map(lambda x, y: x - y, prcp_list_helper, prcp_list)
		var_tmax = map(lambda x, y: x - y, tmax_list_helper, tmax_list)
		var_tmin = map(lambda x, y: x - y, tmin_list_helper, tmin_list)

		if (return_vector is "prcp") :
			return var_prcp[1:7]
		elif (return_vector is "tmax") :
			return var_tmax[1:7]
		elif (return_vector is "tmin") :
			return var_tmin[1:7] 
		else :
			print "Invalid, ya done fucked up"

		

