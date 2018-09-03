# BetBright Take home test
# Candidate Name: Jamsheed BP


def find_anagrams(word, word_list):
    """Returns a list of anagrams from the word_list.
    Steps performed(Algorithm)
        1. Sort the word string alphabetically
        2. Filter the word_list matching the sorted element to the sorted word
    Args:
        word: The string whose anagrams has to be identified
        word_list: The list from which we have to check for anagrams of 'word'.
    Returns:
        list: A list of matching anagrams from word_list
    """

    _sorted = ''.join(sorted(word.lower().strip()))
    results = filter(lambda x: _sorted == ''.join(sorted(x.lower().strip())), word_list)
    return list(results)


