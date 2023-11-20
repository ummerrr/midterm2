
def Add(x, y):
    return x + y

def Sub(x, y):
    return x - y

def Mul(x, y):
    return x * y

def Div(x, y):
    if y == 0:
        return "Cannot Div by zero"
    return x / y
def SqRoot(x):
    return (x ** 0.5)


while True:
    print("Options:")
    print("Enter 'Add' for Addition")
    print("Enter 'Sub' for Subion")
    print("Enter 'Mul' for multiplication")
    print("Enter 'Div' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("Add", "Sub", "Mul", "Div"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "Add":
            print("Result:", Add(num1, num2))
        elif user_input == "Sub":
            print("Result:", Sub(num1, num2))
        elif user_input == "Mul":
            print("Result:", Mul(num1, num2))
        elif user_input == "Div":
            print("Result:", Div(num1, num2))
        elif user_input == "sqrt":
            print("Resutl of num1:", SqRoot(num1))
            print("Resutl of num2:", SqRoot(num2))
    else:
        print("Invalid input")
