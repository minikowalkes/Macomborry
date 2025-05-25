import random as r

class Cards:
    def __init__(self):
        self.cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def draw_cards(self):
        card_idx = r.randint(0,(len(self.cards)-1))
        print("You drew:",self.cards[card_idx])
        del self.cards[card_idx]

        if len(self.cards) <= 1:
            self.shuffle_cards()

    def shuffle_cards(self):
        new_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.cards = new_cards
        return self.cards

    def void_loop(self):
        msg = str()
        while msg.lower() != "q":
            msg = input("Would you like to draw a card? Y/N/(Q)uit: ")
            if msg.lower() == "y":
                self.draw_cards()
            elif msg.lower() == "n":
                self.shuffle_cards() # actually stupid logic here.
''' Gotta add a skip turn. Too lazy to do so right now, but
    it should take in "self.cards" current state/status and 
    maintain it for that player when they skip the turn.'''

player_obj = Cards()
player_obj.void_loop()
