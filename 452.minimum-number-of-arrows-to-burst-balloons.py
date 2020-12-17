#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        # 对气球左边端点进行从小到大排序
        sort_point = sorted(points, key=lambda x: x[0])

        # 初始化弓箭手数量为1
        short_num = 1
        # 初始化区间，即第一个气球的两个端点
        # short_begin = sort_point[0][0]
        short_end = sort_point[0][1]

        for i in range(1, len(points)):
            # 在一个排好序的大区间内，要选择最小区间
            if sort_point[i][0] <= short_end:
                # short_begin = sort_point[i][0]
                
                if short_end > sort_point[i][1]:
                    short_end = sort_point[i][1]
            
            else:
                # 再保证当前气球被射穿的条件下，射击区间不能再更新了，需要再增加一个新的区间了
                short_num += 1
                # short_begin = sort_point[i][0]
                short_end = sort_point[i][1]
        
        return short_num

# @lc code=end

