num1 = input("Enter a number: ")
num2 = input("Enter another number: ")  # By default python converts input to strings
result = num1 + num2
print(result)
# Therefore we need to use a function to convert the string to an interger
# The int function only takes whole numbers
# result = int(num1) + int(num2)
result = float(num1) + float(num2)  # Takes in both decimals and whole numbers
print(result)

