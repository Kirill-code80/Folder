def longword(d):
    f1=open(d)
    e=f1.readlines()
    max1='разошлись'
    col = len(max1)
    for i in e:
        if len(i)>len(max1):
            max1=i
            col = len(i)
    print(max1)

longword('article.txt')
        
