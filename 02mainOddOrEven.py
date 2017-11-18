#rewriting program so we can import into other programs

def main():
    import sys

#get user input
    str = input('give me a number: ')
#force user input into a string
    num = int(float(str))

#is the number odd or even
    if num % 2 == 0:
    	print('{} is even'.format(num))
    else:
    	print('{} is odd'.format(num))

    if num % 4 == 0:
    	print('and your number is divisible by 4')
    

    print('\nwe will now be dividing your inputs. Numerator by denominator.\n')
    numerator = int(float(input('enter a numerator: ')))
    denominator = int(float(input('enter a denominator: ')))
    answer = numerator/denominator
    if denominator == 0:
    	print('You cannot divide by 0. \nGoodbye!')
    	sys.exit()
    else:
    	if numerator % denominator == 0:
    		print('\n{} divides evenly into {}'.format(numerator, denominator))
    	else:
    		print('{} does not divide evenly into {}'.format(numerator, denominator))
    print('\nAlso, {} divid by {} equals {}'.format(numerator, denominator, answer))

if __name__ == '__main__':
    main()