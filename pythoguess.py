import random


history_path = './messages/history/'
game_history = {
    "part_1": open(history_path + 'part_1.txt', 'r'),
    "part_2": open(history_path + 'part_2.txt', 'r'),
    "part_3": open(history_path + 'part_3.txt', 'r'),
}


game_events = {
    "instructions": open('./messages/instructions.txt', 'r'),
    "gameover": open('./messages/gameover.txt', 'r'),
    "win": open('./messages/win.txt', 'r')
}


def run():

    # History of the game
    history_part = 1
    while True:
        current_history_part = game_history['part_{}'.format(history_part)].read()
        print(current_history_part)
        user_response = input('Press enter to continue ')
        history_part += 1

        if history_part > 3:
            break

    # Starting the game
    print(game_events['instructions'].read())
    max_range = 100
    user_lives = 10
    wins = 0
    machine_number = random.randint(1, max_range)

    while user_lives > 0:
        if wins == 25:
            print(game_events['win'].read()) # Winning the game
            return

        print('''
Guessed: {}/25
Lives: {}
        '''.format(wins, user_lives))

        user_number = input('Number: ')
        try:
            user_number = int(user_number)
        except:
            print('\nEnter a valid number!\n')
            continue

        if user_number == machine_number:
            user_lives += 5
            max_range += 10
            wins += 1
            print('''
    You found it!
    You earn +5 lives!
    The machine increase the maximum range to {}
    Keep going!
            '''.format(max_range))

            machine_number = random.randint(1, max_range) # resets the machine number to a new random number more difficult to adivinate.
        elif user_number < machine_number:
            user_lives -= 1
            print('''
    Nop, the number is greater...
    Remaining lives: {}
            '''.format(user_lives))

        elif user_number > machine_number:
            user_lives -= 1
            print('''
    Nop, the number is minor...
    Remaining lives: {}
            '''.format(user_lives))

    # Losing the game
    print(game_events['gameover'].read())
        

if __name__ == '__main__':
    run()
