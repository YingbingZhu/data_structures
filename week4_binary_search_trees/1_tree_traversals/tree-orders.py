# python3

import sys
import threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self, root, res):
    # self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if root == -1:
        return
    self.inOrder(self.left[root], res)
    res.append(self.key[root])
    self.inOrder(self.right[root], res)
    return res

  def preOrder(self, root, res):
    if root == -1:
        return
    res.append(self.key[root])
    self.preOrder(self.left[root], res)
    self.preOrder(self.right[root], res)
    return res

  def postOrder(self, root, res):
    if root == -1:
        return
    self.postOrder(self.left[root], res)
    self.postOrder(self.right[root], res)
    res.append(self.key[root])
    return res

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder(0, [])))
    print(" ".join(str(x) for x in tree.preOrder(0, [])))
    print(" ".join(str(x) for x in tree.postOrder(0, [])))


threading.Thread(target=main).start()
