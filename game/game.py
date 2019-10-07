import random


class Card(object):
    card_to_name = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
                    8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.name = "%s of %s" % (self.card_to_name[value], suit)

    def is_royalty(self):
        if self.value == 1:
            return 4
        elif self.value == 11:
            return 1
        elif self.value == 12:
            return 2
        elif self.value == 13:
            return 3
        else:
            return 0

    def __str__(self):
        return "Card("+self.name+")"


class Hand(object):

    def __init__(self, cards=[]):
        self.hand = cards

    def play_card(self):
        return self.hand.pop(0)

    def receive_card(self, card):
        self.hand.append(card)

    def receive_stack(self, cards):
        for card in cards:
            self.hand.append(card)

    def has_cards(self):
        return not len(self.hand) == 0

    def __str__(self):
        string = "Hand("
        for card in self.hand:
            string += card.__str__() + ", "
        if len(self.hand) > 0:
            string = string[:-2]
        return string + ")"


class Deck(object):

    basic_deck = [Card(value, suit) for value in range(1, 14) for suit in ["Diamonds", "Clubs", "Hearts", "Spades"]]

    def __init__(self, num_decks=1):
        self.deck = self.basic_deck * num_decks
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)

    """
    players will be a list of 
    """
    def deal_all_cards(self, players):
        player = players[0]
        while self.deck:
            player.hand.receive_card(self.deal_card())


class Pile(object):

    def __init__(self):
        self.pile = []

    def add_card(self, card):
        self.pile.append(card)

    def burn_card(self, card):
        self.pile.insert(0, card)

    def empty_pile(self):
        cards = self.pile
        self.pile = []
        return cards

    def pair(self):
        if len(self.pile) > 1:
            if self.pile[-1].value == self.pile[-2].value:
                return True
        return False

    def sandwich(self):
        if len(self.pile) > 2:
            if self.pile[-1].value == self.pile[-3].value:
                return True
        return False


class Player(object):

    def __init__(self, letter, name="Player"):
        self.name = name
        self.letter = letter
        self.hand = Hand()

    def pickup_pile(self, pile):
        self.hand.receive_stack(pile.empty_pile())

    def play_card(self, pile):
        card = self.hand.play_card()
        pile.add_card(card)
        return card

    def burn_card(self, pile):
        pile.burn_card(self.hand.play_card())

    def has_cards(self):
        return self.hand.has_cards()

    def __str__(self):
        return 'PLayer(name='+self.name+', letter='+self.letter+')'


class Game(object):

    def __init__(self, players, num_decks=1):
        self.players = players
        self.deck = Deck(num_decks)
        self.pile = Pile()

    def deal_cards(self):
        self.deck.deal_all_cards(self.players)

    def play_game(self):
        current_player = 0
        royal = False
        royalty_count = 0
        while self.check_conditions():
            card = self.players[current_player].play_card(self.pile)
            print("%-*s played %s" % (20, players[current_player].name, card))
            slap = input()
            if len(slap) > 0:
                slap = slap[0]
                for index in range(len(players)):
                    if players[index].letter == slap:
                        if self.pile.sandwich():
                            print("%-*s slapped a sandwich, the pile is given to them" % (20, players[index].name))
                            players[index].pickup_pile(self.pile)
                            current_player = index
                            royal = False
                            royalty_count = 0
                            continue
                        elif self.pile.pair():
                            print("%-*s slapped a pair, the pile is given to them" % (20, players[index].name))
                            players[index].pickup_pile(self.pile)
                            current_player = index
                            royal = False
                            royalty_count = 0
                            continue
                        else:
                            print("%-*s slapped nothing, they burn a card" % (20, players[index].name))
                            players[index].burn_card(self.pile)

            royalty_val = card.is_royalty()
            if royalty_val > 0:
                royal = True
                royalty_count = royalty_val
                current_player = self.next_player(current_player)
                continue
            elif royal:
                royalty_count -= 1
                if royalty_count > 0:
                    continue

                else:
                    print("%-*s failed to place a face card, so %-*s gets the pile" % (20, players[current_player].name, 20, players[self.previous_player(current_player)].name))
                    players[self.previous_player(current_player)].pickup_pile(self.pile)
                    royalty_count = 0
                    royal = False
                    current_player = self.previous_player(current_player)
                    continue

            current_player = self.next_player(current_player)

    def next_player(self, index):
        if index == len(self.players) - 1:
            return 0
        else:
            return index + 1

    def previous_player(self, index):
        if index == 0:
            return -1
        else:
            return index - 1

    def check_conditions(self):
        if len(self.players) == 1:
            print("Player %-*s is the only one left and wins the game! Congrats!" % (20, self.players[0].name))
            return False
        remove_players = []
        for player in self.players:
            if not player.has_cards():
                print("Player %-*s has run out of cards and is out of the game" % (20, player.name))
                remove_players.append(player)
        for r in remove_players:
            self.players.remove(r)
        return True



if __name__ == "__main__":
    print("Welcome to Egyptian Rat Race! Make sure to read the rules and instructions in the README")
    print("How many players are playing?")
    while True:
        num_players = input()
        try:
            num_players = int(num_players)
            break
        except ValueError:
            print("Please enter an integer")
    players = []
    for i in range(num_players):
        print("What is the name of player %i? (keep under 20 characters)" % i)
        while True:
            name = str(input())
            if name in [player.name for player in players]:
                print("That name has already been used, use something else")
            else:
                break
        print("What key would %s like to use?" % name)
        while True:
            key = input()
            if key in [player.letter for player in players]:
                print("That letter has already been used, use something else")
            elif len(key) == 1:
                break
            print("Please input only one character, accessible on your keyboard")
        players.append(Player(key.lower(), name))

    print("How many decks would you like to use (1 deck works in nearly all situations)?")
    while True:
        num_decks = input()
        try:
            num_decks = int(num_decks)
            break
        except ValueError:
            print("Please enter an integer")


    game = Game(players, num_decks)
    game.deal_cards()

    # now for the actual game logic
    game.play_game()