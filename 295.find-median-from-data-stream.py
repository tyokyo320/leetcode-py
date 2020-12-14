#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lists = []
        

    def addNum(self, num: int) -> None:
        self.lists.append(num)
        

    def findMedian(self) -> float:
        self.lists.sort(reverse=False)
        length = len(self.lists)
        median = length // 2
        
        if not length:
            return 0.0
        if length % 2 == 0:
            return (self.lists[median] + self.lists[median - 1]) / 2
        else:
            return self.lists[median]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

