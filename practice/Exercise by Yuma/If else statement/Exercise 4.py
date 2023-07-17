a=int(input("enter a :"))
b=int(input("enter b :"))
c=int(input("enter c :"))
d=int(input("enter d :"))
x=int(input("enter x :"))
k=int(input("enter k :"))

if x > k :
    y= a*(x**3) - b*(x**2) + c*x - d
    print("F(x) = ",y)
elif x == k :
    y =0
    print("F(x) = ",y)
else :
    y = -a*(x**3) + b*(x**2) - c*x + d
    print("F(x) = ",y)
