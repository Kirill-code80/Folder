lst=[1,3,5,3,6,7,5,8,6,3,9]
lst=sorted(lst)
k=0
for i in lst:
    if i==k:
        continue
    t=lst.count(i)
    k=i
    print(i,t,sep=" ")
    
