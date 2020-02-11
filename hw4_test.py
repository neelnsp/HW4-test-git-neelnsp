import unittest
import hw4_cards as stuff

#######################################
##### Name: Neel Shashikant Patel #####
##### Unique: neelsnp             #####
#######################################
""" 
Create test as per instructions. Pretty much just test the cases they give and go from there.
Remember "test" before functions and try to keep different variable names as to not get confused. 
"""
class TestCard(unittest.TestCase):
    def test_0_create(self):
        card = stuff.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)
    def test_1_queen(self):
        card = stuff.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")
    def test_2_Clubs(self):
        card = stuff.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")
    def test_3_king_of_spade(self):
        card = stuff.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), "King of Spades")
    def test_4_deck(self):
        deck = stuff.Deck()
        self.assertEqual(len(deck.cards), 52)
    def test_5_deckcard(self):
        deck = stuff.Deck()
        card_from_deck = deck.deal_card()
        self.assertEqual(card_from_deck.__str__(), "King of Spades")
        new_card = stuff.Card()
        self.assertEqual(type(card_from_deck), type(new_card))
    def test_6_decklen(self):
        deck = stuff.Deck()
        original_len = len(deck.cards)
        _ = deck.deal_card()
        new_len = len(deck.cards)
        self.assertEqual(original_len-1, new_len)
    def test_7_replace(self):
        deck = stuff.Deck()
        original_len =  len(deck.cards)
        card = deck.deal_card()
        deck.replace_card(card)
        new_len = len(deck.cards) 
        self.assertEqual(original_len, new_len)
    def test_8_already(self):
        deck = stuff.Deck()
        original_len = len(deck.cards) 
        card = stuff.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), deck.cards[-1].__str__()) 
        deck.replace_card(card)
        new_len = len(deck.cards)
        self.assertEqual(original_len, new_len)

if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()


