# Last updated: 8/5/2025, 2:56:51 PM
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.queue = [''] * self.k
        self.isQueueEmpty = True
        self.isQueueFull = False
        self.elements = 0
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isQueueFull:
            return False
        else:
            if self.tail == self.k - 1:
                self.tail = 0
            else:
                self.tail += 1
            self.queue[self.tail] = value
            self.elements += 1
            if self.elements == self.k:
                self.isQueueFull = True
                self.isQueueEmpty = False
            elif self.elements == 0:
                self.isQueueFull = False
                self.isQueueEmpty = True
            else:
                self.isQueueFull = False
                self.isQueueEmpty = False
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isQueueEmpty:
            return False
        else:
            self.queue[self.head] = ''
            self.head += 1
            self.elements -= 1
            if self.elements == self.k:
                self.isQueueFull = True
                self.isQueueEmpty = False
            elif self.elements == 0:
                self.isQueueFull = False
                self.isQueueEmpty = True
            else:
                self.isQueueFull = False
                self.isQueueEmpty = False
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isQueueEmpty:
            return -1
        else:
            return self.queue[self.head]



    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isQueueEmpty:
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.isQueueEmpty

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.isQueueFull
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()