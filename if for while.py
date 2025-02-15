a=100
b=1000
for i in range(1,10):
  print(a,b)
a=a//b
b=a-b
for i in range(b,a):
  print(i)
  a=a-b
  b=b-a
  if a > b:
    print("a>b")
    a=100-a
    b=1000-b
  if a < b:
    print("a<b")
    a=1000-a
print(a,b)
