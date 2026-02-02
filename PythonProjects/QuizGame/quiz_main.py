# Users are asked question and they get a score based on the correct answers
# We print the final scores

print("Welcome to the computer quiz!")

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay, let's play")

score = 0
answer = input("What does CPU stamnd for? ")
if answer.lower() == "central processing unit":
    print("That is correct!")
    score += 1 
else:
    print("That is incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("That is correct!")
    score += 1 
else:
    print("That is incorrect")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("That is correct!")
    score += 1 
else:
    print("That is incorrect")

answer = input("What does PSU stamnd for? ")
if answer.lower() == "cpower supply unit":
    print("That is correct!")
    score += 1 
else:
    print("That is incorrect")

print("that's the end of the quiz. You scored: " + str(score) + " points")
