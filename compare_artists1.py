import pickle
import math

def cosine_sim(v1, v2):
	"""Function that calculates cosine similarity between two dictionaries"""
	numer = 0
	dena = 0
	for key1 in v1:
		val1 = v1[key1]
		numer += val1*v2.get(key1,0)
		dena += val1**2
	denb = 0
	for val2 in v2.values():
		denb += val2**2
	return numer/math.sqrt(dena*denb) 


def main():
	itemsim = {}
	try:
		sim = pickle.load(open("item_sim01", "rb"))
	except FileNotFoundError:
		tagged = pickle.load(open("tagged", "rb"))
		for uid in tagged:
			itemsim[uid] = {}
			
			v1 = tagged[uid]

			for artist in tagged:

				#DONT compare same artists
				if artist != uid:
					score = cosine_sim(v1,tagged[artist])
					#only include cosine similarities higher than 0.01
					if score > 0.01:
						itemsim[uid][artist] = score

				else:
					pass
		pickle.dump(itemsim, open("item_sim01", "wb"))
		
	
	

if __name__ == '__main__':
	main()