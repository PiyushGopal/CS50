a=input("What time is it?")
h,m=map(int,a.split(":"))
if ((h==7 or h==8) and m<=59 and m>=00):
    print("breakfast time")
elif((h==12 or h==13) and m<=59 and m>=00):
    print("lunch time")
elif((h==18 or h==19) and m<=59 and m>=00):
    print("dinner time")
