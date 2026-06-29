import math as m
import random as r
attempt=8
game_stopped=False
def stop_game():
    global game_stopped
    game_stopped=True



print("Welcome to the Number guessing game !")
want_to_play =input("Enter YES if you want to play  the game else enter NO : ").lower()
if want_to_play != "yes":
    # stop_game()
    print("you quit the game !")

else:

    print("you have to guess the no between 1 to 100 both included")
    random_number=r.randint(1,100)
    while(game_stopped==False and attempt>0):
        guessed_number=int(input("Enter the number : "))

        if(guessed_number>random_number):
            print("TOO HIGH !")
            attempt-=1
            print(f'ATTEMPT LEFT : {attempt}')
        elif(guessed_number<random_number):
            print("TOO LOW")
            attempt-=1
            print(f'ATTEMPT LEFT : {attempt}')


        else:
            print("You guessed the correct number !")

            print(":):) you won the game ! :):)")
            game_stopped=True
    if(attempt==0):
        print(f'you loose the game ! :( ')
        print(f"The correct number was {random_number}")






