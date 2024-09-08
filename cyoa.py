name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road,  it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator")

    elif answer == "walk":
        print("You walk in the wild animal jungle and disappear therefore you lost the game")

    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back) ")

    if answer == "back":
        print("You go back and lose.")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no) ").lower()

        if answer == "yes":
            print("You talked to the stragres and they told you the right path out of the adventure")

        elif answer == "no":
            print("You ignored the adventure guidence and you lose the game.")

        else:
            print("Not a valid option. You lose.")

    

else: 
    print("Not a valid option. You lose.")


print(f"Thank you trying to play the unknown adventure {name}")