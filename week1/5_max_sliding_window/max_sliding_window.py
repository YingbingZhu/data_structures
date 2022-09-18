# python3
from collections import deque


def max_sliding_window_naive(sequence, m):
    maximums = []
    # for i in range(len(sequence) - m + 1):
    #     maximums.append(max(sequence[i:i + m]))
    d = deque()
    for i, v in enumerate(sequence):
        # if d is not empty and the current max is smaller then new value, pop
        while d and sequence[d[-1]] < v:
            d.pop()
        d.append(i)
        if d[0] == i - m:
            d.popleft()
        if i >= m - 1:
            maximums.append(sequence[d[0]])
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

