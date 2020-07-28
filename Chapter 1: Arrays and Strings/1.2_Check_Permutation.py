"""
Given two strings, write a method to decide if one is a permutation of the
other
Example cases: aabb: abab, bbaa, baab, baba
- Strategy 1: sort two strings and compare: O(nLogn) runtime
- Strategy 2: Count the occurrence of each character in two strings and compare them
O(n) runtime
"""


def is_string_permutation(s: str, t: str) -> bool:
    letters = [0] * 128

    for char in s:
        letters[ord(char)] += 1

    for char in t:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False
    return True


def is_string_permutation_2(s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(t)

    return s == t


if __name__ == '__main__':
    assert is_string_permutation("aabb", "abab") == True
    assert is_string_permutation("aabb", "aabb") == True
    assert is_string_permutation("123123", "aa12312312") == False

    assert is_string_permutation_2("aabb", "abab") == True
    assert is_string_permutation_2("aabb", "aabb") == True
    assert is_string_permutation_2("123123", "aa12312312") == False