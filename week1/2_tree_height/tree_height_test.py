import unittest


from tree_height import compute_height


class MyTestCase(unittest.TestCase):

    def test_tree_height(self):
        i = 1
        with open('tests/{:02d}'.format(i), 'r') as f:
            all_lines = f.readlines()
            n = int(all_lines[0])
            parents = list(map(int, all_lines[1].split(" ")))
            f.close()
        with open('tests/{:02d}.a'.format(i), 'r') as f:
            ans = int(f.read())
            f.close()
        output = compute_height(n, parents)
        self.assertEqual(output, ans)  # add assertion here


if __name__ == '__main__':
    unittest.main()
