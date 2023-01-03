import unittest

from game_state_model import GameState

'''
Setup, if you haven't played this game before.
There's a number of vials of different color liquids, always 4 blocks tall.
You also get 2 empty vials.
You need to sort the blocks of liquid, Tower of Hanoi style, until each vial
contains 4 blocks of the same color, and you again have 2 empty vials.

a b       ->      a b
b a _ _   ->  _ _ a b

You can only put like colors on top of each other.
  b    ->    b a             b
a b a  ->  _ b a   NOT   a b a
You can also put any color in a blank vial.

And contiguous colors fill as much as they can.
a         a
a a  -> a a 
b a     b a
'''

class TestMoveValidity(unittest.TestCase):
    def test_samplegame(self):
        g = GameState('aaaa')
        self.assertTrue(g.isValidMove((0, 1)))
        self.assertTrue(g.isValidMove((0, 2)))
        self.assertFalse(g.isValidMove((1, 2)))  # empty into empty
        self.assertFalse(g.isValidMove((1, 0)))  # empty into full    

    def test_partialvials(self):
        f = GameState('aba ba  abaab   ')
        self.assertTrue(f.isValidMove((0, 1)))
        self.assertTrue(f.isValidMove((1, 0)))
        self.assertFalse(f.isValidMove((1, 1)))
        self.assertFalse(f.isValidMove((0, 2)))
        self.assertTrue(f.isValidMove((2, 0)))
        self.assertFalse(f.isValidMove((0, 3)))
        
    def test_invalidmove(self):
        e = GameState('aaaa')
        with self.assertRaises(IndexError):
            e.isValidMove((0, 3))

    def test_invalidmove2(self):
        d = GameState('aaaa')
        with self.assertRaises(IndexError):
            d.isValidMove((3, 0))

class TestMoveVials(unittest.TestCase):
    def test_samplegame(self):
        g = GameState('aaaa')
        g.makeMove((0, 1))
        self.assertEqual(g.vials_[0].__repr__(), '    ')
        self.assertEqual(g.vials_[1].__repr__(), 'aaaa')    

    def test_partialvials(self):
        g = GameState('baa baa ')
        g.makeMove((0, 1))
        self.assertEqual(g.vials_[0].__repr__(), 'ba  ')
        self.assertEqual(g.vials_[1].__repr__(), 'baaa')    

if __name__ == '__main__':
    unittest.main()