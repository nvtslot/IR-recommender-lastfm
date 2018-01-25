import pickle
from collections import Counter

def get_training():
	with open("train.dat","r") as data:
		training = {}
		for line in data.readlines():
			user, artist, count = line.strip().split("\t")
			try:
				training[user][artist] = int(count)
			except KeyError:
				training[user] = {}
				training[user][artist] = int(count)
	return training

def get_test():
	with open("test.dat","r") as test:
		return test.readlines()

def recommend(sim, listen, u1, n):
	scores = []
	for u2 in sim[u1]:
		scores.append((sim[u1][u2],u2))
	already_listened = [] # will contain all artists that are already listened by the user
	try:
		for artist in listen[u1]:
			already_listened.append(artist)
	except KeyError:
		pass
	popular = [] # a counting list of artists listened to by the n most similar users
	top_n = sorted(scores,reverse=1)[:n]
	for tup in top_n:
		# assign a weight to each top similar user (based on its similarity score)
		weight = int(tup[0]*100)
		try:
			for artist in listen[tup[1]]:
				if artist not in already_listened:
					# add each vip <weight> times to the counting list
					popular = popular + weight*[artist] 
		except KeyError:
			pass
	most_popular = [] # will contain the 10 most frequent artists from the popular list
	for popular_artist in Counter(popular).most_common(10):
		# count all frequencies in the list and form a top 10
		most_popular.append(popular_artist[0]) 
	return most_popular

def main():
	# listen = pickle.load(open("listen", "rb"))
	sim = pickle.load(open("user_sim01", "rb"))
	training = get_training()
	test = get_test()
	score = 0
	for line in test:
		user, artist = line.split()[:2]
		# get 10 recommended vips for every user
		recommended = recommend(sim, training, user, n=10)
		hit = int(artist in recommended) # determine whether the vip was predicted or not
		# print(user, vip, " ".join(most_popular), hit)
		score += hit
	print("Score: {} from {}\nPercentage: {:.2f}%".format(score, len(test), 100*score/len(test)))

if __name__ == '__main__':
	main()