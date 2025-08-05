# Last updated: 8/5/2025, 2:54:50 PM
class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        # self.array = [0] * length
        self.array = dict()
        self.snap_ids_dict = dict()
        self.count = 0

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.snap_ids_dict[self.count] = dict(self.array.items())
        self.count += 1
        return self.count - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.snap_ids_dict:
            snap_id_arr = self.snap_ids_dict[snap_id]
            if index in snap_id_arr:
                return snap_id_arr[index]
            else:
                return 0
        else:
            return 0



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)