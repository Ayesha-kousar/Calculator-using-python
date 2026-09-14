# Assingment no 1: using clculator
num1=20
num2=10
num1=float(input("Enter first number:"))
operator=input("enter any sign(+,-,*,/)")
num2=float(input("enter second number"))
if operator=="+":
    print("Result",num1+num2)
elif operator=="-":
    print("Result",num1-num2)
elif operator=="*":
    print("Result",num1*num2) 
elif operator=="/":
    if num2!=0:
        print("Results",num1/num2)
    else:
        print("number is no divisible") 
else:           
    print("invalid chracter")