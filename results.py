#!/usr/bin/python3
import re

vowels = ["a", "e", "i", "o", "u"]

def vowelCount(line):
	if line[0] in vowels:
		counter = 1
	else:
		counter = 0

	for i in range(1,len(line)):
		if line[i] in vowels:
			counter += 1
	
	return counter


def pairCheck(line):
	if(("ab" in line) or ("cd" in line) or ("pq" in line) or ("xy" in line)):
		return False
	else:
		return True


def pairBuilder(line):
	pairsFun = []
	for i in range(len(line)-1):
		pair = line[i] + line[i+1]
		pairsFun.append((pair,i, i+1)) 

	return pairsFun


def doublePairs(pairs, line):
	pairFound = False
	for i in range(len(line)-1):
		for j in range(len(line)-2):
			p = line[j] + line[j+1]
			if(p == pairs[i][0] and pairs[i][1] != j and pairs[i][2] != j+1 and not pairFound):
				pairFound = True

	return pairFound


def alternatedPairs(pairs, line):
	found = False
	for i in range(len(line)-2):
		if(pairs[i][0][0] == pairs[i+1][0][1] and not found):
			found = True

	return found

def firstProblem():
	firstCounter = 0
	with open("input") as inFile:
		for row in inFile:
			vowelsCount = vowelCount(row)

			repLet = re.search( r'([a-z])\1', row)
			stringCheck = pairCheck(row)
			if(repLet and vowelsCount >= 3 and stringCheck):
				firstCounter += 1

	inFile.close()

	print("The nice strings in the first part are " + str(firstCounter))


def secondProblem():
	secondCounter = 0
	with open("input") as inFile:
		for row in inFile:
			
			pairs = pairBuilder(row)

			doublePairsFound = doublePairs(pairs, row)

			alternatedPairsFound = alternatedPairs(pairs, row)
			
			found = False
			for i in range(len(row)-2):
				if(pairs[i][0][0] == pairs[i+1][0][1] and not found):
					found = True

			if(doublePairsFound and alternatedPairsFound):
				secondCounter += 1

			
	inFile.close()

	print("The nice strings in the second part are " + str(secondCounter))


		

def main():
	# Part 1
	# The first part checks how many vowels there are in each
	# string. Therefore, it checks every letter and when it finds
	# a vowels it increments the counter. 
	# The second property is found using a regex, which checks
	# if there is at least a pair of the same letter. The last property
	# is found by simply checking if there are the unwanted srings.

	firstProblem()

	# Part 2
	# The second part splits each row in pairs 
	# and checks if exists another pair with the same
	# letters, in case they don't overlap (aaa), or 
	# they are in same position (same pair). The second 
	# property is found when two pairs next to each other 
	# have the same last and first letters.
	
	secondProblem()


if __name__ == "__main__":
    main()

