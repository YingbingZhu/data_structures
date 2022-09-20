#!/usr/bin/python3

import sys
from math import inf
from threading import stack_size, Thread

sys.setrecursionlimit(10**7)  # max depth of recursion
stack_size(2 ** 25)  # new thread will get stack of such size


class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c


def IsBinarySearchTree(tree):
    stack = [(float('-inf'), tree[0], float('inf'))]
    while stack:
        min, node, max = stack.pop()
        if node.key < min or node.key >= max:
            return False
        if node.left != -1:
            stack.append((min, tree[node.left], node.key))
        if node.right != -1:
            stack.append((node.key, tree[node.right], max))
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        node = Node(a, b, c)
        tree.append(node)
    if nodes == 0 or IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


Thread(target=main).start()
