# print("Hello World!")
import random
secret = random.randint(1,10);

user_input = int(input("Enter a number = "))

if user_input == secret:
    print("Correct Guess!")
elif user_input > secret:
    print("Guess is high!")
elif user_input < 0 and user_input > 10:
    print("Guess out of bounds")
else:
    print("Guess is low")