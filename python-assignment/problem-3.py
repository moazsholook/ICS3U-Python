my_list = []
while True:
  num = int(input("Enter a number: "))  
  if num == 0:
    break
  else:
    my_list.append(num)
  

my_list.sort()
mean = sum(my_list)/2
print(f"mean: {mean}")

