'bulk of the algorithm is computed here'
from weather_data import get_CD, get_PD
import numpy as np
class main_algorithm:

	def sliding_windows (self, PD) :
		'uses iterative process to create 8 sliding windows from PD'
		'present them as a list'
		# Ok here's how we'll do this
		# PD should be in the form of a 14 x 4 matrix already SO
		W = []
		For i in range (0, 8)
			W.append(np.vstack((PD[i],PD[i+1],PD[i+2],PD[i+3],PD[i+4],PD[i+5],PD[i+6])))

	def euc_distance (self, CD) :
		'uses iterative process to compute euclidian distance of each sliding window with CD'
		'present as list'

	def select_matrix (self, euc_list) :
		'Wi = Corresponding_Matrix(Min.(euc_distancei))'
		'for each matrix'

	def variation_vector (self, matrix) :
		'takes in a matrix, computes variance vector'

	def get_VC (self) :
		'expose VC'

	def get_VP (self) :
		'expose VP'

		'im a massive nerd'







	