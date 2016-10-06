
import	data
from math import pow

"""Euclidean / Minkowski method for Data Mining the absolute distance
   of the data points on a plane"""

def minkowski (rating1, rating2, r ):
	"""computes the minkowski/euclidean distance between dictionaries rating1 and rating2
		from dictionary 'users' """
	distance =0
	commonRating = False
	for key in rating1:
		if key in rating2:
			distance+= pow(abs(rating1[key] - rating2[key]),r)
			commonRating = True
	if commonRating:
		return pow(distance, 1/r)
	else :
		return 0

def ComputeNearestNeighabour( username , users ):
	distances = []
	for user in users:
		if user != username:
			distance = minkowski(users[user], users[username], 2)
			distances.append((distance,user))
	distances.sort()  #sorted distances in order
	return distances

def recommander ( username , users ):
	# get the nearest neighabour first
	nearest = ComputeNearestNeighabour(username, users)[0][1]
	recommendation = []
	user = users[username]
	neighabour = users[nearest]

	for artist in neighabour:
		if not artist in user:
			recommendation.append((neighabour[artist], artist))
	recommendation.sort(reverse= True)
	return recommendation

print recommander("Dan", data.users)  #recommendation for Hailey