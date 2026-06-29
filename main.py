from random import *

print("    WELCOME TO NUMBER GUESSING GAME !")

user_name = input("Enter your name ")

print("Welcome", user_name)
computer_guess= randint(1,50)
# condition =True no use of it rather just use while true 
while True:   #condition==True no use of it 
    user_guess=int(input("Enter a number between 1 and 50 both included"))
    if user_guess>0 and user_guess<51:
            if user_guess > computer_guess:
                print("TOO high,guess lower")
            elif user_guess<computer_guess:
                print("TOO low, guess higher")    
                    
            else:
                print("Congrats,you guess the right number !")
                # condition=False
                break
    else:
            print("Invalid input !, Enter no between 1 and 50 both included")

print("Game over !")

# improvement 1 here we can use while true rather than condition true and where are we using the conditon = false to break the looop we can use break instead


