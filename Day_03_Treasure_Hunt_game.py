print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
way = input("where do you wanna go left or right? ")
if way == "left" or way == "Left":
    print("You found a river")
    stop_1 = input("do you wanna swim through it or wait for a boat ")
    if stop_1 == "wait" or stop_1 == "Wait":
        print("You got three doors Red , Yellow and Blue")
        stop_2 = input("which door you wanna choose red, yellow or blue ")
        if stop_2 == "yellow":
            print("Congratulations! You won the treasure!")
        elif stop_2 == "red" or stop_2 == "blue" or stop_2 == "Red" or stop_2 == "Blue":
            print("Sorry you chose the wrong door, you lost the treasure!")
    else:
        print("Sorry you got eaten by the crocodile, you lost the treasure!")
elif way == "right" or way == "Right":
    print("Sorry, you lost the treasure!")
else:
    print("You entered the wrong input")