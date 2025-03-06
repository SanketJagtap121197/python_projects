
number1 = float(input("Enter first number : "))
number2 = float(input("Enter second number : "))
operation = input("Choose the following operators : +, -, *, / \n")

if operation == "+" :
    result = number1 + number2
    
elif operation == "-" :
    result = number1 - number2
    
elif operation == "*" :
    result = number1 * number2
    
elif operation == "/" :
    if number2 !=0 :
        result = number1 / number2
    else :
        result = "Error division by zero"

else :
    result = "Invalid operation"

print ("The result of the following is ", result)