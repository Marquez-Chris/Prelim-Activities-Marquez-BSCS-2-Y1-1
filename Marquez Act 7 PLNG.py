while True:

    print("========Arithmetic Calculator=======")
    print("1. Addition     2. Subtraction   3. Multiplication")
    print("4. Division     5. Modulus       6. Increment")
    print("7. Decrement")
    chos = float(input("Select an arithmetic option: "))
    if chos == 1 or chos == 2 or chos == 3 or  chos == 4 or chos == 5:
        x = float(input("Enter the value of x: "))
        y = float(input("Enter the value of y: "))
    elif chos == 6:
        x = float(input("Enter the value of x: "))
    elif chos == 7:
        x = float(input("Enter the value of x: "))

    if chos == 1:
        ans = x+y
        print("Operation is (Addition) ||","Value of x:",x, "||| Value of y:", y, "||Answer:",ans,)
    elif chos == 2:
        ans = x-y
        print("Operation is (Subtraction) ||","Value of x:",x, "||| Value of y:", y, "||Answer:",ans)
    elif chos == 3:
        ans = x*y
        print("Operation is (Multiplication) ||","Value of x:",x, "||| Value of y:", y, "||Answer:",ans)
    elif chos == 4:
        ans = x/y
        print("Operation is (Division) ||","Value of x:",x, "||| Value of y:", y, "||Answer:",ans)
    elif chos == 5:
        ans = x%y
        print("Operation is (Modulo) ||","Value of x:",x, "||| Value of y:", y, "||Answer:",ans)
    elif chos == 6:
        ans = 1+x
        print("Operation is (Incriment) ||","Value of x:",x, "||Answer:",ans)
    elif chos == 7:
        ans = x-1
        print("Operation is (Decriment) ||","Value of x:",x, "||Answer:",ans)
   
    choice = input("Do you want to continue(YES/NO): ")
    if choice.upper() != "YES":
        print("Program Terminated")
        break
   