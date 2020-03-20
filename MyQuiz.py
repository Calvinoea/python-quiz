import time

score = 0

name = str(input("What's your name?"))
print("Welcome, "+name+"to the quiz!\n")

def scorePlus():
    global score
    score+= 1
    print("Your score:",score)

def scoreMinus():
    global score
    score -=1
    print("Your score:", score)



def q1():
    global score
    print("1. What is Elon Capitan?\n")
    time.sleep(0.5)
    print("a) An operating system for Windows")
    print("b) An operating system for Mac")
    print("c) A third-party application")

    answer = str(input("What's the right answer?:"))

    if answer == "b":
        print("Well done, that's correct!")
        scorePlus()
    
    else:
        print("You are wrong")
        scoreMinus()



    q2()
def q2():
    global score
    print("1. What is Bitcoin?\n")
    time.sleep(0.5)
    print("a) A cryptocurrency")
    print("b) A machine made by aliens")
    print("c) A new way of making coffee")

    answer = str(input("What's the right answer?:"))

    if answer == "b":
        print("Well done, that's correct!")
        scorePlus()
    else:
        print("You are wrong")
        scoreMinus()

    q3()
def q3():
    global score
    print("1. What is PayPal?\n")
    time.sleep(0.5)
    print("a) A great way of sending money")
    print("b) A friend that pays you money")
    print("c) A robot")

    answer = str(input("What's the right answer?:"))

    if answer == "b":
        print("Well done, that's correct!")
        scorePlus()
    else:
        print("You are wrong")
        scoreMinus()



q1()
