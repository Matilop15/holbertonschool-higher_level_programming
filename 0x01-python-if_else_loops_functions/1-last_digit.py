#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numb = -number
    digito = numb % 10
    digito = -digito
else:
    digito = number % 10

if digito > 5:
    print('Last digit of',number, 'is', digito, 'and is greater than 5')
elif digito == 0:
    print('Last digit of',number, 'is', digito, 'and is 0')
else:
    print('Last digit of',number, 'is', digito, ' and is less than 6 and not 0')
