import random

def greeetings():
    player_choice = input("enter your choice (Rock,pepper ,scissors): ")
    options = ["Rock","papper","scissors"]
    computer_choice = random.choices(options)
    choices = {"computer":computer_choice,"player":player_choice}
    return choices

def check_win(player,computer):
    print(f"you choose {player} and computer chose {computer}")
    if player == computer:
        return "match is a draw"
    elif player == "Rock":
        if computer == "scissors":
            return "Rock smash scissors! You win"
        else :
            return "papper covers rock! you lose"
    elif player == "papper":
        if computer == "Rock":
            return "papper covers rock! You win"
        else :
            return "scissors cuts papper! you lose"
    elif player == "scissors":
        if computer == "papper":
            return "scissors cuts papper! You win"
        else :
            return "rock smashes scissors! you lose"

choices = greeetings()

print(check_win(choices['player'],choices['computer']))