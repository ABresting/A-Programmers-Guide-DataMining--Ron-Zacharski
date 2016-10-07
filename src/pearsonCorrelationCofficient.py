
from math import sqrt

import data

def pearson( rating1, rating2  ):
	sum_xy=0
	sum_x1=0
	sum_y1=0
	sum_x2=0
	sum_y2=0
	n=0  #to check how many ratings are common 
	for key in rating1:
		if key in rating2:
			n +=1
			x=rating1[key]
			y=rating2[key]
			sum_xy += x*y
			sum_x1 += x
			sum_y1 += y
			sum_x2 += x**2
			sum_y2 += y**2
	if n == 0:
		return 0

	denominator = (sqrt(sum_x2 - (sum_x1**2) / n) * sqrt(sum_y2 - (sum_y1**2) )/ n)
	if denominator == 0:
		return 0
	else :
		return (sum_xy - (sum_x1 * sum_y1)/n)/denominator

