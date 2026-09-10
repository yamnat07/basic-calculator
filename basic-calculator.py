print("=====================================")
print("~~~~~~WELCOME TO THE CALCULATOR~~~~~~")
print("=====================================")
num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))
print("For addition: +")
print("For subtraction: -")
print("For multiplication: *")
print("For division: /")
print("For remainder: %")
print("For power: **")
print("All these operations will be calculate as num1+num2, num1-num2,\n num1*num2, num1/num2, num1%num2, num1**num2:-  Be careful while entering numbers.")

op=input("Enter the operator: ")
if op=="+":
    print(f"The sum is: {num1+num2}")
elif op=="-":
    print(f"The difference is: {num1-num2}")
elif op=="*":
    print(f"The product is: {num1*num2}")
elif op=="/":
    print(f"The answer is: {num1/num2}")
elif op=="%":
    print(f"The remainder is: {num1%num2}")
elif op=="**":
    print(f"The answer is: {num1**num2}")
else:
    print("This operation is not defined in this calculator!")                    
