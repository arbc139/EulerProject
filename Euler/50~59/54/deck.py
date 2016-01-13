class Deck:
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

  fields = ['class_deck_num', 'class_deck', 'max_card']

############### test method
  def test(self, kind):
    if kind == 'High Card':
      return self.__get_highest_card()
    elif kind == 'One Pair':
      return self.__is_one_pair()
    elif kind == 'Two Pairs':
      return self.__is_two_pairs()
    elif kind == 'Three of a Kind':
      return self.__is_three_of_a_kind()
    elif kind == 'Straight':
      return self.__is_straight()
    elif kind == 'Flush':
      return self.__is_flush()
    elif kind == 'Full House':
      return self.__is_full_house()
    elif kind == 'Four of a Kind':
      return self.__is_four_of_a_kind()
    elif kind == 'Straight Flush':
      return self.__is_straight_flush()
    elif kind == 'Royal Flush':
      return self.__is_royal_flush()

############### base methods (init, etc...)
  def __init__(self, cards):
    self.cards = cards

############### public methods
  def get_deck_class(self):
    """
      'High Card'
      'One Pair'
      'Two Pairs'
      'Three of a Kind'
      'Straight'
      'Flush'
      'Full House'
      'Four of a Kind'
      'Straight Flush'
      'Royal Flush'
    """
    # Test Royal Flush
    result = self.__is_royal_flush()
    if result: return Deck.__result_dict_maker(Deck.class_hash['Royal Flush'], result)

    result = self.__is_straight_flush()
    if result: return Deck.__result_dict_maker(Deck.class_hash['Straight Flush'], result)

    result = self.__is_four_of_a_kind()
    if result: return Deck.__result_dict_maker(Deck.class_hash['Four of a Kind'], result)

    result = self.__is_full_house()
    if result: return Deck.__result_dict_maker(Deck.class_hash['Full House'], result)

    result = self.__is_flush()
    if result: return Deck.__result_dict_maker(Deck.class_hash['Flush'], result)

    result = self.__is_straight()
    if result: return Deck.__result_dict_maker(Deck.class_hash['Straight'], result)

    result = self.__is_three_of_a_kind()
    if result: return Deck.__result_dict_maker(Deck.class_hash['Three of a Kind'], result)

    result = self.__is_two_pairs()
    if result: return Deck.__result_dict_maker(Deck.class_hash['Two Pairs'], result)

    result = self.__is_one_pair()
    if result: return Deck.__result_dict_maker(Deck.class_hash['One Pair'], result)

    return Deck.__result_dict_maker(Deck.class_hash['High Card'], self.__get_highest_card())



############### internal methods
#### rules
  def __get_highest_card(self):
    highest_card = self.cards[0]
    for card in self.cards:
      if Deck.__get_number(card) > Deck.__get_number(highest_card):
        highest_card = card
    return Deck.__dict_maker(Deck.__get_number(highest_card), [highest_card], Deck.__get_max_number(self.cards))

  def __is_one_pair(self):
    for i in range(0, len(self.cards)-1):
      for j in range(i+1, len(self.cards)):
        if Deck.__get_number(self.cards[i]) == Deck.__get_number(self.cards[j]):
          return Deck.__dict_maker(Deck.__get_number(self.cards[i]), [self.cards[i], self.cards[j]], Deck.__get_max_number(self.cards))
    return False
    

  def __is_two_pairs(self):
    result = []
    for i in range(0, len(self.cards)-1):
      for j in range(i+1, len(self.cards)):
        if Deck.__get_number(self.cards[i]) == Deck.__get_number(self.cards[j]):
          result.append( [self.cards[i], self.cards[j]] )
    if result and len(result) == 2:
      return Deck.__dict_maker(int(max(Deck.__get_number(result[0][0]), Deck.__get_number(result[1][0]))), result, Deck.__get_max_number(self.cards))
    else:
      return False

  def __is_three_of_a_kind(self):
    for i in range(0, len(self.cards)-2):
      for j in range(i+1, len(self.cards)-1):
        for k in range(j+1, len(self.cards)):
          if Deck.__get_number(self.cards[i]) == Deck.__get_number(self.cards[j]) == Deck.__get_number(self.cards[k]):
            return Deck.__dict_maker(Deck.__get_number(self.cards[i]), [self.cards[i], self.cards[j], self.cards[k]], Deck.__get_max_number(self.cards))
    return False

  def __is_straight(self):
    card_number_list = []

    for card in self.cards:
      card_number_list.append(Deck.__get_number(card))

    card_number_list.sort()

    if all(x<y and y==(x+1) for x, y in zip(card_number_list, card_number_list[1:])):
      return Deck.__dict_maker(Deck.__get_max_number(self.cards), self.cards, Deck.__get_max_number(self.cards))
    else:
      return False

  def __is_flush(self):
    card_patterns = set()

    for card in self.cards:
      card_patterns.add(card[1])

    if len(card_patterns) != 1:
      return False
    else:
      return Deck.__dict_maker(Deck.__get_max_number(self.cards), self.cards, Deck.__get_max_number(self.cards))

  def __is_full_house(self):
    triple = self.__is_three_of_a_kind()
    
    if triple is False:
      return False

    triple_cards = triple['class_cards']

    one_pair_cards = []

    for card in self.cards:
      if card in triple_cards:
        continue
      else:
        one_pair_cards.append(card)

    if one_pair_cards[0][0] == one_pair_cards[1][0]:
      return Deck.__dict_maker(Deck.__get_max_number(self.cards), self.cards, Deck.__get_max_number(self.cards))

    else:
      return False


  def __is_four_of_a_kind(self):
    for i in range(0, len(self.cards)-3):
      for j in range(i+1, len(self.cards)-2):
        for k in range(j+1, len(self.cards)-1):
          for l in range(k+1, len(self.cards)):
            if Deck.__get_number(self.cards[i]) == Deck.__get_number(self.cards[j]) == Deck.__get_number(self.cards[k]) == Deck.__get_number(self.cards[l]):
              return Deck.__dict_maker(Deck.__get_number(self.cards[i]), [self.cards[i], self.cards[j], self.cards[k], self.cards[l]], Deck.__get_max_number(self.cards))
    return False

  def __is_straight_flush(self):
    if self.__is_straight() and self.__is_flush():
      return Deck.__dict_maker(Deck.__get_max_number(self.cards), self.cards, Deck.__get_max_number(self.cards))
    else:
      return False

  def __is_royal_flush(self):
    if self.__is_straight_flush() and Deck.__get_max_number(self.cards) == 14:
      return Deck.__dict_maker(Deck.__get_max_number(self.cards), self.cards, Deck.__get_max_number(self.cards))
    else:
      return False



############### tool methods
  @staticmethod
  def __get_number(card):
    return Deck.number[card[0]]

  @staticmethod
  def __get_max_number(cards):
    card_number_list = []

    for card in cards:
      card_number_list.append(Deck.__get_number(card))

    return max(card_number_list)

  @staticmethod
  def __dict_maker(class_cards_num, class_cards, max_card_num):
    return {
      'class_cards_num': class_cards_num,
      'class_cards': class_cards,
      'max_card_num': max_card_num
    }

  @staticmethod
  def __result_dict_maker(class_id, info):
    return {
      'class_id': class_id,
      'info': info
    }

  @staticmethod
  def test_all():
    print '########### High Card Testing ###########'
    Deck.test_rule('High Card', True)
    Deck.test_rule('High Card', False)
    print '########### One Pair Testing ###########'
    Deck.test_rule('One Pair', True)
    Deck.test_rule('One Pair', False)
    print '########### Two Pairs Testing ###########'
    Deck.test_rule('Two Pairs', True)
    Deck.test_rule('Two Pairs', False)
    print '########### Three of a Kind Testing ###########'
    Deck.test_rule('Three of a Kind', True)
    Deck.test_rule('Three of a Kind', False)
    print '########### Straight Testing ###########'
    Deck.test_rule('Straight', True)
    Deck.test_rule('Straight', False)
    print '########### Flush Testing ###########'
    Deck.test_rule('Flush', True)
    Deck.test_rule('Flush', False)
    print '########### Full House Testing ###########'
    Deck.test_rule('Full House', True)
    Deck.test_rule('Full House', False)
    print '########### Four of a Kind Testing ###########'
    Deck.test_rule('Four of a Kind', True)
    Deck.test_rule('Four of a Kind', False)
    print '########### Straight Flush Testing ###########'
    Deck.test_rule('Straight Flush', True)
    Deck.test_rule('Straight Flush', False)
    print '########### Royal Flush Testing ###########'
    Deck.test_rule('Royal Flush', True)
    Deck.test_rule('Royal Flush', False)

  # C, D, H, S
  @staticmethod
  def test_rule(kind, cond):
    if kind == 'High Card':
      test_deck = Deck(['2C', '3D', '8H', 'KS', 'QC'])
      print test_deck.test(kind)

    elif kind == 'One Pair':
      test_deck = Deck(['2C', '2D', '8H', 'KS', 'QC']) if cond else Deck(['2C', '3D', '8H', 'KS', 'QC'])
      print test_deck.test(kind)

    elif kind == 'Two Pairs':
      test_deck = Deck(['2C', '2D', '8H', '8S', 'QC']) if cond else Deck(['2C', '2D', '8H', 'KS', 'QC'])
      print test_deck.test(kind)

    elif kind == 'Three of a Kind':
      test_deck = Deck(['2C', '2D', '2H', '8S', 'QC']) if cond else Deck(['2C', '2D', '8H', 'KS', 'QC'])
      print test_deck.test(kind)

    elif kind == 'Straight':
      test_deck = Deck(['AC', 'JD', 'QH', 'KS', 'TC']) if cond else Deck(['2C', '2D', '8H', 'KS', 'QC'])
      print test_deck.test(kind)

    elif kind == 'Flush':
      test_deck = Deck(['AC', '6C', '7C', '8C', '2C']) if cond else Deck(['2C', '3C', '8C', 'KS', 'AC'])
      print test_deck.test(kind)

    elif kind == 'Full House':
      test_deck = Deck(['8C', '2D', '2H', '8S', '2C']) if cond else Deck(['2C', '2D', '8H', 'KS', 'QC'])
      print test_deck.test(kind)

    elif kind == 'Four of a Kind':
      test_deck = Deck(['QC', '2D', '2H', '2S', '2C']) if cond else Deck(['3C', '2D', '8H', '2S', 'QC'])
      print test_deck.test(kind)

    elif kind == 'Straight Flush':
      test_deck = Deck(['AC', 'TC', 'JC', 'KC', 'QC']) if cond else Deck(['3Q', '2Q', '4H', '6S', '5C'])
      print test_deck.test(kind)

    elif kind == 'Royal Flush':
      test_deck = Deck(['AC', 'QC', 'KC', 'TC', 'JC']) if cond else Deck(['2C', '2D', '8H', 'KS', 'QC'])
      print test_deck.test(kind)

    #print test_deck.test(kind)

"""
TEST KIND LIST

  'High Card'
  'One Pair'
  'Two Pairs'
  'Three of a Kind'
  'Straight'
  'Flush'
  'Full House'
  'Four of a Kind'
  'Straight Flush'
  'Royal Flush'
"""
#Deck.test_all()