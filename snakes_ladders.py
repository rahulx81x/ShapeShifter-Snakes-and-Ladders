import random
Snakes = []
Ladders = []


def check1(no, list1, list2):
    if (no in list1) or (no in list2):
        no += 1
        no = check1(no, list1, list2)
    return no


for i in range(10):
    temp = random.randint(6, 97)
    temp = check1(temp, Snakes, Snakes)
    Snakes.append(temp)

for j in range(10):
    temp = random.randint(10, 90)
    temp = check1(temp, Ladders, Snakes)
    Ladders.append(temp)
Counter = [1, 2, 3, 4, 5, 6, 7, 8, 9]


