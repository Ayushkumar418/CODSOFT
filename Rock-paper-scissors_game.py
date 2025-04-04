import random
from colorama import init, Fore, Back, Style

init(autoreset=True)

ASCII_ART = {
    "Rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    Rock
""",
    "Paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    Paper
""",
    "Scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    Scissors
"""
}

def print_border(width=50):
    print(Fore.CYAN + "=" * width)

def print_score(user_score, computer_score, rounds):
    print_border()
    print(Fore.YELLOW + f"Round: {rounds}".center(50))
    print(Fore.GREEN + f"Your Score: {user_score}".center(50))
    print(Fore.RED + f"Computer Score: {computer_score}".center(50))
    print_border()

def check(com, user):
    if com == user:
        return 0
    elif com == 1 and user == 3:
        return -1
    elif com == 2 and user == 1:
        return -1
    elif com == 3 and user == 2:
        return -1
    return 1

def main():
    print_border()
    print(Fore.BLUE + "ROCK PAPER SCISSORS GAME".center(50))
    print_border()
    
    user_score = computer_score = rounds = 0
    
    while True:
        print(Fore.CYAN + "\nChoose your move:")
        print(Fore.WHITE + "1. Rock 👊")
        print("2. Paper ✋")
        print("3. Scissors ✌")
        
        try:
            user = int(input(Fore.YELLOW + "\nEnter your choice (1-3): "))
            computer = random.randint(1, 3)
            dct = {1: "Rock", 2: "Paper", 3: "Scissors"}
            
            if 1 <= user <= 3:
                rounds += 1
                print("\n" + Fore.GREEN + "Your choice:" + Style.RESET_ALL)
                print(ASCII_ART[dct[user]])
                print("\n" + Fore.RED + "Computer's choice:" + Style.RESET_ALL)
                print(ASCII_ART[dct[computer]])
                
                score = check(computer, user)
                if score == 0:
                    print(Fore.YELLOW + "🤝 Game Draw!")
                elif score == -1:
                    print(Fore.RED + "❌ Sorry, You lose!")
                    computer_score += 1
                elif score == 1:
                    print(Fore.GREEN + "🎉 Congratulations, you win!")
                    user_score += 1
                
                print_score(user_score, computer_score, rounds)
            else:
                print(Fore.RED + "Invalid Input. Please choose 1, 2, or 3.")
                
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            
        play = input(Fore.YELLOW + "\nDo you want to play again? (y/n): ").lower()
        if play == "n":
            print_border()
            print(Fore.GREEN + "Final Statistics".center(50))
            print_score(user_score, computer_score, rounds)
            win_rate = (user_score / rounds * 100) if rounds > 0 else 0
            print(Fore.BLUE + f"Win Rate: {win_rate:.1f}%".center(50))
            print(Fore.GREEN + "\nThanks for playing!".center(50))
            print_border()
            break

if __name__ == "__main__":
    main()