import unittest

from game_state_model import Vial
from game_state_model import GameState

class TestGameCreation(unittest.TestCase):
    def test_finishedgame(self):
        g = GameState('aaaabbbb')
        self.assertTrue(g.isSolved())
    
    def test_finishedvial(self):
        g = GameState('abaabaab')
        self.assertFalse(g.isSolved())
        
    def test_invalidinitstring(self):
        s = 'aa'
        with self.assertRaises(ValueError):
            GameState(s)

class TestVialCreation(unittest.TestCase):
    def test_emptyvial(self):
        v = Vial('    ')
        self.assertEqual(v.__repr__(), '    ')
    
    def test_finishedvial(self):
        v = Vial('aaaa')
        self.assertEqual(v.__repr__(), 'aaaa')
    
    def test_scrambledvial(self):
        v = Vial('abac')
        self.assertEqual(v.__repr__(), 'abac')
        
    def test_invalidinitstring(self):
        s = 'aa'
        with self.assertRaises(ValueError):
            Vial(s)

class TestVialCapacities(unittest.TestCase):
    def test_emptyvial(self):
        v = Vial('    ')
        self.assertEqual(v.canFillWith(), (4, '*'))
    
    def test_finishedvial(self):
        v = Vial('aaaa')
        self.assertEqual(v.canFillWith(), (0, ' '))
    
    def test_scrambledvial(self):
        v = Vial('abac')
        self.assertEqual(v.canFillWith(), (0, ' '))
    
    def test_partialvial(self):
        v = Vial('abc ')
        self.assertEqual(v.canFillWith(), (1, 'c'))

        v = Vial('ab  ')
        self.assertEqual(v.canFillWith(), (2, 'b'))

        v = Vial('a   ')
        self.assertEqual(v.canFillWith(), (3, 'a'))

class TestVialTopLayer(unittest.TestCase):
    def test_emptyvial(self):
        v = Vial('    ')
        self.assertEqual(v.topLayer(), (0, '*'))
    
    def test_finishedvial(self):
        v = Vial('aaaa')
        self.assertEqual(v.topLayer(), (4, 'a'))
    
    def test_scrambledvial(self):
        v = Vial('abac')
        self.assertEqual(v.topLayer(), (1, 'c'))
    
    def test_partialvial(self):
        v = Vial('acc ')
        self.assertEqual(v.topLayer(), (2, 'c'))

        v = Vial('a   ')
        self.assertEqual(v.topLayer(), (1, 'a'))

if __name__ == '__main__':
    unittest.main()