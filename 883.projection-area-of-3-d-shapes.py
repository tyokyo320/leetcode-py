#
# @lc app=leetcode id=883 lang=python3
#
# [883] Projection Area of 3D Shapes
#

# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        '''
        对于x方向，求每个x方向的最大值的和，就是x方向的表面积
        对于y方向，求每个y方向的最大值的和，就是y方向的表面积
        剩下的顶面，即为非零元素的数目

        front, left, top = 0, 0, 0

        # 以x方向为前面
        for xs in grid:
            front += max(xs)
        print(front)
        
        # 以y方向为左侧面
        for i in range(0, len(grid)):
            ys = []
            for j in range(0, len(grid)):
                ys.append(grid[j][i])
                print(ys)
            left += max(ys)
        print(left)
        
        # 顶面
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] == 0:
                    top += 0
                else:
                    top += 1
        print(top)

        return front + left + top
        '''

        '''
        优化写法：
        对于y方向的求解，使用zip(*)
        '''
        
        # x方向
        front = sum(map(max, grid))

        # y方向
        left = sum(map(max, zip(*grid)))

        # z方向
        top = sum(v > 0 for row in grid for v in row)

        return front + left + top


        
# @lc code=end

