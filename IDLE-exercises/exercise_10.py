import random
while True:
  first_roll = random.randint(1,6)
  print(f"Your first roll and point value is: {first_roll}")
  count = 0
  while True:
    next_roll = random.randint(1,6)
    print(f"Your next roll is: {next_roll}")
    count += 1
    if next_roll == first_roll:
      print(f"It took {count} times to get your point again.")
      break
    else:
      continue
  answer = input("Do you want to play again (Y/N): ")
  if answer == "Y":
    continue
  else:
    break