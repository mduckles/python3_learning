import random
import time


blah

def sayit(thing):
    import subprocess
    print(thing)
    subprocess.run(['say', thing])

def simplify_text(mytext):
     return(mytext.lower().replace(' ', '') )

def firstQ(count):
    sayit('what is the best pll')
    A = simplify_text(input())
    if A == 'jperm':
        sayit('right')
        count = count + 2
    else:
        sayit('WRONG!')
        count = count - 1
    secondQ(count)


def secondQ(count):
    sayit('is aubry a strawberry')
    A = simplify_text(input())
    if A == 'no':
        sayit('right you good')
        count = count + 2
    if A == 'yes':
        sayit('wrong you bad')
        count = count - 1
    thirdQ(count)


def thirdQ(count):
    sayit('Raiders axe or Aspect of the end?')
    A = simplify_text(input())
    if A == 'raidersaxe':
        sayit('yes you smart')
        count = count + 2
    else:
        sayit('no you big dumb')
        count = count - 1
    fourthQ(count)

def fourthQ(count):
    sayit('what state or city is the the capital of the usa ')
    A = simplify_text(input())
    if A == 'washingtondc':
        sayit('yes. it is not a state')
        count = count + 2
    else:
        sayit('no its not even a state')
        count = count - 1
    fithQ(count)

def fithQ(count):
    sayit('what is the derivative x ? it is a intger')
    A = int(input())
    if A == 1:
        sayit('right yay derivatives')
        count = count + 2
    else:
        sayit('WRONG you stupid')
        count = count - 1
    end(count)

def end(count):
    sayit('do you want to see your score? say no or yes')
    A = simplify_text(input())
    if A == 'yes':
        sayit('your score is {count} out of 10 good luck next time'.format(count=count))
    else:
       sayit('good luck next time')

firstQ(count = 0)
