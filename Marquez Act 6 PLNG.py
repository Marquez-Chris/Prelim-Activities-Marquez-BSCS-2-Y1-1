

while True:
    print("========GRADES CALCULATION=======")
    javag = float(input("Enter your JAVA programming score: "))
    cg = float(input("Enter your C programming score: "))
    dhs = float(input("Enter your Database Handling Score: "))

    ave = (javag + cg + dhs) / 3

    if ave >= 90:
        print("Average:", round(ave,2), "||", "Grade is A because the average is between 90 and 100")
    elif ave >= 80:
        print("Average:", round(ave,2), "||", "Grade is B because the average is between 80 and 89")
    elif ave >= 75:
        print("Average:", round(ave,2), "||", "Grade is C because the average is between 75 and 79")
    else:
        print("Average:", round(ave,2), "||", "Grade is F because the average is below 75")

    choice = input("Do you want to continue (YES/NO): ")

    if choice.upper() != "YES":
        print("Program Terminated")
        break