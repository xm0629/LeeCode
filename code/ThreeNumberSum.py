# python3.6 实现 三个元素 a + b + c = 0

import numpy as np

class ThreeNumberSum(object):
    """
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    Input:
        nums: 输入的数组
    Output:
        res_list: 输出满足 a + b + c = 0 条件的三元组
    """
    def __init__(self, nums):
        self.nums = nums

    def threeSum(self):
        nums = self.nums

        res_list = [] 
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    res_list.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res_list


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    tmp = ThreeNumberSum(nums)
    res_list = tmp.threeSum()
    print(res_list)
    tmp.threeSum()
