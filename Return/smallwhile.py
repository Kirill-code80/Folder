def small():
  a=int(input())
  index=1
  mini=a
  while True:
    a=int(input())
    if a == 0:
      return(mini,index)
    if mini > a:
      mini = a
    index+=1
print(small())
