def count_characters(word):
    """
    Print a count of characters of a string

    :param word: string that must be counted
    :return list with each (key, value)
    e.g:
    >>> count_characters('wagner')
    [('a', 1), ('e', 1), ('g', 1), ('n', 1), ('r', 1), ('w', 1)]

    >>> count_characters('banana')
    [('a', 3), ('b', 1), ('n', 2)]
    """

    ordered_characters = sorted(set(word))
    result = [(characters, word.count(characters)) for characters in ordered_characters]
    return result


print(count_characters('banana'))
print()
print(count_characters('wagner'))
print()
print(count_characters('abacate'))
