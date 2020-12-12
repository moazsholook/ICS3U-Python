class Error(Exception):
  pass
class ValueNegativeError(Error):
  pass


my_list = []
while True:
  try:   
    num = int(input("Enter an integer. Enter 0 to end list: "))
    if num < 0:
      raise ValueNegativeError
    if num == 0:
      break
      my_list.append(num)
  except ValueNegativeError:
      print("Error! Your input must be POSITIVE.\n")
      continue
  except ValueError:
      print("Error! Your input must be an INTEGER.\n")
      continue
 
my_list.sort()
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
print(f"range: {range_of_list}") 
