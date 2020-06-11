import random
import pyttsx3

def userinput():




def invailid():





def sayit(thing):
    import pyttsx3
    print(thing)
    engine = pyttsx3.init()
    engine.say(thing)
    engine.runAndWait()


def simplify_text(mytext):
    badchars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '/', ';','<','>','-','_']
    mytext = mytext.lower().replace(' ', '')
    for c in badchars:
        mytext = mytext.replace(c,'')
    return(mytext)



def firstQ(count):
    sayit('what is the capitol of belgium?')
    A = simplify_text(input())
    if A == 'brussels':
        sayit('right nice')
        count = count + 1
    else:
        sayit('wrong')
    secondQ(count)

def secondQ(count):
    sayit('what is the capitol of england?')
    A = simplify_text(input())
    if A == 'london':
        sayit('yah you got it right')
        count = count + 1
    try:
        val = input()    
    else:
        sayit('wrong')
    thirdQ(count)

def thirdQ(count):
    sayit('what is the capitol of new york state')
    A = simplify_text(input())
    if A == 'albany':
        sayit('yes right')
        count = count + 1
    else:
        sayit('wrong')
    fourthQ(count)


def fourthQ(count):
    sayit('what is the capitol of new zealand')
    A = simplify_text(input())
    if A == 'wellington':
        sayit('right')
        count = count + 1
    else:
        sayit('wrong')
    fithQ(count)



def fithQ(count):
    sayit('what is the capital of the Czech Republic?')
    A = simplify_text(input())
    if A == 'prague':
        sayit('Right')
        count = count + 1
    else:
        sayit('Wrong')
    sixthQ(count)


def sixthQ(count):
    sayit('what is the catitol of oregon')
    A = simplify_text(input())
    if A == 'salem':
        sayit('right')
        count = count + 1
    else:
        sayit('wrong ')
    seventhQ(count)

def seventhQ(count):
    sayit('what is the catitol of south dakota?')
    A = simplify_text(input())
    if A == 'piere':
        sayit('right')
        count = count + 1
    else:
        sayit('wrong')
    end(count)


def end(count):
    sayit('nice your score is {} out of 7'.format(count))
    sayit('rate this game by typing a number ')
    A = int(input())
    if A > 0:
        sayit('thank you for playing I have added your score to rating to get {}'.format(A+count))
    if A == 0:
        sayit('come on you are meine')
    if A < 0:
        sayit('never mind you score is {} '.format(A))



firstQ(count = 0)
