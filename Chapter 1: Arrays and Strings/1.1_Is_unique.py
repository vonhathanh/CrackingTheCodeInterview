"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures
"""


def is_unique(string: str) -> bool:
    """
    - Strategy 1: we will use a lookup array to count the occurrence of every character in the input string
    if any element in the array have value > 1, we can easily conclude that string is not unique
    Pros: O(n) time
    Cons: O(x) memory, when x is the number of possible characters that can appears in the string
    if the string use utf-8 encoding scheme, it will took us 2^16 bytes to store the occurrence
    Improvement: We could use a bit vector (bool array) instead of int array
    """
    counter = [0]*65536
    for char in string:
        counter[ord(char)] += 1
        if counter[ord(char)] > 1:
            return False
    return True


def is_unique_2(string: str) -> bool:
    """
    - Strategy 2:
    Use hash table to store and lookup for every character in the string
    Pro: O(n) time
    Cons: Use other additional data structures
    """
    lookup_table = {}
    for char in string:
        if char not in lookup_table:
            lookup_table[char] = 1
        else:
            return False
    return True


def is_unique_3(string: str) -> bool:
    """
    - Strategy 3:
    Sort the string using merge sort then check for duplicate
    Pro: Do not use other data structure
    Cons: O(n*Logn) runtime
    """
    pass


if __name__ == '__main__':
    # Test cases for strategy 1
    assert is_unique("abcd") == True
    assert is_unique("aa") == False
    assert is_unique("") == True
    assert is_unique("12345!@#$%") == True

    # Test cases for strategy 2
    assert is_unique_2("abcd") == True
    assert is_unique_2("aa") == False
    assert is_unique_2("") == True
    assert is_unique_2("12345!@#$%") == True