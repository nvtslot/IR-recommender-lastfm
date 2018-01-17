import pickle
import math

def get_vector(tagged, ID):
	try:
		vector = {}
		#print(tagged[ID])
		for tag in tagged[ID]:
			vector.append((int(tag),tagged[ID][tag]))
		vector.sort()
	except KeyError:
		pass
	return vector

def cosine_sim(v1, v2):
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
	ID = "2"
	#vector = get_vector(tagged, ID)
	v1 = tagged[ID]
	"""c=0
	for artist in tagged:
		if c < 4:
			print(artist)
			print(cosine_sim(v1, tagged[artist]))
		c+=1"""
	print(cosine_sim(tagged["707"], tagged["917"]))
	

if __name__ == '__main__':
	main()