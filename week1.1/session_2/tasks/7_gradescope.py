#Ask the user to enter two numbers
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("That is not a number")
    exit()

#Multiply those numbers together
result = num1 * num2

#Print out the result
print(result)
