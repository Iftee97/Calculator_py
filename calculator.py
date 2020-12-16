logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Calculator:
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return round(n1 / n2, 2)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# function = operations["*"]
# function(2, 3)
def calculator():
    print(logo)

    num1 = float(input("\nWhat's the first number? "))
    print()

    for symbol in operations:
        print(symbol)

    should_contiue = True
    while should_contiue:
        operation_symbol = input("\nPick an operation: ")
        num2 = float(input("\nWhat's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"\n{num1} {operation_symbol} {num2} = {answer}\n")

        choice = input(f"type 'yes' to continue calculationg with {answer}\nor type 'new' to start a new calculation\nor type 'no' to exit: \n")
        if choice == "yes":
            num1 = answer
        elif choice == 'new':
            should_contiue = False
            calculator()
        elif choice == 'no':
            should_contiue = False
            print("goodbye!")

calculator()
