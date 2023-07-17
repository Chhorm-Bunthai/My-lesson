print("Welcome to Yummy restuarant. Here is the menu.")
print("- Burger(enter b)")
print("- Chicken(enter c)")
print("- Pizza(enter p)")
choose = input("Choose a menu (enter b,c,p) :")
if choose != 'c' or choose != 'b' or choose != 'p' :
    print("Please enter the menu again")
else:
    if choose == 'b':
        print("you chose Burger.")
    elif choose == 'c' :
        print("you chose Chicken")
    else :
        print("you chose Pizza")