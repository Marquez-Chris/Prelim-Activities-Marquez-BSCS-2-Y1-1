print("==========SHOP NG NGG==========")

num = float(input("Enter the cost of the product you are going to purchase: "))
num2 = float(input("Enter the cost of the second product you are going to purchase: "))
print("==========PAYMENT==========")
tot = num + num2 
print("Total amount to be paid: ", tot)
num3 = float(input("How much are you going to pay?: "))
    

if tot > num3:
    lef = tot - num3
    print ("You still have a remaing balance of:", lef)
elif num3 > tot:
    lef = num3 - tot
    print ("Thank you your change is: ", lef)