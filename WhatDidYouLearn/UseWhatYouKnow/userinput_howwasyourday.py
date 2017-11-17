#ask for daily response

response = input('how was your day? ')


if response == 'not good':
    print(' sorry, sad face')
else:
	response2 = input('come on, you can say more than that! ')

print('I knew you could more than \"{}\"'.format(response))
