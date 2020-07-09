import random

def main():
    rolls = ['rock','paper','scissors']
    say_header()
    player = get_player()
    roll = get_roll(player,rolls)
    computer = random.choice(rolls)
    game(roll,computer)
    print('game ended')
    
    

def say_header():
    print('--------------------------')
    print('   Rock Paper Scissors')
    print('--------------------------')


def get_player():
    return input("Enter player 1's name: ")

def get_roll(player,rolls):
    while True:
        roll = input(f"{player}, what is your roll? [rock, paper, scissors]:")
        if roll not in rolls:
            print('not a valid roll, try again')
        else:
            return roll


def game(roll,computer):
    if roll == 'rock':
        def switch(computer):
            switcher = {
                'rock': 'draw',
                'paper': 'lose',
                'scissors': 'win'
            }
            print(f'computer chose {computer}')
            return switcher.get(computer,'error')
        print(switch(computer))

    if roll == 'paper':
        def switch(computer):
            switcher = {
                'rock': 'win',
                'paper': 'draw',
                'scissors': 'lose'
            }
            print(f'computer chose {computer}')
            return switcher.get(computer,'error')
        print(switch(computer))

    if roll == 'scissors':
        def switch(computer):
            switcher = {
                'rock': 'lose',
                'paper': 'win',
                'scissors': 'draw'
            }
            print(f'computer chose {computer}')
            return switcher.get(computer,'error')
        print(switch(computer))

    
   



if __name__ == '__main__':
    main()