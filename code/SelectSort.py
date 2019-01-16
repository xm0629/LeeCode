# Python3.6 实现选择排序

import numpy as np

def SelectSort(nums):
    """
    nums 数组实现选择排序
    Input:
        nums: 输入需要排序的数组
    Output:
        sortnums: 排序之后的数组
    """

    for i in range(len(nums)-1):
        index = i
        for j in range(i+1, len(nums)):
            if nums[index] > nums[j]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    return nums



if __name__ == "__main__":
    nums = [54,26,93,17,77,31,44,55,20]
    tmp = SelectSort(nums)
    print(tmp)
