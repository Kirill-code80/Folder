r=[]
a=input()
r.append(a)
while a != 'stop':
    a=input()
    if a not in r:
        r.append(a)
    elif a in r:
        print("Duplicate!")
print(r)
