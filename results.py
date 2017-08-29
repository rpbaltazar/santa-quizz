#!/usr/bin/python3
import re

# Part 1
# The first part checks how many vowels there are in each
# string. Therefore, it checks every letter and when it finds
# a vowels it increments the counter. 
# The second property is found using a regex, which checks
# if there is at least a pair of the same letter. The last property
# is found by simply checking if there are the unwanted srings.

#fone = open("output_1", "w")

vowels = ["a", "e", "i", "o", "u"]

firstCounter = 0
with open("input") as in_file:
	for row in in_file:
		count_vowels = 0
		for r in row:
			if r in vowels:
				count_vowels += 1

		repLet = re.search( r'([a-z])\1', row)
		if(repLet and count_vowels >= 3 and (("ab" not in row) and ("cd" not in row) and ("pq" not in row) and ("xy" not in row))):
			#fone.write(row.rstrip() + "\n")
			firstCounter += 1

#fone.close()

in_file.close()

print("The nice strings in the first part are " + str(firstCounter))

# Part 2
# The second part splits each row in pairs 
# and checks if exists another pair with the same
# letters, in case they don't overlap (aaa), or 
# they are in same position (same pair). The second 
# property is found when two pairs next to each other 
# have the same last and first letters.

#ftwo = open("output_2", "w")

pairs = []
secondCounter = 0
with open("input") as in_file:
	for row in in_file:
		i = 0
		while (i < len(row)-1):
			pair = row[i] + row[i+1]
			pairs.append((pair,i, i+1)) 
			i += 1

		pairFound = False
		for i in range(len(row)-1):
			for j in range(len(row)-2):
				p = row[j] + row[j+1]
				if(p == pairs[i][0] and pairs[i][0][0] != pairs[i+1][0][1] and pairs[i][1] != j and pairs[i][2] != j+1 and not pairFound):
					pairFound = True

		
		found = False
		for i in range(len(row)-2):
			if(pairs[i][0][0] == pairs[i+1][0][1] and not found):
				found = True


		if(pairFound and found):
			#ftwo.write(row.rstrip() + "\n")
			secondCounter += 1

		pairs = []

#ftwo.close()

in_file.close()

print("The nice strings in the second part are " + str(secondCounter))
