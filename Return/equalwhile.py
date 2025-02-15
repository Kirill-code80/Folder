def equality():
  a=int(input())
  eq=a
  while True:
    a=int(input())
    if a == 0:
      return(eq)
    eq=eq*a
print(equality())
