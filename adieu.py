import sys
import inflect
p = inflect.engine()

namesList = []
#piyushgopal
while True:
    try:
        names = input("Name: ").title()
        if len(names) < 1:
            sys.exit()
        #piyushgopal
        namesList.append(names)
        output = p.join(namesList)
#piyushgopal
    except EOFError:
        print('\n')
        print("Adieu, adieu, to " + output)
        break
    else:
        continue
