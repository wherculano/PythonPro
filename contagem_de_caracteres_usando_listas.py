def count_characters(word):
    '''
    Print a count of characters of a string

    :param word: string that must be counted

    e.g:
    >>> count_characters('wagner')
    a: 1
    e: 1
    g: 1
    n: 1
    r: 1
    w: 1
    >>> count_characters('banana')
    a: 3
    b: 1
    n: 2
    '''

    ordered_characters = sorted(word)
    previous_characters = ordered_characters[0]
    count = 1
    for character in ordered_characters[1:]:
        if character == previous_characters:
            count += 1
        else:
            print(f'{previous_characters}: {count}')
            count = 1
            previous_characters = character
    print(f'{previous_characters}: {count}')


if __name__ == '__main__':
    count_characters('wagner')
    print()
    count_characters('banana')
