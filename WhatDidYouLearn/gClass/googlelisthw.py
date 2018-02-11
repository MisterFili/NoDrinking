#!/usr/bin
"""

def match_ends()
return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.

def front_x():
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
"""

list = ['a', 'b', 'c', 'lisa', 'clapping', 'looking', 'walking', 'bob', 'doctorawkward']
xlist = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

count = 0

def match_ends():
	for i in list:
		if len(i) >= 2 and i[0] == i[-1]:
			print (i)

def front_x():
	xxxlist = []
	leftoverlist = []
	for i in xlist:
	    if i.startswith('x'):
	        xxxlist.append(i)
	    else:
	    	leftoverlist.append(i)
	print(sorted(xxxlist) + sorted(leftoverlist))
	# z2a = sorted(list, reverse=True)
	# print(z2a)

def main():
	#match_ends()
	front_x()

if __name__ == '__main__':
	main()