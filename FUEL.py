while True:
    try:
        y =list(map(int,input("Fraction:").split('/')))
        if(y[0]>y[1]):
            continue
        break
    except (ValueError , ZeroDivisionError):
        pass

a=(y[0]/y[1])
b=a*100
c=round(b)

if (c >= 99):
    print("F")
elif (c <= 1):
    print("E")
else:
    print(f"{c}%")
