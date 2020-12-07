number = int(input("Enter a number: "))
sum_of_digits = 0
num = str(number)
for i in num:
  sum_of_digits += int(i)
print(f"{number} has {len(num)} digits and their sum is {sum_of_digits}")