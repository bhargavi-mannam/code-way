def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def calculator():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    print("Welcome to Simple Calculator!")
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter operation number (1/2/3/4): ")
    if choice not in operations:
        print("Invalid operation choice!")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = operations[choice](num1, num2)
    print("Result:", result)

if __name__ == "__main__":
    calculator()
