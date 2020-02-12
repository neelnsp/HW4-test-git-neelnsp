import unittest
import hw4_cards as stuff

#######################################
##### Name: Neel Shashikant Patel #####
##### Unique: neelsnp             #####
#######################################

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

""" 
Create test as per instructions. Pretty much just test the cases they give and go from there.
Remember "test" before functions and try to keep different variable names as to not get confused. 
"""
class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = stuff.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)
    def test_1_queen_test(self):
        '''
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        '''
        card = stuff.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")
    def test_2_Club_test(self):
        '''
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        '''
        card = stuff.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")
    def test_3_card_string_phrase(self):
        '''
        Test that if you invoke the __str__ method of a card instance that is created with
        suit=3, rank=13, it returns the string "King of Spades"
        '''
        card = stuff.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), "King of Spades")
    def test_4_deck_creation_to_52(self):
        '''
        Test that if you create a deck instance, it will have 52 cards in its cards instance
        variable
        '''
        deck = stuff.Deck()
        self.assertEqual(len(deck.cards), 52)
    def test_5_get_a_card_instance(self):
        '''
        Test that if you invoke the deal_card method on a deck, it will return a card
        instance.
        '''
        deck = stuff.Deck()
        card_from_deck = deck.deal_card()
        self.assertEqual(card_from_deck.__str__(), "King of Spades")
        new_card = stuff.Card()
        self.assertEqual(type(card_from_deck), type(new_card))
    def test_6_deck_is_one_less(self):
        '''
        Test that if you invoke the deal_card method on a deck, the deck has one fewer
        cards in it afterwards.
        '''
        deck = stuff.Deck()
        original_len = len(deck.cards)
        _ = deck.deal_card()
        new_len = len(deck.cards)
        self.assertEqual(original_len-1, new_len)
    def test_7_one_more_card(self):
        '''
        Test that if you invoke the replace_card method, the deck has one more card in it
        afterwards. (Please note that you want to use deal_card function first to remove a
        card from the deck and then add the same card back in)
        '''
        deck = stuff.Deck()
        original_len =  len(deck.cards)
        card = deck.deal_card()
        deck.replace_card(card)
        new_len = len(deck.cards) 
        self.assertEqual(original_len, new_len)
    def test_8_sizer(self):
        '''
        Test that if you invoke the re_card method with a card that is already in the deck,
        the deck size is not affected.(The function must silently ignore it if you try to add 
        a card that’s already in the deck)
        '''
        deck = stuff.Deck()
        original_len = len(deck.cards) 
        card = stuff.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), deck.cards[-1].__str__()) 
        deck.replace_card(card)
        new_len = len(deck.cards)
        self.assertEqual(original_len, new_len)

if __name__ == "__main__":
    unittest.main()


