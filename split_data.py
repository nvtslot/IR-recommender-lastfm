from random import shuffle

def main():
	with open("user_artists.dat","r") as data:
		lines = data.readlines()[1:]
		split = 0.1
		shuffle(lines)
		cutoff = int(len(lines) * split)
		test, train = lines[:cutoff], lines[cutoff:]

	with open("test.dat", "w") as f:
		for line in test:
			f.write(line)

	with open("train.dat", "w") as f:
		for line in train:
			f.write(line)



if __name__ == '__main__':
	main()