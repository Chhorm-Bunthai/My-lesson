# hour=10
# if hour < 12:
#     print("It's morning")
# else:
#     print("It's afternoon")
import random
# 2 various example of if-else statement
# score=int(input("Please enter your score :"))
# if score > 90 :
#     print("you passed")
#     print("Get a scholarship, too")
# else :
#     print("You failed")

# 2.1 odd and even number determination
# num =10
# if num % 2 == 0 :
#     print(num, "is an even number.")
# else :
#     print(num,"is an odd number.")


# 2.3 numeric type determination
# x=input("Enter the first integer :")
# print("Input data type :", type(x))
# if x.isdigit() == True :
#     x=int(x)
#     print("Input data type :",type(x))
# else :
#     print("x is not a numeric character")



# 2.4 program to check if the ID matches
# id=int(input("enter your ID :"))
# love= 7
# if id == love :
#     print("I Love Python")
# else :
#     print("I hate Python")
# ---------------------------
# id='ilovepython'
# s=input('enter your id :')
# if s == id :
#     print("Welcome")
# else :
#     print("No id found")


# 2.5 creating a coin flipping game with the random function

import  random as rd
print("Lets start the coin toss game.")
coin=random.randrange(2)
if coin==0 :
    print("front")
else :
    print("Back")
print("Game Over")