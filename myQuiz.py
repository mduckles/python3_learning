import random
import pyttsx3

def userinput():
    pass



def invailid():
    pass




def sayinput(thing):

    print(thing)
    engine = pyttsx3.init()
    engine.say(thing)
    engine.runAndWait()


def simplify_text(mytext):
    badchars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '/', ';','<','>','-','_',"'"]
    mytext = mytext.lower().replace(' ', '')
    for c in badchars:
        mytext = mytext.replace(c,'')
    return(mytext)

def sayinput(thing, take_input=False):
    print(thing)
    engine = pyttsx3.init()
    engine.say(thing)
    engine.runAndWait()
    if take_input:
        return(simplify_text(input()))
    else:
        return("Message sent")


snark_wrong = ['thats not right',
                'you are wrong',
                'try harder',
                'ha ha big dumb',
                'are you a strawberry?',
                'have you heard of school?',
                'what do you do all day?',
                'Its totally the top google result how did you get that one wrong?',
                'nuh',
                'no no no',
                'maybe ask siri',
                'I thought you could at least get this one',
                'nope',
                'so so wrong',
                'I am disappointed',
                'wrong, wrong, yup, still wrong',
                'did you even try?',
                'really this is what I expected']
snark_right = ['you so smart',
                'wow, you are special',
                'you got it',
                'my my I am impressed',
                'you are so smart, where do you go to school?',
                'you got it, I am suprised',
                'nice! did you google that?',
                'Wikipedia told you that',
                'You get a gold star',
                'Yes! Do you want a biscuit.',
                'Yup, but you don\'t get any lollies',
                'oooh look at you!',
                'oh my! I was sure I would stump you. Nice job!'
                ]

'''
Example of YAML
- question: my question
  answer: my answer
- question: another question
  answer: the answer
'''


questions = [ dict(question = "what is the capital of belgium ",
                    answer = "brussels"),
                    dict(question = "what is the capitol of england? ",
                        answer = "london"),
                    dict(question = "what is the capitol of new york state ",
                        answer = "albany"),
                    dict(question = "what is the capitol of new zealand ",
                        answer = "wellington"),
                    dict(question = "what is the capital of the Czech Republic? ",
                        answer = "prague"),
                    dict(question = "what is the catitol of oregon ",
                        answer = "salem"),
                    dict(question = "what is the catitol of south dakota? ",
                        answer = "piere"),
                    dict(question = "Who shot the Archduke Ferdinand in 1914? ",
                         answer="gavriloprincip"),
                    dict(question = "What century did Māori first arrive in New Zealand",
                        answer = "14th"),
                    dict(question = "What is the meaning of life the universe and everything?",
                    answer = "42"),
                    dict(question = "What is the vulcan salute?",
                    answer = "livelongandprosper" ),
                    dict(question = "In what year did Isaac Newton die?",
                        answer = "1727"),
                    dict(question = "What element are you poisoned by if you're 'Mad as a hatter?'",
                        answer = "mercury"),
                    dict(question = "What is the air speed velocity of an unladen swallow?",
                    answer = "africanoreuropean"),
                    dict(question = "How much wood could a wood chuck chuck if a wood chuck could chuck wood?",
                        answer = "asmuchasitcouldchuck"),
                    dict(question = "Who is burried in Grant's tomb?",
                        answer = "grant"),
                    dict(question = "Who was the first prime minister of new zealand?",
                        answer = "henrysewell"),
                    dict(question = "Who invented the cotton gin?",
                        answer = "eliwhitney")

                    ]


def question(question, answer, count):
    A = sayinput(question, take_input=True)
    if A == answer:
        sayinput(random.choice(snark_right))
        count = count + 1
    else:
        sayinput(random.choice(snark_wrong))
    return(count)


def end(count):
    sayinput('nice your score is {} out of 7'.format(count))
    sayinput('rate this game by typing a number ')
    A = int(input())
    if A > 0:
        sayinput('thank you for playing I have added your score to rating to get {}'.format(A+count))
    if A == 0:
        sayinput('come on you are meine')
    if A < 0:
        sayinput('never mind you score is {} '.format(A))


def rungame():
    count = 0
    random.shuffle(questions)
    for q in questions[0:5]:
        count = question(q['question'], q['answer'], count)
        print('Your score is {} out of 5'.format(count))
    end(count)

rungame()




def end(count):
    sayinput('nice your score is {} out of 7'.format(count))
    sayinput('rate this game by typing a number ')
    A = int(input())
    if A > 0:
        sayinput('thank you for playing I have added your score to rating to get {}'.format(A+count))
    if A == 0:
        sayinput('come on you are meine')
    if A < 0:
        sayinput('never mind you score is {} '.format(A))



#firstQ(count = 0)
