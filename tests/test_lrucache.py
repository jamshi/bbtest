import unittest
from random import choice
from src.lrucache import lru_cache

class TestLRU(unittest.TestCase):

    def test_lru(self):
        def orig(x, y=0):
            return 3*x+y
        f = lru_cache(maxsize=20)(orig)
        hits, misses, maxsize, currsize = f.cache_info()
        self.assertEqual(maxsize, 20)
        self.assertEqual(currsize, 0)
        self.assertEqual(hits, 0)
        self.assertEqual(misses, 0)

        f = lru_cache(orig)
        domain = range(20)
        for i in range(1000):
            x, y = choice(domain), choice(domain)
            actual = f(x, y=y)
            expected = orig(x, y=y)
            self.assertEqual(actual, expected)
        hits, misses, maxsize, currsize = f.cache_info()
        self.assertTrue(hits < misses)
        self.assertEqual(hits + misses, 1000)
        self.assertEqual(currsize, 100)

    def test_lru_exception(self):
        with self.assertRaises(Exception):
            @lru_cache()
            def orig(x, y):
                return 3*x+y
            