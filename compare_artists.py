import pickle
from cosine_sim import cosine_sim

def main():
	tagged = pickle.load(open("tagged", "rb"))
	ID = "420"
	v1 = tagged[ID]
	c=0
	for artist in tagged:
		if c < 4:
			print(artist)
			print(cosine_sim(v1, tagged[artist]))
		c+=1

if __name__ == '__main__':
	main()