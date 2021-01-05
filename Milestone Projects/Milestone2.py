import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#cree las cartas 
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}' 

#cree el mazo con las cartas 
class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return f'The deck has:{deck_comp}'
    def deal_cards(self):
        return self.all_cards.pop()

'''my_deck = Deck()
print(my_deck)
my_deck.shuffle_deck()
print(my_deck)
my_deck.deal_cards()
print(my_deck)'''

#cree lo que puede hacer el jugador sin tomar las apuestas
class Player():
    def __init__(self):
        self.cards = []
        self.value = 0 
        self.aces = 0
    def hit(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#cree las apuestas
class Apuesta():
    def __init__(self):
        self.total = 100
        self.bet = 0 
    def win_bet(self):
        self.total += self.bet * 2
    def lose_bet(self):
        self.total -= self.bet

#defino las funciones para poder hacer acciones 

#empezamos con las apuestas
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please provide your bet: '))
        except:
            print('Bet could not be accepted, try again!')
            continue
        else:
            if chips.bet > chips.total:
                print('Bet is bigger than balance. Pleas try again!')
            else:
                return 'Bet accepted! You are betting ${}'.format(chips.bet)

#pedir cartas 
def hit(deck,hand):
    hand.hit(deck.deal_cards())
    hand.adjust_ace()

# preguntar si pide o si se queda 
jugando = True
def hit_or_stand(deck,hand):
    global jugando
    while True:
        preguntar = input('Hit or Stand? Enter (H-S): ')
        if preguntar.lower().startswith('h'):
            hand.hit(deck.deal_cards())
        elif preguntar.lower().startswith('s'):
            print('Dealer is playing!')
            jugando = False
        else:
            print('Please try again!')
            continue
        break

#mostrar las cartas cuando recien empieza la partida (jugador se ven las dos y dealer solo se ve 1)
def show_some(player,dealer):
    print(f'Jugador tiene:')
    print('\n'.join(map(str,player.cards)))
    print(f'Jugador tiene:\n{player.value}')
    print('Dealer tiene:\n{}'.format(dealer.cards[1]))

#cuando le toca jugar al dealer se tienen que mostrar todas las cartas, por lo tanto se da vuelta la carta que estaba dada vuelta 
def show_all(player,dealer):
    print(f'Jugador tiene:')
    print('\n'.join(map(str,player.cards)))
    print(f'Jugador tiene:\n{player.value}')
    print('Dealer tiene:')
    print('\n'.join(map(str,dealer.cards)))
    print('Dealer tiene:\n{}'.format(dealer.value))

#todas las formas en que termina la partida 
#jugador pierde
def player_busts(player,dealer,chips): #se pasa de 21 o dealer tiene mas que jugador y menos q 21
    print('Jugador se pasa!')
    chips.lose_bet()

#jugador gana 
def player_wins(player,dealer,chips):
    print('Jugador gana!')
    chips.win_bet()

#dealer pierde
def dealer_busts(player,dealer,chips):
    print('Dealer se pasa!')
    chips.win_bet()

#dealer gana 
def dealer_wins(player,dealer,chips):
    print('Dealer Gana!')
    chips.lose_bet()

#empate 
def push(player,dealer,chips):
    print('Empate!')

#game logic
while True:
    #introduccion
    print('Bienvenido a BlackJack 21!')
    #creo el mazo
    deck = Deck()
    deck.shuffle_deck()
    #mano de jugador y mano de dealer
    player1 = Player()
    player1.hit(deck.deal_cards())
    player1.hit(deck.deal_cards())
    #mano de dealer
    dealer = Player()
    dealer.hit(deck.deal_cards())
    dealer.hit(deck.deal_cards())
    #set up de las chips que tiene el jugador
    player1_chips = Apuesta()
    #set up para la apuesta del jugador 
    take_bet(player1_chips)
    #mostrar las dos cartas del jugador pero solo 1 del dealer 
    show_some(player1,dealer)
    while jugando:
        #preguntarle si quiere pedir o quedarse 
        hit_or_stand(deck,player1)
        show_some(player1,dealer)      
        if player1.value > 21:
            player_busts(player1,dealer,player1_chips)
            break
    if player1.value <= 21:
        while dealer.value <= 17:
            hit(deck,dealer)
            show_all(player1,dealer)
        if dealer.value > 21:
            dealer_busts(player1,dealer,player1_chips)
        elif dealer.value > player1.value:
            dealer_wins(player1,dealer,player1_chips)
        elif dealer.value < player1.value:
            player_wins(player1,dealer,player1_chips)
        else:
            push(player1,dealer,player1_chips)
    print('\nEl jugador hasta ahora tiene {}'.format(player1_chips.total))

    #preguntar si va a jugar de nuevo o si se retira
    pregunta = input('Jugar de nuevo? (Si/No): ')

    if pregunta[0].lower() == 's':
        jugando = True
        continue
    else:
        print('Gracias por jugar!')
        break