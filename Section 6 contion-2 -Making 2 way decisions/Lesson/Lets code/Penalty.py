import random
# print("1=left")
# print("2=center")
# print("3=right")
# gk=random.randint(1,3)
# print(gk)
# user=int(input('Shot :'))
# if user > 3:
#     print("wrong!")
#     pass
# else:
#     if gk == user :
#         print("No Goal")
#     else :
#         print("Goal!")


# answer
n =random.randint(1,3)
if n == 1:
    computer_choice ='left'
elif n ==2 :
    computer_choice = 'center'
else :
    computer_choice = 'right'

user_choice = input("Where do you want to shoot?(left, center, right) :")
if computer_choice == user_choice :
    print("No Goal")
else :
    print("Goal !")
print("Defence position of computer :",computer_choice)