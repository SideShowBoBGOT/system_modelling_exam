import random

distribution = [(0, 0), (2, 0.15), (4, 0.25), (6, 0.75), (8, 1)]
a = random.random()

for i in range(1, len(distribution)):
    if distribution[i][1] >= a:
        ind = i
        break

r = distribution[ind - 1][0] + (distribution[ind][0] - distribution[ind - 1][0]) / (
            distribution[ind][1] - distribution[ind - 1][1]) * (a - distribution[ind - 1][1])

print(r)
