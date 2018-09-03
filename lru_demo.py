from __future__ import print_function
from src.lrucache import lru_cache

@lru_cache
def _sum(a, b):
    return a+b

@lru_cache(maxsize=3)
def _thrice(a):
    return 3*a

if __name__ == '__main__':
    # Cache demonstration
    # Run 'python lru_demo.py' to see the working
    print('>>>>>Function _sum :: Cache Size (default 100)')
    _sum(2, 3)
    _sum(7, 3)
    _sum(2, 3)
    _sum(0, 3)
    print(_sum.cache_info())
    print('Cached Data')
    print(_sum.cache)

    print('>>>>>Function _thrice :: Cache Size 3')
    _thrice(2)
    _thrice(7)
    _thrice(5)
    _thrice(2)
    _thrice(8)
    _thrice(7)
    print(_thrice.cache_info())
    print('Cached Data')
    print(_thrice.cache)