import random
import os
from art import logo


cls=lambda: os.system('cls')
computer_number=int()
guess=int()
dif=""
attempts=int()

def random_number():
    
    number=random.randint(1,100)
    return number

def hot_or_cold(num):
    global guess
    global computer_number
    closeness=abs(computer_number-guess)
    if closeness<3:
        return "Super Hot! My blood is boiling!"
    elif closeness<5:
        return "Hot! I could use some ice!"
    elif 5<=closeness<10:
        return "Warm, feels good!"
    elif 10<=closeness<15:
        return "Lil bit chilly!"
    elif 15<=closeness<=30:
        return "It's cold out here!"
    else:
        return "I am going to die bc of freezing. I won't even rot and mix with the soil! "

print(logo)


   
while True:
    dif=input('Choose a difficulty, "hard" or "easy":')
    if dif=="hard":
        attempts=5
    elif dif=="easy":
        attempts=10
    print("I am thinking a number between 1 and 100")
    print(f'You wave {attempts} attempts!')
    computer_number=random_number()
    while attempts!=0:
        guess=int(input("Make a guess:"))
        if guess==computer_number:
            print(f"You win! My number was: {guess}")
            break
        
        else:
            print(hot_or_cold(guess))
            attempts-=1
            if attempts==0:
                print(f"You lost my number was: {computer_number}")
                break
            else:
                print(f'You have {attempts} attempts left!\nGuess again!')
                
                
    play_again=input("Play again? (y/n)")
    cls()
    if play_again=="n":
        print("Bye Bye")
        break        
    
    
    