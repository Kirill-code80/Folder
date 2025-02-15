s1 = 'abcd'
s2 = '01'
u=[]
for i in s1:    
    for j in s2:
        t=(i+j)
        u.append(t)
print(u)
# [i+j for i in s1 for j in s2]
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=[]
for i in a:
    if i %2==0:
        print(i)
        b.append(i)
print(b)
# >>> [i for i in a if i%2==0]
d = [1, 2, 3]
e = [4, 5, 6]
f=[]
for i in d:
    for j in e:
        if i*j <=10:
            r=(i,j)
            f.append(r)
print(f)
            
# >>> [(i,j) for i in d for j in e if i*j <= 10]