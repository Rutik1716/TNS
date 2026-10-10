import random 

secret = random.randint(1, 20)

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    Guess = int(input("Guess The Number:"))
    attempts += 1

    if secret == Guess:
        print("You guessed it right!")
        break
    elif secret > Guess:
        print("Too low!")
    else:
        print("Too high!")
        
