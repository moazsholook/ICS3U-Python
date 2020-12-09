while True:
  percentage = int(input("Enter a percentage: "))
  if 100 >= percentage >= 0: 
    print("Thank you")
    break
  else:
    print("Invalid percentage")
    continue