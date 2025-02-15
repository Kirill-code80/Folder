p=0
sum=0
max=0
min=1000
while p!=6:
  a=float(input())
  sum=sum+a
  if a > max:
    max=a
  if a < min:
    min=a
  p=p+1
print(max)
print(min)
print(round(max,2))
print(round(min,2))
e=sum/6
print(e)
  
