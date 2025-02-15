# # s1 = 'abcd'
# # s2 = '01'
# # t=[i+j for i in s1 for j in s2]
# # print(t)
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# u=[i for i in a if i%2==0]
# print(u)
a = [1, 2, 3]
b = [4, 5, 6]
v=[(i,j) for i in a for j in b if i*j <= 10]
print(v)