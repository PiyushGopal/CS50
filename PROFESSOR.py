import random
def main():
    lvl = get_level()
    count = 0
    for _ in range(10):
        i = 3
        while(i>0):
            if i==3:
                x = generate_integer(lvl)
                y = generate_integer(lvl)
            print(x,"+",y,"= ",end="")
            m = input()
            if m.isdigit():
                if int(m)==x+y:
                    count += 1
                    break
                else:
                    print('EEE')
            else:
                print('EEE')
            i -= 1
        if i==0:
            print(x,"+",y,"=",x+y)
    print('Score:',count)
def get_level():
    x= input("Level: ")
    if x.isdigit():
        if 1<=int(x) and int(x)<=3:
                return int(x)
        else:
            get_level()
    else:
        get_level()
def generate_integer(lvl):
    if lvl == 1:
        return random.randint(0,9)
    elif lvl == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)
if __name__=="__main__":
    main()
