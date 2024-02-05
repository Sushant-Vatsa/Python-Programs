#Exercise(calculator)
operator = input("Enter an operator (+ - / *) : ")
num1 = float(input("Enter a number : "))
num2 = float(input("Enter a second number : "))

if operator == "+" :
    print('Answer =',num1 + num2)
elif operator == "-" :
    print('Answer =',num1 - num2)
elif operator == "*" :
    print('Answer =',num1 * num2)
elif operator == "/" :
    print('Answer =',num1 / num2)
else :
    print("Invalid operator")