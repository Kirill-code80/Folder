a="Я обожаю петь, играть и танцевать"
lst=[]
i=0
while True:
  i=a.find(" ")
  if i==-1:
    lst.append(a)
    break
  lst.append(a[:i])
  a=a[i+1:]
print(lst)
