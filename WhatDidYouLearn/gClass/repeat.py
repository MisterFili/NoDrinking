#!/usr/bin/env python
from time import sleep

squares = [2, 4, 6, 8, 10]
def forN():
  sum = 0
  for i in squares:
    sum += i
  print sum

def heythere():
  name = raw_input('what is your firt name? ')
  last = raw_input('Thanks, and your last name? ')
  print('processing.' +  '.' )
  sleep(2)
  print('Hey there, %s %s') % (name, last)

def main():
  forN()
 # heythere()
  
if __name__ == '__main__':
  main()
