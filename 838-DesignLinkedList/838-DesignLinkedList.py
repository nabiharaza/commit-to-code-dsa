# Last updated: 8/5/2025, 2:56:52 PM
class Node:
    """

    """

    def __init__(self, data=None):
        """

        :param data:
        """
        self.data = data
        self.next = None
class MyLinkedList:
    """

    """

    def __init__(self):
        """

        """
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head is None:
            return -1
        else:
            current = self.head
            index -= 1
            val = current.data
            if index == -1:
                return val
            while current.next is not None:
                current = current.next
                index -= 1
                if index == -1:
                    return current.data
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        current = Node(val)
        if self.head is None:
            self.head = current
        else:
            current.next = self.head
            self.head = current

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)
        if self.head is None and index == 0:
            self.head = node
        if index == 0:
            node.next = self.head
            self.head = node
        elif self.head is not None:
            current = self.head
            while index != 1 and current.next is not None:
                current = current.next
                index -= 1
            if index == 1:
                node.next = current.next
                current.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head is not None and index == 0:
            self.head = self.head.next
        elif self.head is not None:
            current = self.head
            previous = None
            while index != 0 and current.next is not None:
                previous = current
                current = current.next
                index -= 1
            if index == 0:
                previous.next = current.next
                current.next = None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)