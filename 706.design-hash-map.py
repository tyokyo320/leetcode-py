#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashmap[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.hashmap.keys():
            return -1
        else:
            return self.hashmap[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key not in self.hashmap.keys():
            return None
        else:
            del self.hashmap[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

