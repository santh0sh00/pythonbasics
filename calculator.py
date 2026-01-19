num1=int(input("num 1:"))
operator=input("operator:")
num2=int(input("num 2:"))
if operator=="+":
    print(f"addition of two numbers:{num1+num2}")
elif operator=="-":
    print(f"subtraction of two numbers:{num1-num2}")    
elif operator=="*":
    print(f"multiplication of two numbers:{num1*num2}")
elif operator=="/":
    print(f"division of two numbers:{num1/num2}")  
else:
    print("invalid operator")
print("thank you!!!")
#calculator ...


