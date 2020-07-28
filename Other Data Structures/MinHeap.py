class MinHeap:
    def __init__(self, max_size: int):
        self.heap = [-1]
        self.max_size = max_size
        self.size = 0

    FRONT = 1

    @staticmethod
    def parent(pos: int) -> int:
        return pos // 2

    @staticmethod
    def left_child(pos: int) -> int:
        return pos * 2

    @staticmethod
    def right_child(pos) -> int:
        return pos * 2 + 1

    def is_leaf(self, pos: int) -> bool:
        return self.size // 2 <= pos <= self.max_size

    def swap(self, fpos: int, spos: int):
        tmp = self.heap[fpos]
        self.heap[fpos] = self.heap[spos]
        self.heap[spos] = tmp

    def heapify(self, pos: int):
        # print(pos)
        if not self.is_leaf(pos):
            if self.heap[pos] > self.heap[MinHeap.left_child(pos)] or \
                    self.heap[pos] > self.heap[MinHeap.right_child(pos)]:
                print(f'heap pos: {self.heap[pos]}, left child: {self.heap[MinHeap.left_child(pos)]}, right child: {self.heap[MinHeap.right_child(pos)]}')
                if self.heap[MinHeap.left_child(pos) < self.heap[MinHeap.right_child(pos)]]:
                    self.swap(pos, MinHeap.left_child(pos))
                    self.heapify(MinHeap.left_child(pos))
                else:
                    self.swap(pos, MinHeap.right_child(pos))
                    self.heapify(MinHeap.right_child(pos))

    def insert(self, value: int):
        if self.size > self.max_size:
            return

        self.heap.append(value)
        self.size += 1
        current = self.size

        while self.heap[current] < self.heap[MinHeap.parent(current)]:
            self.swap(current, MinHeap.parent(current))
            current = MinHeap.parent(current)

    def print(self):
        for i in range(1, self.size // 2 + 1):
            print(f'Parent: {self.heap[i]}, Left child: {self.heap[i * 2]}, Right child: {self.heap[i * 2 + 1]}')

    def build(self):
        for i in range(self.size // 2, 0, -1):
            self.heapify(i)

    def remove(self) -> int:
        popped = self.heap[MinHeap.FRONT]
        self.heap[MinHeap.FRONT] = self.heap[self.size]
        self.size -= 1
        self.heapify(MinHeap.FRONT)
        return popped


if __name__ == '__main__':
    min_heap = MinHeap(max_size=100)

    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(17)
    min_heap.insert(10)
    min_heap.insert(84)
    min_heap.insert(19)
    min_heap.insert(6)
    min_heap.insert(22)
    min_heap.insert(9)

    min_heap.build()

    min_heap.print()

    print(min_heap.remove())

    min_heap.print()