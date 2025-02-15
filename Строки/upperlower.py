r=0
t=0
a=str(input())
for i in range(len(a)):
  print(a[i].isupper())
  if a[i] == " ":
    print("")
  if a[i].isupper():
    r+=1
  else:
    t+=1
    
if r > t:
  print(a.upper())
else:
  print(a.lower())
  
  
