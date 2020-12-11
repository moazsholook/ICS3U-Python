my_list = []
while True:
  num = int(input("Enter a number: "))  
  if num == 0:
    break
  else:
    my_list.append(num)
  

my_list.sort()
print(my_list)
mean = sum(my_list)/2
print(f"mean: {mean}")
if len(my_list)%2 == 1:
  median = my_list[round(len(my_list),0)]
  print(f"median: {median}")
else:
  a = (len(my_list)//2)-1
  b = -(len(my_list)//2)
  median = (my_list[a] + my_list[b])/2
  print(f"median: {median}")
