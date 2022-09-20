#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c


def IsBinarySearchTree(tree, n):
    """
    for any node of the tree, if its key is 𝑥, left subtree its key must be strictly less than 𝑥,
    right subtree its key must be strictly greater
    :param tree:
    :return:
    """
    # Implement correct algorithm here
    res = InOrder(tree)
    for i in range(1, n):
        if res[i] <= res[i-1]:
            return False
    return True


def InOrder(tree):
    res = []
    curr = 0
    stack = [tree[0]]
    while stack:
        # traverse to leftmost
        if curr != -1:
            stack.append(tree[curr])
            curr = tree[curr].left
        else:
            root = stack.pop()
            res.append(root.key)
            curr = root.right
    return res


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        node = Node(a, b, c)
        tree.append(node)
    if nodes == 0 or IsBinarySearchTree(tree, nodes):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
