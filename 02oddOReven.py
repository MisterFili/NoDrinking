#ask the user for input. Depending on wether the number is even or odd, print out an appropriate message to the user
#HINT: how do even/odd numbers react when divided by 2

usernum = int(input("Give me a number. lets see if its even or odd 	: "))
check = int(input('Give me a number to divide by:'))

if usernum % 4 == 0:
	print(usernum, "is a multiple of 4")
elif usernum % 2 == 0:
	print(usernum, 'is even')
else:
	print(usernum, 'is an odd number')