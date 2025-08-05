# Last updated: 8/5/2025, 2:57:01 PM
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = 2069
        self.buckets = []
        for ele in range(self.hash):
            self.buckets.append([])
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self.buckets[key % self.hash]
        item = next((item for item in bucket if item[0] == key), None)
        if item is not None:
            item[1] = value
        else:
            bucket.append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = self.buckets[key % self.hash]
        item = next((item for item in bucket if item[0] == key), None)
        if item is not None:
            return item[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self.buckets[key % self.hash]
        item = next((item for item in bucket if item[0] == key), None)
        if item is not None:
            bucket.remove(item)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)