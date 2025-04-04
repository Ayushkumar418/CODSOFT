import random
import string
import pyperclip
from colorama import init, Fore, Back, Style

init(autoreset=True)

def print_border(width=50):
    print(Fore.CYAN + "=" * width)

def get_password_strength(password):
    strength = 0
    if any(c.islower() for c in password): strength += 1
    if any(c.isupper() for c in password): strength += 1
    if any(c.isdigit() for c in password): strength += 1
    if any(c in string.punctuation for c in password): strength += 1
    return ["Weak", "Fair", "Good", "Strong"][strength-1]

def generate_password(length, complexity="all"):
    char_sets = {
        "lower": string.ascii_lowercase,
        "upper": string.ascii_uppercase,
        "digits": string.digits,
        "special": string.punctuation,
        "all": string.ascii_letters + string.digits + string.punctuation
    }
    chars = char_sets.get(complexity, char_sets["all"])
    return "".join(random.choice(chars) for _ in range(length))

def main():
    print_border()
    print(Fore.BLUE + "PASSWORD GENERATOR".center(50))
    print_border()
    
    try:
        length = int(input(Fore.YELLOW + "Enter the length of password: "))
        if length < 4:
            print(Fore.RED + "Password length must be at least 4 characters!")
            return
            
        num_passwords = int(input(Fore.YELLOW + "How many passwords to generate? (1-5): "))
        num_passwords = min(max(1, num_passwords), 5)
        
        print(Fore.CYAN + "\nSelect complexity:")
        print("1. All characters (recommended)")
        print("2. Letters and numbers only")
        print("3. Letters only")
        print("4. Numbers only")
        
        choice = input(Fore.YELLOW + "Enter choice (1-4): ")
        complexity_map = {
            "1": "all",
            "2": "alphanumeric",
            "3": "letters",
            "4": "digits"
        }
        complexity = complexity_map.get(choice, "all")
        
        print_border()
        print(Fore.GREEN + "Generated Passwords:")
        
        for i in range(num_passwords):
            password = generate_password(length, complexity)
            strength = get_password_strength(password)
            strength_color = {
                "Weak": Fore.RED,
                "Fair": Fore.YELLOW,
                "Good": Fore.BLUE,
                "Strong": Fore.GREEN
            }[strength]
            
            print(f"\nPassword {i+1}: {Fore.WHITE}{password}")
            print(f"Strength: {strength_color}{strength}")
            
        # Copy last generated password to clipboard
        pyperclip.copy(password)
        print(Fore.CYAN + "\nLast password copied to clipboard!")
        
    except ValueError:
        print(Fore.RED + "Please enter valid numbers!")
    
    print_border()

if __name__ == "__main__":
    main()
