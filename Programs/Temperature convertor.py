#Exercise(Temperature convertor)
print("Convert Your Temperature from Celsius to Fahrenheit and Fahrenheit to Celsius")
temp = float(input("Enter the Temperature : "))
Unit = input("Is the Temperature in celsius or fahrenheit ( C/F ) : ") .lower()

if Unit == "c" :
    temp = (temp * 9/5) + 32
    print(f"The temperature in fahrenheit is : {temp} °F")
elif Unit == "f" :
    temp = ((temp - 32 ) * 5/9)
    print(f"The Temperature in celsius is : {temp} °C")
else :
    print("Invalid Temperature Unit !")
