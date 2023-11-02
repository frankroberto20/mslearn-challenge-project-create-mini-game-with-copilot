# write 'hello world' to the console
print('hello world')

# write a start menu for a game of rock, paper, scissors
def start_game():
    print('Welcome to Rock, Paper, Scissors!')
    print('Please choose to play against the computer or a friend.')
    print('1. Play against the computer')
    print('2. Play against a friend')
    print('3. Quit the game')
    choice = input('Please enter your choice: ')
    if choice == '1':
        print('You chose to play against the computer')
        play_game()
    elif choice == '2':
        print('You chose to play against a friend')
        play_game()
    elif choice == '3':
        print('You chose to quit the game')
        quit_game()
    else:
        print('Please enter a valid choice')
        start_game()
    

def play_game():
    # make a random choice for the computer from 1 to 3
    # 1 = rock, 2 = paper, 3 = scissors
    import random
    computer_choice = random.randint(1,3)
    # store choice message in the format "Computer chose {choice}" in dictionary
    choice_messages = {
        1: "Computer chose Rock",
        2: "Computer chose Paper",
        3: "Computer chose Scissors"
    }

    print('Game is starting')
    print('Please choose your weapon')
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    choice = input('Please enter your choice: ')
    print(choice_messages[computer_choice])
    if choice == '1':
        print('You chose Rock')
        if computer_choice == 1:
            print('Tie')
            start_game()
        elif computer_choice == 2:
            print('Computer wins!')
            start_game()
        elif computer_choice == 3:
            print('You win!')
            start_game()
        else:
            print('Please enter a valid choice')
            play_game()
        start_game()
    elif choice == '2':
        if computer_choice == 1:
            print('You win!')
            start_game()
        elif computer_choice == 2:
            print('Tie')
            start_game()
        elif computer_choice == 3:
            print('Computer wins!')
            start_game()
        else:
            print('Please enter a valid choice')
            play_game()
    elif choice == '3':
        if computer_choice == 1:
            print('Computer wins!')
            start_game()
        elif computer_choice == 2:
            print('You win!')
            start_game()
        elif computer_choice == 3:
            print('Tie')
            start_game()
        else:
            print('Please enter a valid choice')
            play_game()
    else:
        print('Please enter a valid choice')
        play_game()

def quit_game():
    print('Thanks for playing!')
    exit()
