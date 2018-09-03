import unittest
from src.anagram import find_anagrams
from itertools import permutations
from random import shuffle

class TestAnagramFinder(unittest.TestCase):

    def test_simple(self):
        word_list = ['oof', 'ofo', 'Foo', 'fofo', 'foobar']
        anagrams = find_anagrams('foo', word_list)
        self.assertEqual(3, len(anagrams))

    def test_mixed(self):
        _goal_perms = [''.join(p) for p in permutations('goal')]
        _dog_perms = [''.join(p) for p in permutations('dog')]
        word_list = _goal_perms + _dog_perms
        shuffle(word_list)
        anagrams = find_anagrams('goal', word_list)
        self.assertEqual(len(_goal_perms), len(anagrams))
