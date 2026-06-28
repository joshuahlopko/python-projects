from goodies import Colour
#Give description of location
label .cave
clear()
print("You are in the cave.")
print(Colour.green + "Bats can be heard crying in the darkness." + Colour.reset)
print("It is dark.")
print()
#Show the choices
print("You can do the following.")
print("go right")
print("go left")
print()
#Ask the user their choice

choice = input("What would you like to do?")
#Use IF statements to act on choices
if choice == "go right":
    print("You start heading right.")
    goto .clearing
if choice == "go left":
    print("You start heading left.")
    goto .forest
print("Invalid choice, please choose again.")
sleep(2)
goto .cave

label .forest
clear()
print("You are in the forest.")
print(Colour.green + "Animal sounds can be heard." + Colour.reset)
print("There are leaves crunching beneath your feet.")
print()
#Show the choices
print("You can do the following.")
print("go right")

print()
#Ask the user their choice
choice = input("What would you like to do?")
#Use IF statements to act on choices
if choice == "go right":
    print("You start heading right.")
    goto .cave
print("Invalid choice, please choose again.")
sleep(2)
goto .forest

label .clearing
clear()
print("You are in the clearing beyond the cave.")
print(Colour.green + "There is a pond." + Colour.reset)
print("A creek babbles in the distance.")
print()
#Show the choices
print("You can do the following.")
print("go left")
print("follow the creek")

print()
#Ask the user their choice
choice = input("What would you like to do?")
#Use IF statements to act on choices
if choice == "go left":
    print("You start heading left.")
    goto .cave
if choice == "follow the creek":
    print("You follow the creek.")
    goto .city
print("Invalid choice, please choose again.")
sleep(2)
goto .forest

label .city
clear()
print("You manage to get out of the forest.")
print("You have reached civilization!")
print("Game Over!")
