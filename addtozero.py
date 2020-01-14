"""Given list of ints, return True if any two nums in list sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True

Given the wording of our problem, a zero in the list will always
make this true, since "any two numbers" could include that same
zero for both numbers, and they sum to zero:

    >>> add_to_zero([0, 1, 2])
    True
"""


def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.

    Initiate an empty dictionary to store the elements of the list 
    nums. This allows for faster lookup time than using lists or sets.

    Go through the list once. If the opposite of the number is not in 
    the dictionary, then add the number to the dictionary. If the 
    opposite IS in the dictionary, then there exist two numbers that 
    add to zero. 

    The naive solution:

        $ for x in list:
        $     for y in list:
        $         if x + y == 0:
        $             return True
        $ return False

    runs in O(n^2), while the solution below runs in O(n).
    """
    nums_dict = {}
    for num in nums:
        if num == 0 or -num in nums_dict:
            return True
        else:
            nums_dict[num] = None
    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n")
