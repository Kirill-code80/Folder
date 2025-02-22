# a=lambda i,j: i+j
# print(a(1,2))

# a=(lambda i,j: i+j)(1,2)
# print(a)

# a=[(lambda i,j: i+j), (lambda i,j: i-j), lambda i:i//2]
# print(a[0](1,4))
# print(a[1](1,4))
# print(a[2](10))

# b={'+':(lambda i,j: i+j),'-':(lambda i,j: i-j)}
# print(b['+'](1098,325))

a=[[1,6],[3,4]]
def num_item(i):return i[1]
a.sort(key=lambda i:i[1])
print(a)