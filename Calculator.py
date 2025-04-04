import os
from colorama import init, Fore, Back, Style
import math

init(autoreset=True)

def print_border(width=50):
    print(Fore.CYAN + "=" * width)

def print_header(text):
    print_border()
    print(Fore.BLUE + text.center(50))
    print_border()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number(prompt):
    while True:
        try:
            return float(input(Fore.YELLOW + prompt))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number.")

def main():
    history = []
    while True:
        clear_screen()
        print_header("CALCULATOR")
        print(Fore.CYAN + """
        Basic Operations:
        1. ➕ Add
        2. ➖ Subtract
        3. ✖️  Multiply
        4. ➗ Divide
        
        Scientific Operations:
        5. 🔢 Power
        6. √ Square Root
        7. 📐 Sin
        8. 📐 Cos
        
        Other Options:
        9. 📜 View History
        0. 🚪 Exit
        """)
        
        choice = input(Fore.YELLOW + "Enter choice (0-9): ")
        
        if choice == '0':
            print_header("Thank you for using the calculator!")
            break
            
        if choice == '9':
            print_header("Calculation History")
            if not history:
                print(Fore.YELLOW + "No calculations yet!")
            else:
                for i, calc in enumerate(history, 1):
                    print(Fore.WHITE + f"{i}. {calc}")
            input(Fore.CYAN + "\nPress Enter to continue...")
            continue
            
        try:
            if choice in '1234':
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                
                result = None
                if choice == '1':
                    result = add(num1, num2)
                    operation = '+'
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = '-'
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = '*'
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = '/'
                
                if isinstance(result, str):  # Error message
                    print(Fore.RED + result)
                else:
                    calc = f"{num1} {operation} {num2} = {result}"
                    history.append(calc)
                    print(Fore.GREEN + f"\nResult: {calc}")
                    
            elif choice in '5678':
                num = get_number("Enter number: ")
                result = None
                if choice == '5':
                    power = get_number("Enter power: ")
                    result = math.pow(num, power)
                    calc = f"{num} ^ {power} = {result}"
                elif choice == '6':
                    result = math.sqrt(num)
                    calc = f"√{num} = {result}"
                elif choice == '7':
                    result = math.sin(math.radians(num))
                    calc = f"sin({num}°) = {result:.4f}"
                elif choice == '8':
                    result = math.cos(math.radians(num))
                    calc = f"cos({num}°) = {result:.4f}"
                
                history.append(calc)
                print(Fore.GREEN + f"\nResult: {calc}")
            else:
                print(Fore.RED + "Invalid choice!")
                
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")
            
        input(Fore.CYAN + "\nPress Enter to continue...")

if __name__ == "__main__":
    main()
