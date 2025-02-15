a=['один','два','три','четыре','пять']

r1=open('one.txt')
r2=open('oneRU.txt','w')

f=r1.read()     
f=f.split()

for i in range(len(f)):
    f[i]=a[i]
    r2.write(a[i])
    r2.write(' ') 
r1.close()
r2.close()
