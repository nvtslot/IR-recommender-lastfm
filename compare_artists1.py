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

	tagged = pickle.load(open("tagged", "rb"))
	for uid in tagged:
		
		v1 = tagged[uid]

		for artist in tagged:
			#DONT compare same artists
			if artist != uid:
				#only include cosine similarities higher than 0.01
				if cosine_sim(v1,tagged[artist]) > 0.01:
					print(uid,artist, cosine_sim(v1,tagged[artist]))
			else:
				pass
		
	
	

if __name__ == '__main__':
	main()