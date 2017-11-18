#ask the user for input. Depending on wether the number is even or odd, print out an appropriate message to the user
#HINT: how do even/odd numbers react when divided by 2

#assing the users number to 'usernum'
usernum = int(input("Give me a number. lets see if its even or odd 	: "))
#assign the 'check' to the number the user pics
check = int(input('Give me a number to divide by:'))

#if number is mod by 4
if usernum % 4 == 0:
	print(usernum, "is a multiple of 4")
elif usernum % 2 == 0:
	print(usernum, 'is even')
else:
	print(usernum, 'is an odd number')

if usernum % check == 0:
	print(usernum, " divides evenly by ", check)
else:
	print(usernum, 'does not divide evenly into', check)