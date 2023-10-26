import random       # Importing random library for generating random numbers
secret = random.randint(1,10);  # Generating a integer random number between 1 and 10

score = 10
user_input = 0

# Statement
print("Guess a number between 1 and 10, you have 10 tries, the higher the score the better.")

while user_input != secret:
    user_input = int(input("Enter a number between 1 and 10: "))
    if(user_input > secret):
        print("Guess is too high")
        score -= 1
    elif(user_input < secret):
        print("Guess is too low")
        score -= 1
    if(score < 1):
        print("Ran out of score")
        break

if(score != 0):
    print(f"You guessed the number {secret} with a score of {score}")