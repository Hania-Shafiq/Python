import random
def play_game():
    options = ["rock", "paper", "scissors"]
    comp_turn = random.choice(options)
    user_turn = input('''
    Press 'r' for rock
    Press 'p' for paper
    Press 's' for scissors
    ''').lower()

    if user_turn == 'r':
        user = "rock"
        print('User chooses:', user)
    elif user_turn == 'p':
        user = "paper"
        print("User chooses:", user)
    elif user_turn == 's':
        user = "scissors"
        print("User chooses:", user)
    else:
        print("Invalid choice")
        return

    print("Computer generated:", comp_turn)

    if comp_turn == user:
        print("It's a tie")
    elif (user == "rock" and comp_turn == "scissors") or (user == 'paper' and comp_turn == "rock") or (
            user == "scissors" and comp_turn == "paper"):
        print("Congratulations, you win!")
    else:
        print("Oh no, you lose")

print('''
Select 1 to play
Select 0 to exit
''')

try:
    start = int(input("Choose 1 or 0: "))
    if start not in [0, 1]:
        raise ValueError
except ValueError:
    print("Invalid choice")
    exit()

while start == 1:
    play_game()
    
    print('''
    Select 1 to play
    Select 0 to exit
    ''')
    
    try:
        start = int(input("Choose 1 or 0: "))
        if start not in [0, 1]:
            raise ValueError
    except ValueError:
        print("Invalid choice")
        exit()
