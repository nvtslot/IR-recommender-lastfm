import pickle
from cosine_sim import cosine_sim

def get_listen():
	try:
		return pickle.load(open("listen", "rb"))
	except FileNotFoundError:
		listen = {}
		with open("user_artists.dat", "r") as data:
			for line in data.readlines()[1:]:
				user, artist, count = line.strip().split("\t")
				try:
					listen[user][artist] = int(count)
				except KeyError:
					listen[user] = {}
					listen[user][artist] = int(count)
		pickle.dump(listen, open("listen", "wb"))
		return listen

def main():
	listen = get_listen()
	try:
		sim = pickle.load(open("user_sim01", "rb"))
	except FileNotFoundError:
		sim = {}
		for u1 in listen:
			sim[u1] = {}
			for u2 in listen:
				if u1 != u2:
					score = cosine_sim(listen[u1],listen[u2])
					if score > 0.01:
						sim[u1][u2] = score
		pickle.dump(sim, open("user_sim01", "wb"))
	
	total = 0 # count the total amount of similarity relations
	for u1 in sim:
		for u2 in sim[u1]:
			total += 1
	print(total)

	"""u1 = "2"
	for u2 in sim[u1]:
		score = sim[u1][u2]
		if score > 0.3:
			print(u2, score)"""


if __name__ == '__main__':
	main()