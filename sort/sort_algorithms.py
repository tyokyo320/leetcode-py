
class SortAlgorithms():

    def insertionSort(self, array):
        for i in range(1, len(array)):
            # 选未排序的第一个值 value
            value = array[i]
            # 从 value 的前一个位置开始比较
            position = i - 1

            # 若 value 比前一个位置的值小
            while position >= 0 and array[position] > value:
                # 用前一个元素覆盖当前元素
                array[position + 1] = array[position]
                position -= 1

            # 循环结束后，将 value 插入到相应位置
            array[position + 1] = value
        return array

    def selectionSort(self, array):
        # 最后一轮不需要遍历，已经有顺序了
        for i in range(len(array) - 1):
            min_index = i
            # 循环查找最小值
            for j in range(i + 1, len(array)):
                if array[min_index] > array[j]:
                    min_index = j
            # 交换
            array[min_index], array[i] = array[i], array[min_index]

        return array

    def bubbleSort(self, array):
        for i in range(len(array) - 1):
            # 以后每次循环的次数为arr.length-1-i
            for j in range(len(array) - i - 1):
                # 相邻两个元素作比较，如果前面元素大于后面，进行交换
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

        return array

    def heapify(self, array, n, index):
        '''
        heapify 堆调整为大堆顶，即将最大值放在根结点
        n 堆的大小
        i 子树根的索引
        '''
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # 找出两个子节点中的最大值
        # 若左子树存在且比根节点大
        if left < n and array[largest] < array[left]:
            largest = left

        # 若右子树存在且比根节点大
        if right < n and array[largest] < array[right]:
            largest = right

        # 如果找出的最大值不是当前父节点所对应的值, 那么将父节点和最大值所对应的下标交换
        if largest != index:
            array[index], array[largest] = array[largest], array[index]

            # 递归调用一次是确保置换后, 子树的子树能满足大顶堆的要求, 所以又把当前子树作为父节点, 重新调用heapify, 确保子树的子树经过置换后依然满足要求
            # 这么一层一层迭代下去, 每置换一次就往下迭代一次
            self.heapify(array, n, largest)

    def heapSort(self, array):
        n = len(array)

        # 创建最大堆
        for i in range(n//2 - 1, -1, -1):
            self.heapify(array, n, i)

        # 一对一的将元素从堆中删除
        for i in range(n-1, 0, -1):
            # 交换现在的根节点至最后
            array[i], array[0] = array[0], array[i]

            # 重新创建最大堆，确保array[0]是[0, i]中的最大值
            # 注意这里一定要将顶堆限制在[0, i]的范围内，否则刚抽取出的最大值又被放到最大堆的起始了！
            self.heapify(array, i, 0)

        return array

    def partition(self, array, low, high):
        '''
        方法1：pivot：low

        pivot = array[low];
        while low < high:
            while low < high and array[high] > pivot:
                high -= 1

            # 交换比基准大的记录到左端
            array[low] = array[high]

            while low < high and array[low] < pivot:
                low += 1

            # 交换比基准小的记录到右端
            array[high] = array[low]

        # 扫描完成，基准到位
        array[low] = pivot
        # 返回的是基准的位置
        return low
        '''

        '''
        方法2：pivot：high


        i = low - 1
        pivot = array[high]

        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
        '''

        '''
        方法3：pivot：high

        '''
        i = low
        j = high - 1

        pivot = array[high]

        while i < j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]

        array[i], array[high] = array[high], array[i]
        return i

    def quickSort(self, array, low, high):
        if low < high:
            mid = self.partition(array, low, high)
            self.quickSort(array, low, mid-1)
            self.quickSort(array, mid+1, high)

        return array

    def merge(self, array, l, m, r):
        # the size of L[]
        n1 = m - l + 1
        # the size of R[]
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(0, n1):
            L[i] = array[l + i]
        for j in range(0, n2):
            R[j] = array[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            array[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            array[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, array, l, r):
        if l < r:
            mid = int(l + (r - l) / 2)
            self.mergeSort(array, l, mid)
            self.mergeSort(array, mid+1, r)
            self.merge(array, l, mid, r)

        return array

    def countingSort(self, array):
        # 获取最大，最小值
        largest = max(array)
        smallest = min(array)
        # 用于统计个数的空数组，初始化为0
        counter = [0 for i in range(largest - smallest + 1)]
        # 桶内索引值
        index = 0

        # 统计每个元素出现的次数
        for i in range(len(array)):
            counter[array[i] - smallest] += 1
        for j in range(len(counter)):
            while counter[j] > 0:
                # 取出元素
                array[index] = j + smallest
                index += 1
                counter[j] -= 1
        return array


if __name__ == "__main__":
    s = SortAlgorithms()
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]

    # 插入排序
    # array = s.insertionSort(unsorted_array)

    # 选择排序
    # array = s.selectionSort(unsorted_array)

    # 冒泡排序
    # array = s.bubbleSort(unsorted_array)

    # 堆排序
    # array = s.heapSort(unsorted_array)

    # 快速排序
    # array = s.quickSort(unsorted_array, 0, len(unsorted_array) - 1)

    # 归并排序
    # array = s.mergeSort(unsorted_array, 0, len(unsorted_array) - 1)

    # 计数排序
    array = s.countingSort(unsorted_array)
    print(array)
