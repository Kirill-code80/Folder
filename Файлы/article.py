def read_last(g,d):
    f1=open(d)
    e=f1.readlines()
    w=len(e)
    e=e[w-g:w]
    f1.close()
    print(e)
g = int(input())
while g <=0:
    g=int(input())
read_last(g,'article.txt')
