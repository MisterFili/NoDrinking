#ask the user for a string and print outwhether this string is a 
#palindrome or not. 
	
def main():
	palindromeQuestion = str(input('Hello, type out a word and lets see if its a palindrome: '))
	
	rvs=palindromeQuestion[::-1]

	if palindromeQuestion == rvs:
		print('{} is a palindrome'.format(palindromeQuestion))
	else:
		print('{} is not a palindrome'.format(palindromeQuestion))

main()