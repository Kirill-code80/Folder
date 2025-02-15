from random import randint
lst=[]
for i in range(0,11):
  if i % 2 != 1 or i == 1:
    y=randint(0,10)
    for j in range(y):
      r=randint(0,len(lst))
      lst.insert(r,i)
print(lst)
