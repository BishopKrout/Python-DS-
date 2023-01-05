def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # for num in lst:
    #     if num in lst:
    #         print(lst[-1])
    #     else:
    #         print (None)

    if lst:
        return lst[-1]

 