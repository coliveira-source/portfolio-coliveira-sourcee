import random
random_number = random.randint(1, 1000)

print("I'm thinking of a number from 1 to " + str(1000) + ". What's the number?")
count = 1
while True:
    guess = int(input("Your guess: "))
    if guess < random_number:
        print("Too low.")
    elif guess > random_number:
        print("Too high.")
    elif guess == random_number:
        print("The correct answer is", random_number , ". You guessed it in " + str(count) + " tries.")
    count+=1