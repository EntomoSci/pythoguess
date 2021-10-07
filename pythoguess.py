import random


def history():
    print('''
                                         |
                                         |
                                         |
                                         |
   _______                   ________    |
  |ooooooo|      ____       | __  __ |   |
  |[]+++[]|     [____]      |/  \/  \|   |
  |+ ___ +|     ]()()[      |\__/\__/|   |
  |:|   |:|   ___\__/___    |[][][][]|   |
  |:|___|:|  |__|    |__|   |++++++++|   |
  |[]===[]|   |_|_/\_|_|    | ______ |   |
_ ||||||||| _ | | __ | | __ ||______|| __|
  |_______|   |_|[::]|_|    |________|  \\
              \_|_||_|_/                 \\
                |_||_|                    \\
               _|_||_|_                    \\
      ____    |___||___|                    \\
     /  __\          ____                    \\
     \( oo          (___ \                    \\
     _\_o/           oo~)/
    / \|/ \         _\-_/_
   / / __\ \___    / \|/ \\
   \ \|   |__/_)  / / .-\ \\
    \/_)  |       \ \ .  /_/
     ||___|        \/___(_/
     | | |          | |  |
     | | |          | |  |
     |_|_|          |_|__|
     [__)_)        (_(___] -- jro --

Part 1:
Many years ago, in the computer labs from Platziland of the Pythonist Facundo Garcia... one robot was created.
Proclaims to be the most intelligent robot ever built, even proclaims to be smart than his
pythonist creators. And he propose a challenge for them.
    ''')
    user_response = input('Press enter to continue')
    print('''
        
       ___________
     / |         |\\
    |_______________|
____|__/( )| |( )\__|____
\___|      | |      |___/
 ___|\     |_|     /|___
/___| \           / |__\\
     \| /  ___  \ |/
      \ | / _ \ | /
       \_________/
        _|_____|_
   ____|_________|____
  /                   \  -- Adaptation of a Mark Moir ASCII draw

Part 2:
The robot say:
"I will demonstrate my power over humans creating a random number between 1 and 100.
Your mission is try to adivinate that number. If I win, I am the most intelligent creature
in this tridimentional reality. If you win... you got my permission to keep learning
the programming language used to bring me to life, Python."
    ''')
    user_response = input('Press enter to continue')
    print('''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 XXXXXXXXXXXXXXXXXX         XXXXXXXX
XXXXXXXXXXXXXXXX              XXXXXXX
XXXXXXXXXXXXX                   XXXXX
 XXX     _________ _________     XXX      THE
  XX    I  _xxxxx I xxxxx_  I    XX        LOCKER
 ( X----I         I         I----X )           GNOME
( +I    I      00 I 00      I    I+ )
 ( I    I    __0  I  0__    I    I )
  (I    I______ /   \_______I    I)
   I           ( ___ )           I
   I    _  :::::::::::::::  _    i
    \    \___ ::::::::: ___/    /
     \_      \_________/      _/
       \        \___,        /
         \                 /
          |\             /|
          |  \_________/  |

Part 3:
The pythonists respond:
"Pfff... easy peasy. That challenge is so trivial for us, with a reward of... nothing!
But, only to demonstrate you, we accept your challenge." 
    ''')
    user_response = input('Press enter to continue')
    print('''

Welcome to PythoGuess!

    In this game the machine generates a random number between 1 and 100.
    Your mission is try to adivinate that number 25 times before lose all your lives.

    How to play:

    -You starts with 10 lives.
    -If you fail, you lose 1 live and the machine tells you if the number you chose is less than or greater than the secret number.
    -If you adivinate the number, you gain 5 lives! but... the max range increases in 10!.
    -If you guess the secret number 25 times ¡You win! ah... and you will have the permission of the robot to keep learning python.

    Try to win as much as you can.
    
    ¡Good luck!

    ''')


def run():
    history()
    max_range = 100
    user_lives = 10
    wins = 0
    machine_number = random.randint(1, max_range)

    while user_lives > 0:
        if wins == 25:
            print('''
    ¡¡¡CONGRATULATIONS!!!
    
    You beat the machine challenge!
    You proved to be smarter (or luckier) than the machine!
    And even more smarter (or luckier) than the creator of the program!
    You!...now have the permission to keep learning python.
            ''')
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

    print('''
      _____________
     /  GAME OVER  \
    |_______________|
____|__/( )| |( )\__|____
\___|      | |      |___/
 ___|\     |_|     /|___
/___| \  |     |  / |___\
     \|   \___/   |/
      \           /
       \_________/
        _|_____|_
   ____|_________|____
  /                   \  -- Adaptation of a Mark Moir ASCII draw

"Almost feel shame for you.
Don't worry, the creator of
the game couldn't beat me either"
    
Your highest streak was {}
The creator highest streak was 11 (for now)
    '''.format(wins))
        

if __name__ == '__main__':
    run()
