# python3

def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash(s):
    """
    compute hash value of a string
    :param s:
    :return:
    """
    res = 0
    sL = [ord(c) - ord('A') for c in s]
    for i in sL:
        res += 26 * res + i
    return res


def get_occurrences(pattern, text):
    m = len(pattern)
    n = len(text)
    p_hash = hash(pattern)
    s_hash = hash(text[:m])
    res = []
    i = m - 1
    while i < n:
        if p_hash == s_hash:
            res.append(i - m + 1)
        i += 1
        if i <= n - 1:
            s_hash -= hash(text[i - m]) * (26 ** (m-1))
            s_hash = s_hash * 26 + hash(text[i])
    return res



def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
    # print(hash("Test"))
    # print(hash("tTes") - (hash("t")) + (hash("t")))
    # print(hash("testTesttesT"))

