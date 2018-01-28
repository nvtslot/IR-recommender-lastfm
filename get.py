import pickle

def get_usersim():
	return pickle.load(open("user_sim01", "rb"))

def get_itemsim():
	return pickle.load(open("item_sim50", "rb"))

def get_friends():
	try:
		return pickle.load(open("friends", "rb"))
	except FileNotFoundError:
		friends = {}
		with open("user_friends.dat", "r", encoding='utf-8', errors='ignore') as data:
			for line in data.readlines()[1:]:
				user, friend = line.strip().split()
				try:
					friends[user][friend] = True
				except KeyError:
					friends[user] = {}
					friends[user][friend] = True
				try:
					friends[friend][user] = True
				except KeyError:
					friends[friend] = {}
					friends[friend][user] = True	
		pickle.dump(friends, open("friends", "wb"))
		return friends

def get_train():
	"""Opens training dataset"""
	with open("train.dat","r") as data:
		train = {}
		for line in data.readlines():
			user, artist, count = line.strip().split("\t")
			try:
				train[user][artist] = int(count)
			except KeyError:
				train[user] = {}
				train[user][artist] = int(count)
	return train

def get_test():
	"""Opens test dataset"""
	with open("test.dat","r") as test:
		return test.readlines()