import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

'''
two_hearts = Card('Hearts','two')
print(two_hearts)
two_hearts.suit
two_hearts.rank
two_hearts.value
three_of_clubs = Card('Club', 'Three')
three_of_clubs.suit
three_of_clubs.rank
three_of_clubs.value
two_hearts.value < three_of_clubs.value
'''

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
         random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

'''my_deck = Deck()
for card_object in my_deck.all_cards:
    print(card_object)

new_deck = Deck()
new_deck.shuffle()
print(new_deck.all_cards[0])
my_card = new_deck.deal_one()
print(my_card)
len(new_deck.all_cards)'''

class Player():
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

'''new_player = Player('Pedro')
print(new_player)
new_player.add_cards(my_card)
print(new_player)
print(new_player.all_cards[0])
new_player.add_cards([my_card,my_card,my_card])
new_player.remove_one()'''

#game setup
player_one = Player('One')
player_two = Player('Two')
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

#while game on
round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One wins!')
        game_on = False
        break
    #start a new round 
    player_one_cards_in_play = []
    player_one_cards_in_play.append(player_one.remove_one())
    player_two_cards_in_play = []
    player_two_cards_in_play.append(player_two.remove_one())

    #while at_war
    at_war = True
    while at_war:
        if player_one_cards_in_play[-1].value > player_two_cards_in_play[-1].value:
            player_one.add_cards(player_one_cards_in_play)
            player_one.add_cards(player_two_cards_in_play)
            at_war = False 
        elif player_one_cards_in_play[-1].value < player_two_cards_in_play[-1].value:
            player_two.add_cards(player_two_cards_in_play)
            player_two.add_cards(player_one_cards_in_play)
            at_war = False 
        else:
            print('War still going on!')
            if len(player_one.all_cards) < 5:
                print('Player One unable to play war!\nPlayer Two wins!')
                game_on = False
                break
            if len(player_two.all_cards) < 5:
                print('Player Two unable to play war!\nPlayer One wins!')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards_in_play.append(player_one.remove_one)
                    player_two_cards_in_play.append(player_two.remove_one)