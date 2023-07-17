x,y=input("enter x,y").split(" ")
x,y=int(x),int(y)
if x < 0 and y < 0 :
    print("In the third quadrant")
elif x >0 and y<0 :
    print("in the fourth quadrant")
elif x > 0 and y > 0 :
    print("In the first quadrant")
else :
    print("in the second quadrant")