x = input("Name: ")
l = []
while(x):
    l.append(x)
    x = input("Name: ")
if(len(l)==1):
    print("Adieu, adieu, to",l[0])
else:
    if len(l)==2:
        print("Adieu, adieu, to",l[0],'and',l[1])
    else:
        string =l[0]+','+' '
        for i in l[1:len(l)-1]:
            if l.index(i)!=len(l)-2:
                string += i+','+' '
            else:
                string += i
        print("Adieu, adieu, to",string,'and',l[len(l)-1])
