class Error(Exception):
  pass
class ValueNegativeError(Error):
  pass
class ValueAbove100Error(Error):
  pass

while True:
  try:
    num = int(input("Enter a percentage: "))
    if num < 0:
      raise ValueNegativeError
    elif num > 100:
      raise ValueAbove100Error
    break
  except ValueNegativeError:
    print("This number is negative!")
    print()
  except ValueAbove100Error:
    print("This number is above 100!")
    print()
print(f"{num}%")