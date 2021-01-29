import random

from average import average
from variance import variance, standard_deviation

X = [random.randint(9,12) for i in range(20)]

print(X)
print(f'Average: {average(X)}')
print(f'Variance: {variance(X)}')
print(f'Standard deviation: {standard_deviation(X)}')