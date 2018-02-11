#!/usr/bin

list = ['Green umbrella', 'Red umbrella', 'Yellow umbrella', 'umbrealla', 'towel']
print(list)

user_request = raw_input('pick from the list: ')

if user_request == 'Green umbrella':
	print ('You selected green umbrealla')
elif user_request == 'towel' :
	print('You selected a towel')
else:
	print('nothing discovered, try again')