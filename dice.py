import sys

sides = sys.argv[1]
n_rolls = sys.argv[2]

def rolldie(sides=6):
    import random
    sides = int(sides)
    return(random.randint(1,sides))

def rolls(n_rolls):
    n_rolls = int(n_rolls)
    for i in range(0,n_rolls):
        print(rolldie(sides))

rolls(n_rolls)

