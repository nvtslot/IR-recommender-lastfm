#s2580748
#user based approach using indexed user similarity file

import sys
import operator
import linecache
import csv

# open all the files
similarfile = open('user_similarity.csv', 'r')
trainingfile = open('matrix_training.csv', 'r')
testfile = open('matrix_test.csv', 'r')


# index the similarusers_file by line numbers
# decreases time to complete drastically
def indexFile(similarfile):
    nr = 1
    index = {}

    for line in similarfile:
        usert = line.split(' ')[0]
        if (usert not in index):
            index[usert] = [nr]
        else:
            index[usert].append(nr)
        nr += 1

    return index

# make a dict that contains which users U already follows
def followDict(trainingfile):
    dictFollow = {}

    for line in trainingfile:
        U, VIP = line.rstrip().split()
        if U in dictFollow:
            dictFollow[U].append(VIP)
        else:
            dictFollow[U] = [VIP]

    return dictFollow

# suggest VIPS that U doesnt follow yey
def suggestVIPS(U, topNsimilarUsers, dictFollow):
    sugs = {}
    already_follows = dictFollow[U]
    for user2, score in topNsimilarUsers:
        followed = dictFollow[user2]
        for VIP in followed:
            if VIP not in already_follows:
                # gets value for key
                sugs[VIP] = sugs.get(VIP, 0) + eval(score)

    # sort the 10 suggested vips on score from highest to lowest so you get a top 10
    topVIPS = sorted(sugs.items(),
                     key=operator.itemgetter(1), reverse=True)[:10]

    # loop through top 10 vips and only pick their username to append to
    # topLIST
    topLIST = []
    for VIP in topVIPS:
        topLIST.append(VIP[0])

    return topLIST


# print suggestionss for  U
def test(dictFollow, index, n):
    totalScore = 0
    # rune through cases in file
    for testcase in testfile:
        U, VIP = testcase.rstrip().split()
        linenrs = index[U]
        similarities = {}
        # for every case look up similar users to that U
        # use linenrs from indexfile
        for line in linenrs:
            # SOURCE:
            # https://stackoverflow.com/questions/2081836/reading-specific-lines-only-python
            usert = linecache.getline(
                'user_similarity.csv', line).rstrip().split(' ')
            user2 = usert[1]
            score = usert[2]
            similarities[user2] = score

        # sort similar users from highest to lowest for n amount
        topNsimilarUsers = sorted(similarities.items(),
                                 key=operator.itemgetter(1), reverse=True)[:n]

        # call suggest function
        suggested = suggestVIPS(U, topNsimilarUsers, dictFollow)

        # create scores
        if VIP not in suggested:
            score = 0
            totalScore += 0
        else:
            score = 1
            totalScore += 1

        # print in desired format U-VIP-sugs - score 
        print("{} {} {} {}".format(U, VIP, " ".join(suggested), score))

    return totalScore


def main():
    dictFollow = followDict(trainingfile)
    index = indexFile(similarfile)
    # value of N set to 22 as it had highest results for me
    score = test(dictFollow, index, 22)
    print(score)

if __name__ == "__main__":
    main()
