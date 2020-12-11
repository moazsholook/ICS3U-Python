 def linear():
  print(f"for an equation in the form: ax + by + c = 0\n")
  y_int = -c / b
  slope = -a / b 
  print(f"{'x':>11}{'y':>21}")
  for x in range (-5,6,1):
    print(f"{round(x,1):>12}{round(slope*x + b,1):>22}")
  
 answer = input("""What relation would you like to see?
  1. Linear
  2. Quadratic\n""")
  a = float(input("What is the a value?: "))
  b = float(input("What is the b value?: "))
  c = float(input("What is the c value?: "))
  if answer == "1":
    linear()