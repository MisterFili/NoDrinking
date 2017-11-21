#practice making list

response = int(float(input('enter a number to see what it is divisible by: ')))
e = []

for i in range(0,100,response):
	e.append(i)
print(e)