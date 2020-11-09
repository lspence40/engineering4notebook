# automatic dice roller
# written by luuk spencer
print("automatic dice roller")

from random import randint
a = 0

while a != 'x':
	a = input()
	print(randint(1,6))
