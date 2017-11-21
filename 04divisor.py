response = int(input('enter a number to see its divisors: '))
#input is stored in range funciton for dividing
x = range(1,response+1)
#create empty divisor list
a = []
#for each number in range of 1 to userinput
for i in x:
#if user input is divisible by range given evenly, append to empty list
	if response % i == 0:
		a.append(i)
print(a)