a=input("Expression:").strip().split(" ")
if ("+" in a):
    print(round(float(a[0])+float(a[2]),1))
elif("-" in a):
    print(round(float(a[0])-float(a[2]),1))
elif("*" in a):
    print(round(float(a[0])*float(a[2]),1))
elif("/" in a):
    print(round(float(a[0])/float(a[2]),1))
