import random

from snakes_ladders import Snakes, Ladders, Counter


def turn(player, throw):
    player.position += throw
    if player.position in Snakes:
        print("###### Landed on a Snake :( ######")
        player.position -= random.choice(Counter)
    if player.position in Ladders:
        print("###### Landed on a Ladder :)######")
        player.position += random.choice(Counter)
    if player.position > 100:
        player.position -= throw
        print("###### Out of Bounds 2######")
    print("Player ", end="")
    print(player.number + 1, end=" ")
    print('is on position ', end=" ")
    print(player.position)
    if player.position == 100:
        print(" Player", end=" ")
        print(player.number + 1, end=" ")
        print('has already reached home and WON!')
