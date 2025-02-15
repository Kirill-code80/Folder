def cylinder():
  r=int(input("Радиус: "))
  h=int(input("Высота: "))
  e=2*3.14*r*h
  c=0
  def circle():
    global c
    c=3.14*r*r
  w=input("Найти бок или всё: ")
  if w == 'бок':
    print(e)
  if w == 'всё' or 'все':
    circle()
    a=e+c
    print(a)

cylinder()
