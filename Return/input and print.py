a=10
b=7
c=53
def getinput():
  a=input()
  return a

def testinput(a):
  try:
    a=int(a)
    print("True")
  except ValueError:
    print("False")
    
def strtoint(b):
  try:
    b=int(b)
  except:
    print("Error")
    return
  return b
    #print(strtoint(b))

def printint(c):
  print(c)
  #print(printint())

print(getinput())
print(testinput(a))
print(strtoint(b))
print(printint(c))
