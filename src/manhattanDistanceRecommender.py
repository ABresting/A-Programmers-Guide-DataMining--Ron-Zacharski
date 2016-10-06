
import	data

"""Manhattan Distance for Data Mining the absolute distance
   of the data points on a plane"""

def manhattan (rating1, rating2):
	"""computes the manhattan distance between dictionaries rating1 and rating2
		from dictionary 'users' """
	distance =0
	for key in rating1:
		if key in rating2:
			distance+= abs(rating1[key] - rating2[key])
	return distance

def ComputeNearestNeighabour( username , users ):
	distances = []
	for user in users:
		if user != username:
			distance = manhattan(users[user], users[username])
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

print recommander("Hailey", data.users)  #recommendation for Hailey