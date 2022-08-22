a=input("Input:").strip()
for i in a:
    if (i in ['a','e','i','o','u','A','E','I','O','U']):
        a=a.replace(i,'')
print(a)
