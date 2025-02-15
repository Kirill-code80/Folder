def returning():
  try:
    r=str(input())
    u=str(input())
  except ValueError:
    print("Error")
  return(r+u)

print(returning())
