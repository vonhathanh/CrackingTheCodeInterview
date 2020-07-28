"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

SOLUTION: count the occurence of every unique character in input string
Continuously subtract the occurrence of every character we found in other string that exist in input string
"""


def is_one_away(s: str, t: str) -> bool:
    letters = [0]*128
    total_occur = len(s)
    for char in s:
        letters[ord(char)] += 1
    for char in t:
        if letters[ord(char)] > 0:
            letters[ord(char)] -= 1
            total_occur -= 1

    if abs(total_occur) == 1:
        return True

    return False


if __name__ == '__main__':
    assert is_one_away("pale", "ple") == True
    assert is_one_away("pales", "pale") == True
    assert is_one_away("pale", "bale") == True
    assert is_one_away("pale", "bake") == False