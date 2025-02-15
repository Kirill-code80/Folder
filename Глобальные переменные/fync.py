sum=0
def whil():
  a=int(input())
  global sum
  sum=sum+a
  while a!=0:
    a=int(input())
    sum=sum+a
    if a==0:
      print(sum)
      break
    
whil()
