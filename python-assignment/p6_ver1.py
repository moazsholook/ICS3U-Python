def linear():
  print(f"for an equation in the form: ax + by + c = 0\n")
  y_int = -c / b
  slope = -a / b 
  print(f"{'x':>11}{'y':>21}")
  for x in range (-5,6,1):
    print(f"{round(x,1):>12}{round(slope*x + b,1):>22}")

def quadratic():
  print(f"for an equation in the form: y = ax^2 + bx + c\n")
  x_vertex = -b/2*a 
  x = x_vertex - 6 
  print(f"{'x':>11}{'y':>21}")
  for i in range(11):
    x += 1
    y = a*x**2 + b*x + c
    print(f"{round(x,1):>12}{round(y,1):>22}")

while True:
  answer = input("""What relation would you like to see?
  1. Linear
  2. Quadratic\n""")
  a = float(input("What is the a value?: "))
  b = float(input("What is the b value?: "))
  c = float(input("What is the c value?: "))
  if answer == "1":
    linear()
  elif answer == "2":
    quadratic()
  input("Would you like to try another one? Y/N: ")
  if answer == "Y":
    continue
  else:
    print("Thank you, goodbye")
    break
  

