' this class contains the necessary statistical operations for the late stages of the algorithm'
from main_algorithm import VC, VP
class stat_calc:


	def mean_matrix(self, matrix) :
		' This calculates the mean of a variance vector VC or VP'
		return sum(matrix) * 1.0 / len(matrix)

	def variation_helper(self) :
		'calls mean_matrix on VC and VP and gives variation'

	def get_variation (self):
		'exposes variation'
		'oi'



	'the below methods are for use in examining trends'
	def variance( lst , unbiased) :
		' Calculates the variance of a list of objects'
		' unbiased is a bool, if true then (1/n-1) if false (1/n) '
		N = len(lst)
		avg = sum(lst) * 1.0 / N
		epsilon = map(lambda x: (x - avg)**2, lst)

		if unbiased:  
			variance = sum(epsilon) * 1.0 / N - 1 
		else:
			variance = sum(epsilon) * 1.0 / N

		return variance


	def pmcc (lst1, lst2) :
		' Takes in two lists, calculates the correlation coefficient between them'
		s1 = math.sqrt(variance(lst1))
		s2 = math.sqrt(variance(lst2))
		N = len(lst1)
		avg1 = sum(lst1) * 1.0 / N
		avg2 = sum(lst2) * 1.0 / N
		epsilon = map(lambda x, y: (x - avg1)*(y - avg2), lst1, lst2)
 		covariance = sum(epsilon) * 1.0 / N - 1 
		
		return (s1*s2)/covariance


		'question: should this output a list or a value?'






