from random import *
x = input("Level: ")
while(True):
    if x.isdigit() and int(x)>0:
        break
    else:
        x = input("level: ")
r = randint(1,int(x))
y = input("Guess: ")
while(True):
    if(y.isdigit() and int(y)>0):
        if int(y)==r:
            print("Just right!")
            break
        elif int(y)>r:
                print("Too large!")
                y=input("Guess: ")
        elif int(y)<r:
            print("Too small!")
            y=input("Guess: ")
    else:
        y=input("Guess: ")
