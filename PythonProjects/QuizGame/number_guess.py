import random

max_num = input("type a number: ")
guesses = 0 

if max_num.isdigit():
    max_num = int(max_num)
    if max_num <= 0:
        print("please print a number higher than 0.")
        quit()
else:
    print("please type a number next time")
    quit()

random_number = random.randint(0, max_num)

while True: 
    guesses += 1
    guess = input("guess the number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please type a number next time")
        continue

    if random_number == guess:
        print("You got the number")
        break 
    elif guess < random_number:
        print("You are less than the number")
    else:
        print("You were below the number")

print("you got it in", guesses, "guesses")
