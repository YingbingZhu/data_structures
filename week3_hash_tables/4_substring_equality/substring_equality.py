# python3
import random
import sys

m1 = 10 ** 9 + 7
m2 = 10 ** 9 + 9


class Solver:
    def __init__(self, s):
        self.s = s

    def precompute_hashtable(self, s, prime, x):
        n = len(s) + 1
        H = [0] * n
        for i in range(1, n):
            H[i] = (x * H[i-1] + ord(s[i - 1])) % prime
        return H

    def hash_value(self, table, prime, x, start, l):
        # y = pow(x, length) % prime
        y = pow(x, l, prime)
        res = (table[start + l] - y * table[start]) % prime
        return res

    def ask(self, table1, table2, x, a, b, l):
        hash_a1 = self.hash_value(table1, m1, x, a, l)
        hash_a2 = self.hash_value(table2, m2, x, a, l)
        hash_b1 = self.hash_value(table1, m1, x, b, l)
        hash_b2 = self.hash_value(table2, m2, x, b, l)
        if hash_a1 == hash_b1 and hash_a2 == hash_b2:
            return True
        else:
            return False


if __name__ == '__main__':
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)
    x = random.randint(1, m2)
    table1 = solver.precompute_hashtable(s, m1, x)
    table2 = solver.precompute_hashtable(s, m2, x)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(table1, table2, x, a, b, l) else "No")
