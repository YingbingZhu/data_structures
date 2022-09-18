# python3

import sys
import threading
from collections import deque


class Node:
    def __init__(self):
        self.parent = None
        self.children = []


def compute_height(n, parents):
    """
    :param n:
    :param parents:
    :return:
    """
    tree, root_index = construct_tree(n, parents)
    max_height = 1
    # create a queue with
    q = deque([tree[root_index]])

    while len(q)>0:
        node = q.popleft()
        if node.children:
            max_height += 1
        for child in node.children:
            q.append(tree[child])

    return max_height

    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height


def construct_tree(n, parents):
    """
    construct a tree
    :param n:
    :param parents:
    :return: tree list and root
    """
    # create a tree with n nodes
    tree = [Node() for _ in range(n)]
    root = None
    # add parents
    for i in range(n):
        tree[i].parent = parents[i]
        tree[parents[i]].children.append(i)
        if parents[i] == -1:
            root = i

    return tree, root


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()

