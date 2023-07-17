print("1) addition, 2) subtraction, 3) multiplication 4) division")
choose = int(input("Please enter the number corresponding to the operation :"))


if choose > 4:
    print("Invalid input")
else:
    num1 = int(input("Please enter two numbers for the operation :"))
    num2 = int(input("Please enter two numbers for the operation :"))
    if choose == 1:
        add = num1 + num2
        print(num1, "+", num2, "=", add)
    elif choose == 2:
        sub = num1 - num2
        print(num1, "-", num2, "=", sub)
    elif choose == 3:
        mul = num1 * num2
        print(num1, "*", num2, "=", mul)
    else:
        div = num1 / num2
        print(num1, "/", num2, "=", div)
