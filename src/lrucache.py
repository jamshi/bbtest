# BetBright Take home test
# Candidate Name: Jamsheed BP

""" 2. Least recently used cache """

from collections import OrderedDict, namedtuple
from functools import wraps

_CacheInfo = namedtuple("CacheInfo", "hits misses maxsize currsize")

def lru_cache(*args, **kwargs):
    """Least-recently-used cache decorator.
    Cache storage is OrderedDict, 
    The args and kwargs must be hashable for the key to dict.

    eg usage:

        @lru_cache(maxsize=100)
        def sum2(a, b):
            ...

        @lru_cache
        def sum2(a, b):
            ...

    """

    cache = OrderedDict()
    hits, misses = [0], [0]
    _func = None
    maxsize = 100

    # Check func is frst argument
    # To see if called like @lru_cache
    if len(args) > 0 and callable(args[0]):
        _func = args[0]

    if _func is None:
        if 'maxsize' not in kwargs:
            raise Exception('maxsize attribute not provided')
        maxsize = kwargs['maxsize']

    def _callable(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args
            if kwargs:
                key += tuple(kwargs.items())

            # On Cache Hit
            if key in cache:
                result = cache[key]
                cache.pop(key)
                cache[key] = result    # Re-insert the result to cache so as to position last
                hits[0] += 1
                return result

            # On Cache Miss
            result = func(*args, **kwargs)
            misses[0] += 1
            cache[key] = result 
            if len(cache) > maxsize:
                cache.popitem(0)    # pop out least recently used cache entry on max-size
            return result

        wrapper.cache_info = cache_info
        wrapper.cache = cache
        return wrapper
    
    def cache_info():
        """Report cache statistics"""
        return _CacheInfo(hits[0], misses[0], maxsize, len(cache))

    if _func is None:
        return _callable
    else:
        return _callable(_func)


