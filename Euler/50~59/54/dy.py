import os
from poker import Poker

def test_place(first_deck, second_deck):
  game = poker.Poker(first_deck, second_deck)
  print game.test()


f = open(os.path.expanduser("~/Documents/Development/Python/Project/Euler/input/54.txt"), "r")

first_decks = []
second_decks = []

while True:
    line = f.readline()
    if not line: break

    match = line.strip('\n').split(" ")

    first_decks.append(match[:5])
    second_decks.append(match[5:])


poker_game = Poker(first_decks, second_decks)
print poker_game.play()