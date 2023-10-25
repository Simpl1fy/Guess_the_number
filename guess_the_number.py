import random
secret = random.randint(1,10);

x = True
score = 10

# Statement
print("Guess a number between 1 and 10, you have 10 tries, the higher the score the better.")

while x:
    user_input = int(input("Enter a number = "))    # User Input
    if ((user_input) < 1 or (user_input) > 10):     # If the guess is out of bounds
        print("Guess out of bounds")
    elif user_input == secret:                      # If the user has correctly guessed the random number
        print("Correct Guess!")
        x = False
    elif user_input > secret:                       # If the number guessed is higher than the random number
        print("Guess is high!")
        score -= 1
    else:                                           # If the number guessed is lower than the random number
        print("Guess is low")
        score -= 1
    if score < 1:                                   # If user runs out of tries
        print("You ran out of tries😢")
        x = False

if score > 0:                                       # Printing the score if score is greater than 0
    print("Your score is = ", score)