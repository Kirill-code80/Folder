a=5
b=6
c=3
d=4
if a > d and c > b:
  c=c-1
  d=d-1
if a < d and c < b:
  a=a-1
  b=b-1
for i in range(10,100):
  while c > -100 and d > -100:
    a=c-d
    d=c-10
    c=a-b
    b=a+10
    a=10-a
    c=100+a
print(a,b,c,d)

  
