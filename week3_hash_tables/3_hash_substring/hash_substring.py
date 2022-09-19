# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans


def precompute_hashes(text, plength, prime, x):
    H = [0] * (len(text) - plength + 1)
    s = text[-plength:]
    H[len(text) - plength] = poly_hash(s, prime, x)
    # y = 1
    # # for _ in range(1, plength + 1):
    # #     y = (y * x) % prime
    y = pow(x, plength, prime)
    for i in reversed(range(len(text) - plength)):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + plength])) % prime
        # while (prehash < 0):
        #     prehash += prime
    return H


def get_occurrences(pattern, text):
    prime = 1000000007
    x = random.randint(1, prime)
    plength = len(pattern)
    phash = poly_hash(pattern, prime, x)
    H = precompute_hashes(text, plength, prime, x)
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if phash == H[i] and text[i:i + len(pattern)] == pattern
    ]


def get_occurrences_naive(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
    # precompute_hashes(text, 3, "aab", )
    # print(hash("Test"))
    # print(hash("tTes") - (hash("t")) + (hash("t")))
    # print(hash("testTesttesT"))
