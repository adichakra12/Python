from queue import Empty
from classes.deck import Deck
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.is_busted = False
        self.sum = 0
    
    def join_table (self,table):
        table.player_list.append(self)
        return self

    def draw(self):
        if (self.is_busted == False):
            card = bicycle.draw()
            card.card_info()
            self.hand.append(card)

            self.calculate_points()
        else:
            print("wait until next hand")
        self.calculate_points()
        return self

    def hit(self):
        if sum < 14:
            self.draw()
        return self

    def calculate_points(self):
        self.sum = 0
        for i in range(len(self.hand)):
            card = self.hand[i]
            self.sum += card.point_val
        if self.sum > 21:
            self.is_busted = True
            tablea.you_busted(self.name)
        return self

class Dealer (Player):
    def __init__(self, table):
        super().__init__(table)
        self.hand = []
        self.is_busted = False
        self.sum = 0

    def hit(self):
        if self.sum<17:
            self.draw()
        else:
            tablea.determine_winner()
        # return self



class Table:
    def __init__(self):
        self.player_list = []
        self.dealer = Dealer(self)
        print("Welcome to this table")
    
    def you_busted(self, player_name):
        print(f"{player_name} is busted. please wait until next turn")


    def determine_winner(self):
        for i in self.player_list:
            if i.sum > self.dealer.sum and i.is_busted==False:
                print(f"{i.name} is a winner!")
            elif i.is_busted == False and tablea.dealer.is_busted == True:
                print(f"{i.name} is a winner!")
            else:
                print("The house wins.")
    
    def deal(self):
        self.dealer.draw().draw()
        for i in self.player_list:
            i.draw().draw()
        return self

def addPlayer():
    initInput = input('To add player please type add: ')
    player1 = input('What is your name: ')
    player1 = Player(player1)
    table = input("Which table would you like to join? (1, 2, 3)  ")
    # funcitonality to be added later 
    player1.join_table(tablea)
    while(initInput.lower() != 'add'):
        addPlayer = input('Please add a player: ')
        if (addPlayer.lower() == 'add'):
            initInput = addPlayer
        else: 
            continue

bicycle = Deck()
bicycle.shuffle()

tablea = Table()


addPlayer()

addAnother = input('Would you like to add another player (yes or no): ')
if (addAnother.lower() == 'yes'):
    addPlayer()

tablea.deal()

print(f"Dealer sum is: {tablea.dealer.sum}")
for player in tablea.player_list:
    print(f"{player.name} sum is: {player.sum}")
    choice = input("Do you want to hit or stay?  ")
    while(choice == "hit" and player.is_busted == False):
        player.draw()
        print(f"{player.name} sum is: {player.sum}")
        if player.is_busted == True:
            break
        else: 
            choice = input("Do you want to hit or stay?  ")
tablea.dealer.hit()
tablea.determine_winner()



