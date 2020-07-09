import random

def main():
    rolls = ['rock','paper','scissors']
    say_header()
    player = get_player()
    roll = get_roll(player,rolls)
    computer = random.choice(rolls)
    game(roll,computer)
    print('Game ended')
    
    

def say_header():
    print('--------------------------')
    print('   Rock Paper Scissors')
    print('--------------------------')


def get_player():
    return input("Enter player 1's name: ")

def get_roll(player,rolls):
    while True:
        roll = input(f"{player}, what is your roll? [rock, paper, scissors]:").lower()
        if roll not in rolls:
            print('not a valid roll, try again')
        else:
            return roll


def game(roll,computer):
    print(f'You chose {roll}')
    if roll == 'rock':
        def switch(computer):
            switcher = {
                'rock': 'it\'s a draw',
                'paper': 'You lose',
                'scissors': 'You win'
            }
            print(f'Computer chose {computer}')
            return switcher.get(computer,'error')
        print(switch(computer))

    if roll == 'paper':
        def switch(computer):
            switcher = {
                'rock': 'You win',
                'paper': 'it\'s a draw',
                'scissors': 'You lose'
            }
            print(f'Computer chose {computer}')
            return switcher.get(computer,'error')
        print(switch(computer))

    if roll == 'scissors':
        def switch(computer):
            switcher = {
                'rock': 'You lose',
                'paper': 'You win',
                'scissors': 'it\'s a draw'
            }
            print(f'Computer chose {computer}')
            return switcher.get(computer,'error')
        print(switch(computer))

    
   



if __name__ == '__main__':
    main()