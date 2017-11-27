def main():
	wrds = str(input('enter a word. we will test for palindrome: '))
	is_it = (wrds.strip()).lower()
	print(palindrome(is_it))

def palindrome(list):
	list_rev = list[::-1]
	return (list_rev == list)

if __name__ == '__main__':
	main()