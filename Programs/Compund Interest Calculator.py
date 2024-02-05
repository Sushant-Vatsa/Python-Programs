#Compund Interest Calculator

#This'll be done through while loop

principal = 0
rate = 0
number_of_times = 0
time = 0 #in Years

#Principle
while principal <= 0 :
    principal = int(input("Enter the Principal : "))
    if principal <= 0 :
        print("Principal is not specified")

#Rate
while rate <= 0 :
    rate  = float(input("Enter the Rate : "))
    if rate <= 0 :
        print("Rate is not specified")

#number_of_times
while number_of_times <= 0 :
    number_of_times  = int(input("Enter Number of times Interest to be calculated : "))
    if number_of_times <= 0 :
        print("Command is not specified")

#Time
while time <= 0 :
    time  = int(input("Enter the Time(In Years) : "))
    if time <= 0 :
        print("Command is not specified")

#Compund Interest

c_i_ = principal * pow((1 + rate/100),time) - principal
print(f"Compund interest after {time} years : ${c_i_}")