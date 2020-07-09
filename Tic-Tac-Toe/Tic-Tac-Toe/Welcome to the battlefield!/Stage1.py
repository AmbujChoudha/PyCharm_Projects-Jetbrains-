import random

states = ['O', 'X']
for i in range(3):
    # choices creates a list, key or length = 3
    # joining the list to create a string
    x = ''.join(random.choices(states, k=3))
    print(x)
