a = input("camelCase: ").strip()
l=[]
for i in a:
    l.append(i)
v=-1
for j in l:
    u=j.isupper()
    v=v+1
    if (u==True):
        l[v]=l[v].lower()
        l.insert(v,'_')
strs=""
for i in l:
    strs+=i
print(strs)


