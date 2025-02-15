a={1:'What',2:'is',3:'your',4:'name'}

f = []
v = []
for key,value in a.items():
    f.append(key)
    v.append(value)
f.reverse()
v.reverse()
d = dict.fromkeys(f)
for i in range(len(v)):
    d[i+1] = v[i]
print(d)
