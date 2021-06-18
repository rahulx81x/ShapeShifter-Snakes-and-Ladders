import random
import turn
import time
from dices import d


class Player:
    def __init__(self, number, position):
        self.number = number
        self.position = position


consent = 'y'

while consent == 'y':

        count = int(input('\nEnter no. of players(<=4 for better experience): '))
        P = []  # Player List

        for index in range(count):
            P.append(Player(index, 0))
        winner = 0
        while winner == 0:
            for index in range(count):
                while P[index].position != 100:
                    print("Your turn : Player", end=" ")
                    print(P[index].number + 1)
                    try:
                        dice = int(input('Enter Dice Number(1, 2, 3, 4): '))
                        throw = int(random.choice(d[dice - 1]))
                        turn.turn(P[index], throw)
                    except IndexError:
                        print('Choose a dice from the list 1-4 next turn\n')
                    if P[index].position == 100:
                        winner = 1
                    break
        print("GAME HAS ENDED. CONGRATULATIONS TO THE WINNER. HOPE YOU ALL ENJOYED!!")
        consent = input('\n HEY! Let\'s play again \nInput y for Yes, anything else otherwise: ')


print('\n Hope to see you soon')
print("-rahulx81x")

time.sleep(3)
# rahulx81x

