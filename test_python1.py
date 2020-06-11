import random

def sayit(thing):
    import subprocess
    print(thing)
    subprocess.run(['say', thing])

#makeinag a random number

def setgame():
    sayit('what is the lower number?')
    lowernum = int(input())
    sayit('what is the  higher number?')
    highernum = int(input())
    target = random.randint(lowernum, highernum)
    return(target)

def playgame():
    target = setgame()
    sayit('what is your guess')
    guess = int(input())
    count = 1
    while 1:
        if guess > target:
            sayit('the number is lower')
            guess = int(input())
            count = count + 1
        elif guess < target:
            sayit('the number is higher')
            guess = int(input())
            count = count + 1
        elif guess == target:
            sayit('you got it yay')
            sayit('it took you {count} trys'.format(count=count))
            break

playgame()
