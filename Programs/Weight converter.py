#Exercise(Weight converter)
weight = float(input("Enter Your Weight : "))
Unit = (input("Kilograms or Pounds ? (K or Lb)"))

if Unit == "K" :
    print(weight * 2.2046)
elif Unit == "Lb" :
    print(weight / 2.2046)
else:
    print("Invalid Unit")