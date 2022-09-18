# python3



def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    swaps = []
    for i in range(len(data)//2, -1, -1):
        j = 2 * (i + 1) - 1
        while j < len(data):
            # find the smaller node
            if j < len(data) - 1 and data[j] > data[j+1]:
                j += 1
            if data[j] < data[i]:
                swaps.append((i, j))
                data[j], data[i] = data[i], data[j]
                i = j
                j = 2 * i + 1
            else:
                break
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
