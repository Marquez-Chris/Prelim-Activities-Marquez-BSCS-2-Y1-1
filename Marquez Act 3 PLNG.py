print("==========IS IT A MULTIPLE OF 5==========")
while True:
    num = float(input("Enter numbers that is a multiple of 5: "))

    if 1 <= num <= 100:
        if num % 5 == 0:
             print("This number is a multiple of 5")
        else:
            print("This number is not a multiple of 5 ")
            break
    else:
        print("Invalid number")
        break