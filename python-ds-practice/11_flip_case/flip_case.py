def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

        to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out


    # upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # lower = 'abcdefghijklmnopqrstuvwxyz'
    # if to_swap == upper:
    #     phrase.replace(to_swap).lower()
    #     return phrase
    # if to_swap == lower:
    #     phrase.replace(to_swap).upper()
    #     return phrase
   

