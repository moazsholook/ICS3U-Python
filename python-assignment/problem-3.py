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
  small_middle_value = (len(my_list)//2)-1
  large_middle_value = -(len(my_list)//2)
  median = (my_list[small_middle_value] + my_list[large_middle_value])/2
  print(f"median: {median}")
max_value = my_list[-1]
min_value = my_list[0]
range_of_list = max_value - min_value
print(f"range: {range_of_list}) 
