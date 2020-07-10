import random

def main():
    rolls = ['rock','paper','scissors']
    say_header()
    player = get_player()
    computer = random.choice(rolls)
    roll = get_roll(player,rolls)
    print(f'You chose {roll}')
    print(f'Computer chose {computer}')
    result(roll, computer)
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

def result(roll, computer):
    if roll == computer:
        print('it\'s a draw') 
    else:    
        matches = {
            'rock': {
                'paper': 'You lose',
                'scissors': 'You win'           
            },
            'paper': {
                'rock': 'You win',
                'scissors': 'You lose'
            },
            'scissors': {
                'rock': 'You lose',
                'paper': 'You win',
            }
        }
        print(matches.get(roll,'Error').get(computer,'Error 2'))


def best_of_three(computer,roll,player):
    game(roll,computer)
    
   



if __name__ == '__main__':
    main()