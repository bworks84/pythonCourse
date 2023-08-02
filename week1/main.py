import random

options = ["rock", "paper", "scissors"]
player_choice = input("Enter a choice (rock, paper, scissors) ")
computer_choice = random.choice(options)


def get_choices():
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


choices = get_choices()

# print(choices)


def check_win(player, computer):
    print(f"You chose {player} and the computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "rock beats scissors, you win!"
        else:
            return "paper covers rock, you lose"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock, you win!"
        else:
            return "scissors cuts paper, you lose!"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cut paper, you win!"
        else:
            return "rock smashes scissors, you lose!"


choices = get_choices()

result = check_win(choices["player"], choices["computer"])

print(result)

# def greeting():
#     return "Hello"

# response = greeting()
# print(response)


# dict = {"name": "rob", "color": "blue"}
# food = ["pizza", "hamburgers", "hotdogs"]
# dinner = random.choice(food)
