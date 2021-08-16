#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

from typing import List

# @lc code=start


class Solution:

    def __init__(self) -> None:
        self.sum = 0

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import queue

        # init
        q = queue.PriorityQueue()
        m = len(heightMap)
        n = len(heightMap[0])
        cur_max = float('-inf')

        # 将四周边框放入优先队列
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    q.put((heightMap[i][j], i, j))
                    # visited
                    heightMap[i][j] = None

        while not q.empty():
            # 更新水位
            point = q.get()
            cur_max = max(point[0], cur_max)

            # BFS向4个方向遍历
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                x, y = point[1] + dx, point[2] + dy

                if x >= 0 and x < m and y >= 0 and y < n and heightMap[x][y] != None:
                    # 若发现比现在水位低的格子，求目前能装的水体积
                    if heightMap[x][y] < cur_max:
                        self.sum += (cur_max - heightMap[x][y])

                    # 没有的话，将新发现的格子放入优先队列，并继续探索
                    q.put((heightMap[x][y], x, y))
                    heightMap[x][y] = None

        return self.sum

# @lc code=end
