num1=int(input("num 1:"))
operator=input("operator:")  
num2=int(input("num 2:"))
if operator=="+":
    print(f"sum of two numbers:{num1+num2}")
elif operator=="-":
    print(f"subtraction of two numbers:{num1-num2}")
elif operator=="*":
    print(f"multiplication of two numbers: {num1*num2}")
elif operator=="/":
    if num2 != 0:
        print(f"division of two numbers: {num1/num2}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator=="%":
    if num2 != 0:
        print(f"modulus of two numbers: {num1 % num2}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator=="**":
    print(f"exponentiation of two numbers: {num1 ** num2}")
elif operator=="//":
    if num2 != 0:
        print(f"floor division of two numbers: {num1 // num2}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator=="sqrt":
    if num1 >= 0:
        print(f"Square root of {num1} is: {num1 ** 0.5}")
    else:
        print("Error: Cannot calculate square root of a negative number.")
elif operator=="abs":
    print(f"Absolute value of {num1} is: {abs(num1)}")
elif operator=="log":
    import math
    if num1 > 0:
        print(f"Logarithm of {num1} is: {math.log(num1)}")
    else:
        print("Error: Logarithm of non-positive number is undefined.")
else :
    print("Invalid operator")
print("Thank you!!!")
# calculator with additional operations
# This code extends the basic calculator functionality to include more operations like modulus, exponentiation, floor division, square root, absolute value, and logarithm.
# It also includes error handling for division by zero and invalid inputs.
# The code prompts the user for two numbers and an operator, performs the specified operation, and prints the result.
# The code also handles special cases like square root and logarithm, ensuring that the inputs are valid for those operations.
