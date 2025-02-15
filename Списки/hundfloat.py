import random
lst=[]
for i in range(100):
  a=(random.random())
  lst.append(round(a,2))
lst.sort()
print(lst)
def ten():
  i=0
  while i != 100:
    print(lst[i:i+10])
    i=i+10

ten()

