import random

while True:
    user_choices = []
    computer_choices = []
    user_score = 0
    computer_score = 0
    for i in range(3):
        while True:
            user_input = input('Enter (rock, paper, scissors):')
            if user_input in user_choices:
                print('You have already chosen', user_input, 'please choose a different option.')
            else:
                break
        user_choices.append(user_input)
        game_actions = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(game_actions)
        while computer_choice in computer_choices:
            computer_choice = random.choice(game_actions)
        computer_choices.append(computer_choice)
        print(f'\nYou chose {user_input}, computer chose {computer_choice}.\n')
        if user_input == computer_choice:
            print(f'Both players selected {user_input}. Its a tie')
        elif user_input == 'rock':
            if computer_choice == 'scissors':
                print('Rock beats scissors! You win!')
                user_score += 1
            else:
                print('Paper beats rock! You lose.')
                computer_score += 1
        elif user_input == 'paper':
            if computer_choice == 'rock':
                print('Paper beats rock!. You win!')
                user_score += 1
            else:
                print('Scissors cuts paper!. You lose.')
                computer_score += 1
        elif user_input == 'scissors':
            if computer_choice == 'paper':
                print('Scissors beat paper!. You win!')
                user_score += 1
            else:
                print('Rock beats scissors!. You lose.')
                computer_score += 1
        if user_score == 2 or computer_score == 2:
            break
    if user_score > computer_score:
        print('You won', user_score, 'out of', i+1, 'rounds. Congratulations!')
    elif computer_score > user_score:
        print('The computer won', computer_score, 'out of', i+1, 'rounds. Better luck next time!')
    else:
        print('The game ended in a tie!')
    play_again = input('Play another set of rounds? (y/n):')
    if play_again.lower() != 'y':
        break
