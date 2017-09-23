#!/usr/bin/python3

# Both solutions have a linear complexity O(n). 
# They are aimed to be more memory intensive rather than CPU intensive. 

# Outcome: 238 strings are accepted
def prop_one(inp_str):

    # Immutable set of vowels (HashSets)
    vowels_set   = frozenset(['a','e','i','o','u'])
    banned_pairs = frozenset(['ab', 'cd', 'pq','xy'])

    # Greedy return based on the string length
    if len(inp_str) < 3:
        return False
    
    # Greedy initialization of vowels counter it takes sense when you look at following the for loop
    vows = 1 if inp_str[0] in vowels_set else 0
    double = False # double letters condition initialization

    for i in range(1,len(inp_str)):
        # Greedy return as soon as a banned pair appears
        if inp_str[i-1:i+1] in banned_pairs:
            return False

        # if we met already a consecutive letter skip avoiding the 
        # comparison and eventually a new useless assignment (exploits python's short circuited conditional expressions)
        if not double and inp_str[i-1] == inp_str[i]:
            double = True

        # Is the letter a vowel?
        if inp_str[i] in vowels_set:
            vows+=1

    # are both condition evaluated true at the same time? the boolean expression will give the answer! ;)
    return  vows > 2 and double


# Outcome: 69 strings are accepted
def prop_two(inp_str):

    # Greedy return based on the string length
    if len(inp_str) < 4:
        return False

    pairs = {inp_str[0:2]:0} # Python's dictionary (HashMap) initialization with the first pair
    pair_of_letters = False  # Initialization of the pair condition
    one_in_between = inp_str[0] == inp_str[2] # let's take an advantage :D 

    for i in range(1,len(inp_str)-1):
        # selects the current pair to be analyzed
        curr_pair = inp_str[i:i+2]

        # if no previous pairs found and if the pair is already seen without overlapping 
        # (takes sense for loooooong strings, it avoids to check back the whole string every time if needed just checks an hash)
        if not pair_of_letters and curr_pair in pairs and pairs[curr_pair] != i-1:
            # then we found it! 
            pair_of_letters = True
 
        # note we do not use else
        if not pair_of_letters and curr_pair not in pairs:
            pairs[curr_pair] = i

        # again short circuited AND 
        if not one_in_between and inp_str[i-1] == inp_str[i+1]:
            one_in_between = True

    # are both condition evaluated true at the same time? the boolean expression will give the answer! ;)
    return pair_of_letters and one_in_between


# Main function makes use of python's generators (no memory wasting PEP-289 worth to check!) 
def main():

    with open('input','r') as inFile:
        res_list = (prop_one(line.strip()) for line in inFile)
        print ("Ex1: The number of accepted strings is: {}".format(sum(x for x in res_list)))

    with open('input','r') as inFile:
        res_list = (prop_two(line.strip()) for line in inFile)
        print ("Ex2: The number of accepted strings is: {}".format(sum(x for x in res_list)))


# Standard Python Style main
if __name__ == "__main__":
    main()
