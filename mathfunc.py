figure=input("1-прямоугольник, 2-треугольник, 3-круг: ")
def rectangle():
  a=int(input("Длина: "))
  b=int(input("Ширина: "))
  c=a*b
  print(c)
def triangle():
  a=int(input("Длина: "))
  h=int(input("Высота: "))
  t=a*h*0.5
  print(t)
def circle():
  r=int(input("Радиус: "))
  g=3.14*r**2
  print(g)
if figure == '1':
  rectangle()
elif figure == '2':
  triangle()
elif figure == '3':
  circle()
else:
  print("Input error")
