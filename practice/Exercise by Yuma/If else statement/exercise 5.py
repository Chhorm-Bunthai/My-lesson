class_held = int(input("number of classes held :"))
class_attended = int(input("number of classes attended :"))

attend= (100 * class_attended) / class_held
if attend < 75 :
    print("not allowed")
else :
    print("Allowed to sit")
print("Percentage of class attended is ",attend,"%")