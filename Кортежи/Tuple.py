import random
p=tuple(random.randint(0,5)for i in range(10))
t=tuple(random.randint(-5,0)for i in range(10))
u=p+t
print(u)
print(u.count(0))
