#this function retrieves the sum of all the numbers in the list
#and divides them by the total number of elements
def find_mean():
  mean = round(sum(my_list)/len(my_list),1)
  print(f"mean: {mean}")
#this function determines whether the function has an odd or even 
#number of values and then finds the exact middle of the list using division 
def find_median():
  if len(my_list)%2 == 1:
    median_position = int(round(len(my_list)/2,0))
    median = my_list[median_position]
    print(f"median: {median}")
  else:
    small_middle_value = (len(my_list)//2)-1
    large_middle_value = -(len(my_list)//2)
    sum_of_middle_values = my_list[small_middle_value] + my_list[large_middle_value]
    median = sum_of_middle_values/2
    print(f"median: {median}")
#this function retrieves the first and last values in the list and calculates the difference between them
def find_range():
  max_value = my_list[-1]
  min_value = my_list[0]
  range_of_list = max_value - min_value
  print(f"range: {range_of_list}") 
#the function counts the occurence of each element in the list and 
#sets the most repeated to be the mode. 
def determine_mode():
  mode = ""
  for num in my_list:
    if my_list.count(num) > my_list.count(mode):
      mode = num
  if mode != "":
    print(f"There IS a mode. The mode is {mode}")
  else:
    print("There is no mode")

#creating an error to disregard any inputs that have a negative value
class Error(Exception):
  pass
class ValueNegativeError(Error):
  pass
#the try and except statements allow the program to ignore any inputs 
#are not appropriate for the program, even if they do not match the input type.
my_list = []
while True:
  try:   
    num = int(input("Enter an integer. Enter 0 to end list: "))
    if num < 0:
      raise ValueNegativeError
    elif num == 0:
      break
    my_list.append(num)
  except ValueNegativeError:
      print("Error! Your input must be POSITIVE.\n")
      continue
  except ValueError:
      print("Error! Your input must be an INTEGER.\n")
      continue
my_list.sort()
print(my_list)
find_mean()
find_median()
find_range()
determine_mode()