'bulk of the algorithm is computed here'
from weather_data import get_CD, get_PD

import numpy as np

class main_algorithm:

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
		i = min(euc_list)
		return w[i]

		

	def sub(x,y): return x - y

	def variation_vector (self, matrix) :
		' turns 7 x 4 matrix into 4 6 x 1 matrices. i will represent this as'
		' a 6 x 4 matrix, and produce a function that can parse this'
		flat_matrix = matrix.flatten('F') 
		data_list = flat_matrix.to_list()
		split_list = for i in xrange(0, len(data_list), 7) : yield l[i:i+7]
        prcp_list = split_list[0]
        tmax_list = split_list[1]
        tmin_list = split_list[2]

        prcp_list_helper = [0] + prcp_list[0:6]
        tmax_list_helper = [0] + tmax[0:6]
        tmin_list_helper = [0] + tmin_list[0:6]

        var_prcp = map(sub, prcp_list, prcp_list_helper)
        var_tmax = map(sub, tmax_list, tmax_list_helper)
        var_tmin = map(sub, tmin_list, tmin_list_helper)


	def get_VC (self) :
		'expose VC'

	def get_VP (self) :
		'expose VP'

		'im a massive nerd'







	