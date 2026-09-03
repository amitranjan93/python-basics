# Heap and Priority Queue
# left child  = 2*i + 1
# right child = 2*i + 2
# parent      = (i - 1) // 2
import heapq

# tasks = [
#     (3, "Update documentation"),
#     (1, "Server is down"),
#     (2, "Fix database bug"),
#     (4, "Send email")
# ]

# heapq.heapify(tasks)

# while(tasks):
#       print(heapq.heappop(tasks))

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def push(self, priority, data):
        heapq.heappush(self.heap, (priority, self.counter, data))
        self.counter += 1

    def pop(self):
        priority, counter, data = heapq.heappop(self.heap)
        return data

pq = PriorityQueue()

pq.push(3, "Update documentation")
pq.push(1, "Server down")
pq.push(2, "Fix database")
pq.push(1, "Network down")

print(pq.pop())
print(pq.pop())
print(pq.pop())
print(pq.pop())