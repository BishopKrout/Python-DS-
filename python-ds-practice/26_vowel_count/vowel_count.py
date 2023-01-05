def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    frequency_map = {}
    for ltr in phrase:
        ltr = ltr.lower()
        if ltr in vowels:
            if ltr in frequency_map:
                frequency_map[ltr] += 1
            else:
                frequency_map[ltr] = 1
    print (frequency_map)


    # phrase = phrase.lower()
    # counter = {}

    # for ltr in phrase:
    #     if ltr in VOWELS:
    #         counter[ltr] = counter.get(ltr, 0) + 1

    # return counter