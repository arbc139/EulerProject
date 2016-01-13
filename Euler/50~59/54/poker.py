from deck import Deck

class Poker:
############### class variables
  number = {
    '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14
  }

  class_hash = {
    'High Card': 1,
    'One Pair': 2,
    'Two Pairs': 3,
    'Three of a Kind': 4,
    'Straight': 5,
    'Flush': 6,
    'Full House': 7,
    'Four of a Kind': 8,
    'Straight Flush': 9,
    'Royal Flush': 10
  }

############### test method
  @staticmethod
  def test():
    poker_game = Poker([
          ['8C', 'TS', 'KC', '9H', '4S'], ['5C', 'AD', '5D', 'AC', '9C']
      ],[
          ['7D', '2S', '5D', '3S', 'AC'], ['7C' ,'5H', '8D', 'TD', 'KS']
    ])

    print poker_game.play()

############### base methods (init, etc...)
  def __init__(self, first_decks, second_decks):
    self.first_decks = []
    self.second_decks = []

    for first_deck, second_deck in zip(first_decks, second_decks):
      self.first_decks.append( Deck(first_deck) )
      self.second_decks.append( Deck(second_deck) )

############### public methods
  def play(self):
    first_wins = 0

    for first_deck, second_deck in zip(self.first_decks, self.second_decks):
      first_result = first_deck.get_deck_class()
      second_result = second_deck.get_deck_class()

      fields = ['class_id', 'card_info']
      deck_fields = ['class_cards_num', 'class_cards', 'max_card']

      print 'first:\t', first_result
      print 'second:\t', second_result

      if first_result['class_id'] < second_result['class_id']:
        continue # first lose

      # if same class id
      elif first_result['class_id'] == second_result['class_id']:
        if first_result['info']['class_cards_num'] < second_result['info']['class_cards_num']:
          continue # first lose
        elif first_result['info']['class_cards_num'] == second_result['info']['class_cards_num']:
          if first_result['info']['max_card_num'] < second_result['info']['max_card_num']:
            continue # first lose

      first_wins += 1

    return first_wins



# Poker.test()

