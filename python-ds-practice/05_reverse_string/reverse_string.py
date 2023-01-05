def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    r_phrase = phrase[::-1]
    for letter in r_phrase:
        print (letter)

    # return phrase[::-1]

