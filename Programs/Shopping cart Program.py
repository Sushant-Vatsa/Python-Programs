#Shopping cart Program
import time

foods = []
prices = []
Total = 0

print("Welcome to Our Shopping Mall, Here You can Buy all Grocery Products From us !")
for x in range(3,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    time.sleep(1)

while True :
    food = input("Enter the Product You want to Purchase or Press q to quit : ")
    if food.lower() == "q":
       break
    else :
        price = float(input("Enter The Price of The Product You want to Purchase : $"))
        foods.append(food)
        prices.append(price)

print("_____YOUR CART ______")

for food, price in zip(foods, prices):
    print(f"{food}: ${price}")

Total = sum(prices)
print()
print(f"Your Total is: ${Total}")
