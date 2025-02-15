def test():
  a=int(input())
  if a > 0:
      positive()
  if a < 0:
      negative()
def positive():
  print("Positive")
def negative():
  print("Negative")
  
test()
