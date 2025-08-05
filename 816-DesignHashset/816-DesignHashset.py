# Last updated: 8/5/2025, 2:56:58 PM
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = 2069
        self.bucket = []
        for _ in range(self.hash):
            self.bucket.append([])

    def add(self, key: int) -> None:
        hashed_key = key % self.hash
        bucket = self.bucket[hashed_key]
        item = next((item for item in bucket if item == key), None)
        if item is None:
            bucket.append(key)

    def remove(self, key: int) -> None:
        hashed_key = key % self.hash
        bucket = self.bucket[hashed_key]
        item = next((item for item in bucket if item == key), None)
        if item is not None:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashed_key = key % self.hash
        bucket = self.bucket[hashed_key]
        item = next((item for item in bucket if item == key), None)
        if item is not None:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)