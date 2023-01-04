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

class TestVialAddColor(unittest.TestCase):
    def test_emptyvial(self):
        v = Vial('    ')
        v.addColor('c')
        self.assertEqual(v.__repr__(), 'c   ')
    
    def test_finishedvial(self):
        v = Vial('aaaa')
        with self.assertRaises(ValueError):
            v.addColor('a')
    
    def test_wrongcolor(self):
        v = Vial('aaa ')
        with self.assertRaises(ValueError):
            v.addColor('b')
    
    def test_partialvial(self):
        v = Vial('aba ')
        v.addColor('a')
        self.assertEqual(v.__repr__(), 'abaa')

        v = Vial('a   ')
        v.addColor('a')
        self.assertEqual(v.__repr__(), 'aa  ')

class TestVialRemoveColor(unittest.TestCase):
    def test_emptyvial(self):
        v = Vial('    ')
        with self.assertRaises(ValueError):
            v.removeColor()
    
    def test_finishedvial(self):
        v = Vial('aaaa')
        v.removeColor()
        self.assertEqual(v.__repr__(), 'aaa ')
    
    def test_scrambledvial(self):
        v = Vial('abac')
        v.removeColor()
        self.assertEqual(v.__repr__(), 'aba ')
    
    def test_partialvial(self):
        v = Vial('acc ')
        v.removeColor()
        self.assertEqual(v.__repr__(), 'ac  ')

        v = Vial('a   ')
        v.removeColor()
        self.assertEqual(v.__repr__(), '    ')

class TestVialMetric(unittest.TestCase):
    def test_emptyvial(self):
        v = Vial('    ')
        self.assertEqual(v.metricValue(), 0)
    
    def test_finishedvial(self):
        v = Vial('aaaa')
        self.assertEqual(v.metricValue(), 3)
    
    def test_scrambledvial(self):
        v = Vial('abac')
        self.assertEqual(v.metricValue(), -3)
    
    def test_partialvial(self):
        v = Vial('acc ')
        self.assertEqual(v.metricValue(), 0)

        v = Vial('a   ')
        self.assertEqual(v.metricValue(), 0)

class TestVialEmpty(unittest.TestCase):
    def test_emptyvial(self):
        v = Vial('    ')
        self.assertTrue(v.isEmpty())
    
    def test_finishedvial(self):
        v = Vial('aaaa')
        self.assertFalse(v.isEmpty())
    
    def test_scrambledvial(self):
        v = Vial('abac')
        self.assertFalse(v.isEmpty())
    
    def test_partialvial(self):
        v = Vial('acc ')
        self.assertFalse(v.isEmpty())

        v = Vial('a   ')
        self.assertFalse(v.isEmpty())

if __name__ == '__main__':
    unittest.main()