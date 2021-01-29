from average import average

def variance(X):
    mu = average(X)
    acc = 0
    for x in X:
        acc += (x - mu)**2
    return acc / len(X)

def standard_deviation(X):
    return variance(X)**0.5