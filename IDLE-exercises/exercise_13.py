elements_in_list = int(input("How many elements should be in the list?: "))
mylist = []
for i in range(elements_in_list):
  number = int(input("Enter element: "))
  mylist.append(number)

print(mylist)