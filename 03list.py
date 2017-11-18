#working with list

list0 = [66,3,2,34,55,22,85,675,66,654,80,90,41,0]
list1 = []

print('{}\nThis is the list we will be working with today\n'.format(list0))
response = int(float(input('enter a number: ')))

for i in list0:
    if i < response:
        list1.append(i)
print('These numbers {} are less than {}'.format(list1,response))
