# Q1
# text=input("please enter text :")
# if text == 'a' or text == 'e' or text == 'i' or text == 'o' or text == 'u' :
#     print("It is  vowel")
# else :
#     print(text," is a consonant")

# Q2

num1,num2=input("Please enter 2 integer :").split(" ")
num1= int(num1)
num2= int(num2)
if num1 % num2 == 0 :
    print(num1,"is a multiple of",num2)
else :
    print(num1,"is not multiple of ",num2)