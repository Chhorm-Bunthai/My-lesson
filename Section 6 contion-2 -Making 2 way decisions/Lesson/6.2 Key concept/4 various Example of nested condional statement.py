# 4.1 using nesting to determine even or odd
num =int(input("Please enter a number :"))
if num < 0 :
    print("this is negative")
else:
    print("It is not negative")
    if num % 2 == 0 :
        print("This is an even number")
    else :
        print("This is an odd number.")
    3