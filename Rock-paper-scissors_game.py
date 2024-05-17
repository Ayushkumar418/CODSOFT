import random

def check(com,user):
    if com==user:
        return 0
    elif com == 1 and user == 3:
        return -1
    elif com == 2 and user == 1:
        return -1
    elif com == 3 and user == 2:
        return -1
    return 1

print("Welcome in Rock-paper-Scissors Game.")
while True:
    user = int(input("\nPress 1 for Rock.\nPress 2 for Paper.\nPress 3 for Scissors.\nEnter: "))
    computer = random.randint(1,3)
    dct = {1:"Rock", 2:"Paper", 3:"Scissors"}
    if 1 <= user <=3:
        print(f"You: {dct[user]}\nComputer: {dct[computer]}")
        score = check(computer, user)
        if score == 0:
            print("Game Draw.")
        elif score == -1:
            print("Sorry!, You lose.")
        elif score == 1:
            print("Congratulation, you win.")
    else:
        print("Invalid Input. Try again.")
    play = input("Do you want to play again? (y/n): ")
    if play == "n":
        break