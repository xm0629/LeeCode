# Python3.6 实现移除元素

import numpy as np


class RemoveElement(object):
    def __init__(self, nums, value):
        self.nums = nums


    def removeElement(self):
        nums = self.nums
        value = self.value

        length = len(nums)
        for i in range(length-1, -1, -1):
            if nums[i] == value:
                nums.pop(i)
        return nums


class RemoveElement2(object):
    def __init__(self, nums, index):
        self.nums = nums
        self.index = index

    def removeElement1(self):
        nums = self.nums
        index = self.index

        length = len(nums)

        if index > length:
            return nums
        elif index < 0:
            return nums
        else:
            nums.pop(index)
            return nums


#if __name__ == '__main__':
#    nums = list([3,2,2,3])
#    value = 3
#
#    tmp =  RemoveElement(nums,value)
#    new_list = test.removeElement()
#    print(new_list)

if __name__ == "__main__":
    nums =  nums = [3,2,2,3]
    index = 2
    test = RemoveElement2(nums,index)
    new_list = test.removeElement1()
    print(new_list)

