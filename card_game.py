import random
import time

suits=('HEARTS','DIAMONDS','SPADES','CLUBS')
ranks=('TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING','ACE')
values={'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9,'TEN':10,'JACK':11,'QUEEN':12,'KING':13,'ACE':14}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank.upper()]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

def len_and_value(P,L,V):
    print(f"Length of player {P} is {L} and value is {V}")

player_one=Player("One")
player_two=Player("Two")

deck=Deck()
#deck.shuffle()

for x in range(26):
    player_one.add_cards(deck.deal_one())
    player_two.add_cards(deck.deal_one())

print("\n\nplayer_one have following cards:\n==================================")
for i in player_one.all_cards:
    print(f"{i}",end=";")
print("\n\nplayer_two have following cards:\n==================================")
for j in player_two.all_cards:
    print(f"{j}",end=";")

print("\n\nGAME ON..............\n")
round_num=0
game_on=True
while game_on:
    round_num+=1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two Wins!")
        game_on=False
        break
    elif len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One Wins!")
        game_on=False
        break

    player1cards=[]
    player1cards.append(player_one.remove_one())
    player2cards=[]
    player2cards.append(player_two.remove_one())

    at_war=True

    while at_war:
        if player1cards[-1].value > player2cards[-1].value:
            player_one.add_cards(player1cards)
            player_one.add_cards(player2cards)

            at_war=False
        elif player1cards[-1].value < player2cards[-1].value:
            player_two.add_cards(player1cards)
            player_two.add_cards(player2cards)

            at_war=False
        else:
            print("WAR!")
            player1cards.append(player_one.remove_one())
            player2cards.append(player_two.remove_one())
            if len(player_one.all_cards) == 0 or len(player_two.all_cards) == 0:
                at_war=False
                break
