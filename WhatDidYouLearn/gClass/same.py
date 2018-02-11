#!/usr/bin/env python

import sys

#defines a repeat function that takes two arguments
def repeat(s, exclaim):
	result = s*3 + ' ' + 'Let\'s celebrate!'
	if exclaim:
		result = result + '!!!'
	return result

def main():
  #print('hello world', sys.argv[1])
  print repeat('Yay', True)      ## YayYayYay

if __name__ == '__main__':
  main()