#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n):
        # 初始化
        location = [["."] * n for i in range(n)]
        mark = [[0] * n for i in range(n)]
        result = []

        self.generate(0, n, location, result, mark)
        return result

    def generate(self, k, n, location, result, mark):
        # k代表完成了几个皇后的放置，所有皇后完成放置后，将记录皇后位置location放入result中
        if k == n:
            result.append(list(location[0]))
            return
        
        # 按顺序尝试第0至第n-1列
        for i in range(n):
            # 如果可以放皇后
            if mark[k][i] == 0:
                # 备份回溯前mark棋盘
                temp_mark = mark
                location[k][i] = "Q"
                # print(location)
                self.put_down_the_queen(k, i, mark)

                # 递归下一行皇后放置
                self.generate(k + 1, n, location, result, mark)

                # 将mark重新赋值为回溯前状态
                mark = temp_mark
                location[k][i] = "."
                # print(location)
    
    def put_down_the_queen(self, x, y, mark):
        # 方向list
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]
        
        # (x, y)放置皇后，标记
        mark[x][y] = 1
        for i in range(1, len(mark)):
            # 8个方向
            for j in range(8):
                new_x = x + i * dx[j]
                new_y = y + i * dy[j]
                
                # 检查新位置是否还在棋盘内
                if (new_x >= 0) and (new_x < len(mark)) and (new_y >= 0) and (new_y < len(mark)):
                    mark[new_x][new_y] = 1

if __name__ == "__main__":
    s = Solution()
    result = s.solveNQueens(2)
    print(result)
# @lc code=end


