def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Simple Calculator")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    
    print("Choose the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        operation = input("Enter choice (1/2/3/4): ")
        
        if operation == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
            break
        elif operation == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
            break
        elif operation == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
            break
        elif operation == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
            break
        else:
            print("Invalid choice! Please select a valid operation (1/2/3/4).")

if __name__ == "__main__":
    main()
