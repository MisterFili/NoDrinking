#listOverlap
'''
write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

class_attendance = ['me', 'myself', 'and', 'eye']

name = input('type a name to check: ')
if name in class_attendance:
	print(' {}, this person is enrolled'.format(name))
else:
	print('{}, did not show up to class'.format(name))
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = [random.randint(1,80)]


for item in a:
	if item in b and item not in c:
		c.append(item)
			
print(c)