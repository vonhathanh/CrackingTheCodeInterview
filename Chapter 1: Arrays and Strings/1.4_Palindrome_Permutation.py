"""
Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations:"taco cat'; "atco cta'; etc.)

SOLUTION:
Palindrome string has this properties: no more than one character that has the occurrence count is odd number in entire string
So we will just count the occurrence of every char in the string
"""


def get_char_number(char: chr) -> int:
    a = ord('a')
    z = ord('z')
    if a <= ord(char) <= z:
        return ord(char)
    return -1


def is_palindrome_permutation(string: str) -> bool:
    odd_count = 0
    letter = [0]*128
    for char in string:
        char_number = get_char_number(char)
        if char_number == -1:
            continue
        letter[char_number] += 1
        if letter[char_number] % 2 == 1:
            odd_count += 1
        else:
            odd_count -= 1

    return odd_count < 2


if __name__ == '__main__':
    assert is_palindrome_permutation("tact coa") == True
    assert is_palindrome_permutation("abba") == True
    assert is_palindrome_permutation("abcd1234") == False
    assert is_palindrome_permutation("hanh nat") == True
