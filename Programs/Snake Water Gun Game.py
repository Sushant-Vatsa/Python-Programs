#Snake Water Gun Game
import random

values = ["Snake","Water","Gun"]

while True:
    User_Input = input("Enter the Value (Snake, Water, Gun) or 'Quit' to stop: ")
    
    if User_Input == "Quit":
        break
    
    if User_Input not in values:
        print("Invalid Input, please enter Snake, Water, or Gun.")
        continue
    Computer_Choice = random.choice(values)


    if Computer_Choice == User_Input:
        print("It's a Tie")
    elif Computer_Choice == "Snake" and User_Input == "Water":
        print(f"You Lose ! I chose {Computer_Choice}")
    elif Computer_Choice == "Water" and User_Input == "Snake":
        print(f"You Win ! I chose {Computer_Choice}")
    elif Computer_Choice == "Water" and User_Input == "Gun":
        print(f"You Lose ! I chose {Computer_Choice}")
    elif Computer_Choice == "Gun" and User_Input == "Water":
        print(f"You Win ! I chose {Computer_Choice}")
    elif Computer_Choice == "Gun" and User_Input == "Snake":
        print(f"You Lose ! I chose {Computer_Choice}")
    elif Computer_Choice == "Snake" and User_Input == "Gun":
        print(f"You Win ! I chose {Computer_Choice}")
