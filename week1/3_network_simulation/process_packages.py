# python3

from collections import namedtuple
from queue import Queue

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = Queue(maxsize=size)

    def process(self, request):
        finish_time = self.finish_time
        process_time = request.time_to_process
        arrive_time = request.arrived_at
        # pop already finish
        while not finish_time.empty():
            if finish_time.queue[0] <= arrive_time:
                finish_time.get()
            else:
                break

        if finish_time.empty():
            finish_time.put(arrive_time + process_time)
            return Response(False, arrive_time)

        if finish_time.full():
            return Response(True, -1)

        else:
            finish_time.put(finish_time.queue[-1] + process_time)
            return Response(False, finish_time.queue[-1] + process_time - arrive_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
