import random

print('What is your name?')

name = input()

print('Hello, %s' % name)

print('Rolling dice...')

nums = [1, 2, 3, 4, 5, 6]

die1 = random.choice(nums)
print('Die 1: %.0f'%die1)
die2 = random.choice(nums)
print('Die 2: %.0f'%die2)

sum = die1+die2
print('Total value: %.0f'%sum)

if sum > 7:
    print('%s won.' % name)
else:
    print('%s lost.' % name)