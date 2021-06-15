import random

d = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]
d.append(d[0])
random.shuffle(d[2])
d.append(d[1])
random.shuffle(d[3])
