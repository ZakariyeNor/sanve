print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()
if playing != 'yes':
    quit()
else:
    print("Let's play")
rights = 0
wrong = 0

answer = input("What does CPU stand for? ").lower()

if answer == "Central processing Unit":
    print("Correct!")
    rights += 1
else:
    print("Incorrect!")
    wrong += 1


answer = input("What does GUI stand for? ").lower()

if answer == "Graphic User Interface":
    print("Correct!")
    rights += 1
else:
    print("Incorrect!")
    wrong += 1

answer = input("What does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct!")
    rights += 1
else:
    print("Incorrect!")
    wrong += 1

answer = input("What does RAM stand for? ").lower()

if answer == "Random access memory":
    print("Correct!")
    rights += 1
else:
    print("Incorrect!")
    wrong += 1

print(f"You got right {rights} and wrong {wrong}")
print("You got " + str((rights / 4) * 100) + "%.")