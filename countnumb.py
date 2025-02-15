a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(end='\t')
for i in range(a,b+1):
  print(i,end='\t')
print()
for k in range(c,d+1):
  print(k, end ='\t')
  for i in range(a,b+1):
    print(k*i,end='\t')
  print()
