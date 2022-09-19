# python3

import sys
from collections import namedtuple
import random

Answer = namedtuple('answer_type', 'i j len')


def poly_hash(s, prime, x):
	hash_value = 0
	for i in range(len(s) - 1, -1, -1):
		hash_value = (hash_value * x + ord(s[i])) % prime
	return hash_value


def compute_table(s, plength, prime, x):
	H = [0] * (len(s) - plength + 1)
	last_value = poly_hash(s[len(s) - plength:], prime, x)

	H[len(s) - plength] = last_value

	y = pow(x, plength, prime)
	for i in range(len(s) - plength - 1, -1, -1):
		current_value = (x * H[i+1] + ord(s[i]) - y * ord(s[i + plength])) % prime
		H[i] = current_value
	return H


def compute_dict(s, plength, prime, x):
	D = {}
	last_value = poly_hash(s[len(s) - plength:], prime, x)

	D[last_value] = len(s) - plength

	y = pow(x, plength, prime)
	for i in range(len(s) - plength - 1, -1, -1):
		current_value = (x * last_value + ord(s[i]) - y * ord(s[i + plength])) % prime
		D[current_value] = i
		last_value = current_value
	return D


def search_substring(table, d):
	matches = {}
	find = False
	for i, v in enumerate(table):
		match = d.get(v, -1)
		if match != -1:
			matches[i] = match
			find = True
	return find, matches


def solve(s, t):
	max_length = 0
	i = 0
	j = 0
	low = 0
	high = min(len(s), len(t))
	m1 = 1000000007
	m2 = 1000000009
	x = random.randint(1, m2)
	while low <= high:
		mid = (low + high) // 2
		short, long = s, t
		if len(s) > len(t):
			short = t
			long = s
		d1 = compute_dict(short, mid, m1, x)
		d2 = compute_dict(short, mid, m2, x)
		t1 = compute_table(long, mid, m1, x)
		t2 = compute_table(long, mid, m2, x)
		find1, matches1 = search_substring(t1, d1)
		find2, matches2 = search_substring(t2, d2)
		if find1 and find2:
			for k, v in matches1.items():
				if matches2.get(k, -1) != -1:
					max_length = mid
					i, j = k, v
					low = mid + 1
		else:
			high = mid - 1
	return Answer(i, j, max_length)


if __name__ == '__main__':
	line = input()
	s, t = line.split()
	ans = solve(s, t)
	if len(s) <= len(t):
		print(ans.j, ans.i, ans.len)
	else:
		print(ans.i, ans.j, ans.len)
