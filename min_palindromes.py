import sys
import numpy as np

#The main method interprets a user input, or uses a default input_string,
#and calculates the minimum number of palindromes contained in the input_string 
#
#Run Time: O(n^2 + n^2) = O(n^2)
############################################################
def main():
	global input_string
	global input_size	
	
	if len(sys.argv) == 1:
		input_string = "abbaddde"
		input_size = len(input_string)
		sys.stderr.write("Using default input_string: " + input_string + "\n")
	else:
		input_string = sys.argv[1]
		input_size = len(input_string)	
		if(input_size == 1):
			sys.stdout.write("You silly goose, obviously the answer is: 1\n")
		elif(input_size < 1000):
			sys.stdout.write("Using user specified input_string: \n" + input_string)
		else:
			sys.stdout.write("Using user specified input_string of length: " + len(str(input_string)) + " characters.")
	
	recursive_palindrome_finder(input_string)
############################################################

#Simpley calls the two methods:
#    1. find_palindromes(input_string): Finds the location of every
#       palindrome in: input_string
#	 2. iterative_solver(p): Using locations of all palindromes to
#	    determine minimum number of palindromes
############################################################
def recursive_palindrome_finder(input_string):		
	p = find_palindromes()
	answer = iterative_solver(p)
	sys.stdout.write("The minimum number of palindromes in the input_string is: " + str(answer + 1) + "\n")
############################################################

#Constructs the upper triangular matrix P which is an element of Real(input_size x input_size)
#with boolean values indicating the positions of all palindromes in input_string
#
#Run Time: O(n^2)
############################################################
def find_palindromes():
	P = np.array([[None]*input_size]*input_size)
	for i in range(0, input_size):
		P[i][i] = True
	for j in range(2, input_size+1):
		for start in range(0, input_size - j + 1):
			end = j + start - 1
			if (j == 2):
				P[start][end] = (input_string[start] == input_string[end])	
			else:
				P[start][end] = (input_string[start] == input_string[end]) and (P[start+1][end-1])
	return P
############################################################


#Iterates through the input input_string and  determines the minimum 
#number of palindromes
#
#Run Time: O(n^2)
############################################################
def iterative_solver(P):
	min_cut = np.array([None]*input_size)
	for i in range (0, input_size):
		if (P[0][i] == True):
			min_cut[i] = 0;
		else:
			min_cut[i] = sys.maxint
			for j in range(0, i):
				if((P[j+1][i] == True) and (1 + min_cut[j] < min_cut[i])):
					min_cut[i] = 1 + min_cut[j]
	return min_cut[input_size-1]
############################################################

#Simple palindrome qualifier
############################################################
def is_palindrome(s):
	if s == s[::-1]:
		return 1
	else:
		return 0

main()
