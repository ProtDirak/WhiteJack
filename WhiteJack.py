ranks = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
suits = ("Hearts", "Spades", "Clubs", "Diamonds")

import random

class Card():
   
    def __init__(self, suit, rank):
       
        self.suit = suit
        self.rank = rank
        self.value = ranks[rank]
       
    def __str__(self):
   
        return self.rank + " of " + self.suit
  
class Deck():
   
    def __init__(self):
       
        self.deck_cards = []
       
        for suit in suits:
            for rank in ranks:
                self.deck_cards.append(Card(suit, rank))
               
    def deal_one(self):
       
        return self.deck_cards.pop()
       
    def shuffle(self):
       
        return random.shuffle(self.deck_cards)

mydeck = Deck()
mydeck.shuffle()

class Player():
   
    def __init__(self, name, balance):
       
        self.name = name
        self.balance = balance
        self.player_cards = []
        self.card_values = []

    #probaj tu napraviti __str__ method koji ce isprintati karte u ruci

    def add_balance(self, bet):

        self.balance += bet

    def sub_balance(self,bet):

        self.balance -= bet


#Uvod u igru
print("\n\n\n")
print("--------------------------------------------------------------------------------------------------------------------------")
print("|Welcome to the game of WhiteJack by Mate Ivic. Please give me your name and the amount of $ you would like to play with.|")
print("--------------------------------------------------------------------------------------------------------------------------")

#umetanje imena i s kolko ces para uc u igru
name = input("\nYour name: ")
money = float(input("$: "))
newplayer = Player(name, money)

print(f"\nWelcome to the table, {newplayer.name}.")
print(f"\nYour balance: {newplayer.balance}")

#Stvaranje dilera (u pozadini)
dealer = Player("Dealer", money)

#Dilanje karata dileru
for i in range(2):
    dealer.player_cards.append(mydeck.deal_one())

#Stvaranje liste vrijednosti dilerovih karata
for card in dealer.player_cards:
    dealer.card_values.append(card.value)

#Dilanje prvih karata igracu
print("\nThe dealer deals you two cards:")
for i in range(2):
    newplayer.player_cards.append(mydeck.deal_one())

#Stvaranje liste vrijednosti igracevih karata
for card in newplayer.player_cards:
    newplayer.card_values.append(card.value)

#Prikazivanje svojih karata igracu
for card in newplayer.player_cards:
    print(card)

#Prikazivanje vrijednosti ruke igraca
print(f"The total value of your cards is: {sum(newplayer.card_values)}.")

#Prikazivanje dilerovih karata (jedna okrenuta)
print("\nDealers cards:")
print(f"{dealer.player_cards[0]}")
print("XXXX") #<---- okrenuta karta

inpt = 'a'

while newplayer.balance > 0 and dealer.balance > 0:

    if inpt == 'n':
        break 

    while sum(newplayer.card_values) <= 21:

        bet_input = True
        play_again = True
        yn = True

        if inpt == 'n':
            break

        while bet_input:

            try:
                bet = float(input("\nPlease place your bet: "))

            except:
                print("Please make sure the bet is a number.")

            else:
                if bet > newplayer.balance:
                    print("Your bet was greater than your balance!")

                else:
                    print("We will take your bet.")
                    bet_input = False

        while yn:

            inpt = input("\nWhould you like another card? y(yes), n(no):")

            if inpt == "y":

                print(f"\nYou were dealt: {newplayer.player_cards[-1]}.")
                print("\nYour cards are: ")

                for card in newplayer.player_cards:
                    print(card)

                newplayer.card_values.append(newplayer.player_cards[-1].value)
                print(f"\nThe total value of your cards is: {sum(newplayer.card_values)}.")

                if sum(newplayer.card_values) > 21:
                    print(f"It's a bust! You loose the hand! Your ${bet} goes to the dealers pockets!")

                    newplayer.sub_balance(bet)
                    dealer.add_balance(bet)

                    yn = False

            elif inpt == "n":

                print("Dealers cards: ")

                for card in dealer.player_cards:
                    print(card)

                for card in newplayer.player_cards:
                    print(card.value)

                print(f"\nThe total value of the dealers cards is: {sum(dealer.card_values)}.")
                print(f"The total value of your cards is: {sum(newplayer.card_values)}")

                if sum(newplayer.card_values) > sum(dealer.card_values):
                    print(f"\nYou win the hand! Dealers {bet} will be added to your ballance.")

                    newplayer.add_balance(bet)
                    dealer.sub_balance(bet)

                    yn = False

                elif sum(newplayer.card_values) == sum(dealer.card_values):

                    print("It's a tie! Nobody looses anything.")

                    yn = False

                else:
                    print(f"You loose the hand! Your ${bet} goes to the dealers pockets.")

                    newplayer.sub_balance(bet)
                    dealer.add_balance(bet)

                    yn = False

        print(f"\nYour balance: {newplayer.balance}\nDealers balance: {dealer.balance}")

        while play_again:

            if newplayer.balance <= 0: 
                print("You lose the game.")
                play_again = False
                inpt == 'n'
                break

            if dealer.balance <= 0:
                print("You win the game.")
                play_again = False
                inpt == 'n'
                break

            inpt = input("Would yo like to keep playing? 'y' for yes or 'n' for no.")

            if newplayer.balance == 0 or dealer.balance == 0:
                play_again = False
                inpt == 'n'

            if inpt == 'y':
                #reshufflanje karata.
                mydeck = Deck()
                mydeck.shuffle()
                #Resetiranje igraceve ruke
                newplayer.player_cards = []
                #Resetiranje liste vrijednosti
                newplayer.card_values = []
                #Resetiranje dilerove ruke
                dealer.player_cards = []
                #Resetiranje lise vrijednosti
                dealer.card_values = []

                #Dilanje karata/vrijednosti igracu
                print("\nThe dealer deals you two cards:")
                for i in range(2):
                    newplayer.player_cards.append(mydeck.deal_one())

                for card in newplayer.player_cards:
                    newplayer.card_values.append(card.value)

                #Dilanje karata/vrijednosti dealeru
                for i in range(2):
                    dealer.player_cards.append(mydeck.deal_one())

                for card in dealer.player_cards:
                    dealer.card_values.append(card.value)

                #Prikazivanje igracevih i dilerovih karata\vrijednosti:
                for card in newplayer.player_cards:
                    print(card)

                print(f"The total value of your cards is: {sum(newplayer.card_values)}.")

                print("\nDealers cards:")
                print(f"{dealer.player_cards[0]}")
                print("XXXX") #<---- okrenuta karta

                play_again = False

            elif inpt == 'n':

                play_again = False

print(f"Thank you for playing, {newplayer.name}. See you again next time!")
print("Beta testers: Aldo Arena")