# python3.6 实现二分查找

import numpy as np

def BinarySearch(nums, index):
    """
    使用二分法查找
    Input:
        nums: 输入的顺序 list
        index: 需要查找的位置索引
    Output:
        mums[index]: 查找的元素
    """

    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end)//2
        #print(mid)
        if mid > index:
            end = mid - 1
        elif mid < index:
            start = mid + 1
        else:
            return nums[mid]
    return -1

# 程序还可以优化，添加一条判断顺序的, 进行排序
if __name__ == "__main__":
    nums = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    tmp = BinarySearch(nums, 3)
    print(tmp)

    nums1 = [50, 32, 30, 28, 13, 11, 5, 3]
    tmp1 = BinarySearch(nums1, 3)
    print(tmp1)
