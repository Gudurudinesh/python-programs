import random
secret_number = random.randint(1,100)
attempts = 0
while True:
  guess = int(input("enter a number" ))
  attempts +=1
  if guess < secret_number:
    print("Too low")
  elif guess > secret_number:
    print("Too high")
  else:
    print("Congratulations,correct guess")
    print("no.of attempts:",attempts)
    break