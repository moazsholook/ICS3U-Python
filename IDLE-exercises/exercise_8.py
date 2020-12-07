starting_value = int(input("Enter a starting value: "))
ending_value = int(input("Enter an ending value: "))
increment = int(input("Enter an increment: "))
print(f"{'List value':>13} {'Square':>20}")
for i in range(starting_value, ending_value, increment):
  print(f"{i:>10}{i**2:>20}")