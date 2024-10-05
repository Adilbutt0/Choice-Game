import random
from colorama import Fore , init
init(autoreset=True)
NUM_ROUNDS = 1
score = 0
print(Fore.GREEN + "Welcome To Game!")
while NUM_ROUNDS <= 3:
    user_num = random.randint(1,100)
    comp_num = random.randint(1,100)
    NUM_ROUNDS += 1
    print(f"Your Number: {user_num}")
    choice = input("do you think high or low?:")

    if user_num < comp_num:
        if choice.lower() == "low":
            score += 1
            print(Fore.GREEN + f"You Were Right! The computer number was : {comp_num} Your Score Is Now {score}")
        else:
            if score == 0:
                score = 0
                print(Fore.RED + f"you were wrong! the computer num was : {comp_num} your score is now {score}")
            else:
                score -= 1
                print(Fore.RED + f"you were wrong! the computer num was : {comp_num} your score is now {score}")
    elif user_num == comp_num:
        if choice.lower() == "high":
            if score == 0:
                score = 0
                print(Fore.RED + f"you were wrong! the computer num was : {comp_num} your score is now {score}")
            else:
                score -= 1
                print(Fore.RED + f"you were wrong! the computer num was : {comp_num} your score is now {score}")
        else:
            if score == 0:
                score = 0
                print(Fore.RED + f"you were wrong! the computer num was : {comp_num} your score is now {score}")
            else:
                score -= 1
                print(Fore.RED + f"you were wrong! the computer num was : {comp_num} your score is now {score}")
    elif user_num > comp_num:
        if choice.lower() == "high":
            score += 1
            print(Fore.GREEN + f"you were right! the computer number was : {comp_num} Your Score IS Now {score}")
    
        else:
            if score == 0:
                score = 0
                print(Fore.RED + f"you were wrong! the computer num was : {comp_num} your score is now {score}")
            else:
                score -= 1
                print(Fore.RED + f"you were wrong! the computer num was : {comp_num} your score is now {score}")
threshold = 3
if score >= threshold:
    print("Thanks for playing!\Best Gameplay!")
elif (score < threshold) and score != 0:
    print("Thanks for playing!\nGood Gameplay!")
elif score == 0: 
    print("Thanks for playing!\Bad Gameplay!") 
