#Gta V Character Info 

class Player:
    name = "Default Character"
    age = 0
    skill = "None"
    fav_gun = "None"
    bank_balance = " "
    def info(self):
        print(f"{self.name}'s Age is {self.age}, His skill is {self.skill} and His favourite gun is {self.fav_gun}. \nHis Bank Balance is {self.bank_balance}")

#Michael
player1 = Player()
player1.name = "Michael"
player1.age = 38  
player1.skill = "Marksman"
player1.fav_gun = "MG 50"
player1.bank_balance = "$60,000,000"
# player1.info()

#Franklin
player2 = Player()
player2.name = "Franklin"
player2.age = 25
player2.skill = "Driving"
player2.fav_gun = "Assault Rifle"
player2.bank_balance = "$40,000,000"
# player2.info()

#Trevor
player3 = Player()
player3.name = "Trevor"
player3.age = 39
player3.skill = "Rampage"
player3.fav_gun = "Shotgun"
player3.bank_balance = "$70,000,000"
# player3.info()

Input_Character = input("Enter the character you want to know about : ") 
Input_Character.lower()

if Input_Character == "michael": 
    player1.info()
elif Input_Character == "franklin":
    player2.info()
elif Input_Character == "trevor":
    player3.info()
else:
    print("Invalid Character! Please try again ")