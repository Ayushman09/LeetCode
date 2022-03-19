#Priority queue based solution
class PQItem(NamedTuple):
    frequency: int
    index: int
    number: int

class FreqStack:
    def __init__(self):
        self.counter = dict()
        self.index = 0
        self.heap = []

    def push(self, val: int) -> None:
        if val in self.counter:
            self.counter[val] += 1
        else:
            self.counter[val] = 1

        self.index += 1
        heapq.heappush(self.heap, PQItem(-self.counter[val], -self.index, val))
        

    def pop(self) -> int:
        pq_item = heapq.heappop(self.heap)

        self.counter[pq_item.number] -= 1
		
		# POP TO RELEASE MEMORY
        if self.counter[pq_item.number] == 0:
            self.counter.pop(pq_item.number)

        return pq_item.number