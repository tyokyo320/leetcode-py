
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




if __name__ == "__main__":
    s = SortAlgorithms()
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]

    # 插入排序
    # array = s.insertionSort(unsorted_array)

    # 选择排序
    # array = s.selectionSort(unsorted_array)

    # 冒泡排序
    array = s.bubbleSort(unsorted_array)
    print(array)
