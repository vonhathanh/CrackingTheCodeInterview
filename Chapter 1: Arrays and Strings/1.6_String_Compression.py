"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed"string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z)
"""


def compress_ver1(string: str) -> str:
    if len(string) <= 1:
        return string

    new_str = string[0]
    duplicate_count = 1

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            duplicate_count += 1
        else:
            new_str += str(duplicate_count) + string[i]
            duplicate_count = 1

    new_str += str(duplicate_count)

    if len(new_str) >= len(string):
        return string

    return new_str


def compress_ver2(string: str) -> str:
    if len(string) <= 1:
        return string

    new_str = [''] * len(string) * 2
    new_str[0] = string[0]
    duplicate_count = 1
    cur_index = 1

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            duplicate_count += 1
        else:
            new_str[cur_index] = str(duplicate_count)
            new_str[cur_index+1] = string[i]
            cur_index += 2
            duplicate_count = 1

    new_str[cur_index] = str(duplicate_count)
    new_str = ''.join(new_str)

    if len(new_str) >= len(string):
        return string

    return new_str


if __name__ == '__main__':
    print("Compress ver 1")
    print(compress_ver1("aabcccccaaa"))
    print(compress_ver1(""))
    print(compress_ver1("aaaaaaa"))
    print(compress_ver1("abcdef"))

    print("Compress ver 2")
    print(compress_ver2("aabcccccaaa"))
    print(compress_ver2(""))
    print(compress_ver2("aaaaaaa"))
    print(compress_ver2("abcdef"))

