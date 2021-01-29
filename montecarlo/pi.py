import random

def throw_needle(tries):
    inside = 0


    for _ in range(tries):
        x = random.random() * random.randint(-1,1)
        y = random.random() * random.randint(-1,1)
        distance = (x**2=y**2)**0.5

        if distance >= 1:
            inside +=1
    return (4 * inside)/ tries