import random

def average(x):
    return sum(x) / len(x)

def variance(X):
    mu = average(X)
    acc = 0
    for x in X:
        acc += (x - mu)**2
    return acc / len(X)

def standard_deviation(X):
    return variance(X)**0.5

def throw_needles(needles):
    inside = 0


    for _ in range(needles):
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])
        distance = (x**2+y**2)**0.5

        if distance <= 1:
            inside +=1
    return (4 * inside)/ needles

def estimate_pi(needles, tries):
    pis = []

    for _ in range(tries):
        pis.append(throw_needles(needles))
    
    average_pi = average(pis)
    sigma = standard_deviation(pis)
    print(f'Average: {average_pi}, sigma: {sigma}, needles={needles}')
    return (average_pi, sigma)
    
def pi(precision, tries):
    needles = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        average, sigma = estimate_pi(needles, tries)
        needles *= 2
    return average
if __name__ == '__main__':
    pi(0.01, 100)