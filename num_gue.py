import random 

top_of_range = input("Type a number: ")
#Make sure that the user types in  a number
#The nmumber must be greater than 0 and less than 11 

if not top_of_range.isdigit():
    print("Please choose a number")
else:
    top_of_range = int(top_of_range)
    print("Please choose a number")
    if 0 < top_of_range < 11:
        print(f"Your number is {top_of_range}")
    else:
        print("Please choose number between 1 - 10")

random_number = random.randint(0, top_of_range)
print(random_number)


guesses = 0 
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if 0 < user_guess < 11: 
            print("Choose in the limit")
print(f"You guessed {guesses} guesses")
