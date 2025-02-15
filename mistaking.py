try:
  n=input("Number: ")
  n=int(n)
except ValueError:
  print("Something's wrong")
else:
  print("It's alright. You input: ",n)
finally:
  print("The end")
