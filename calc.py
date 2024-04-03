print ("          sign up   for calculator           ")
Name = input("Enter your name: ")
age = input("enter your age : ")
email = input("enter your email : ")
print("hello " +  Name + "!")
print("thank you for signing up ")
#calculator

num1 = float(input("enter a number: "))
op = input("enter operator: ")
num2 = float(input("enter secound number: "))
if op == "+" :
    print(num1 + num2)
elif op == "-" :
    print(num1 - num2)
elif op == "/" :
    print (num1 / num2)
elif op == "*" :
    print(num1 * num2)
else :
    print("invalid operator")

