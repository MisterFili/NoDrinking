#ask for daily response

response = input('how was your day? ')

#next level part of the program.
#if respose is shorter than 7 characters ask for more input

if response == 'not good':
    print(' sorry, sad face')
else:
	response2 = input('come on, you can say more than that! ')

print('See, I knew you could\'ve said  more than \"{}\"'.format(response))
