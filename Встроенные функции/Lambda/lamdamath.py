b = {'+':(lambda i,j:i+j), '-':(lambda i,j:i-j), '*':(lambda i,j:i*j), '/':(lambda i,j:i/j)}

# print(b['+'](20,5))
# for key in b.items():
#     print(key)
for key,value in range(len(b)):
    print(b(value),key,b(value))
