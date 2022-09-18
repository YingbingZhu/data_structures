# python3
import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def leftChild(i, size):
    l = 2 * i + 1
    return l if l < size else -1


def rightChild(i, size):
    r = 2 * i + 2
    return r if r < size else -1


def compare(minHeap, i, j, size):
    if j >= size or j < 0:
        return False
    if i >= size or i < 0:
        return False
    if minHeap[i].started_at < minHeap[j].started_at:
        return True
    elif minHeap[i].started_at == minHeap[j].started_at and minHeap[i].worker < minHeap[j].worker:
        return True

    return False


def siftDown(minHeap, i, size):
    if i >= size:
        return
    indexMin = i
    if compare(minHeap, leftChild(i, size), indexMin, size):
        indexMin = leftChild(i, size)

    if compare(minHeap, rightChild(i, size), indexMin, size):
        indexMin = rightChild(i, size)

    if indexMin != i:
        minHeap[i], minHeap[indexMin] = minHeap[indexMin], minHeap[i]
        siftDown(minHeap, indexMin, size)


def assign_jobs(n_workers, jobs):
    result = []
    # next_free_time = [0] * n_workers
    # for job in jobs:
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job
    workers = [AssignedJob(_, 0) for _ in range(n_workers)]
    for job in jobs:
        result.append(AssignedJob(workers[0].worker, workers[0].started_at))
        workers[0] = AssignedJob(workers[0].worker, workers[0].started_at + job)

        siftDown(workers, 0, n_workers)


    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
