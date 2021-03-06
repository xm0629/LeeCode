# python3.6 实现两数之和 LeeCode

class TwoSum(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target
        
    def twosum1(self):
        nums = self.nums
        target = self.target
        
        n = len(nums)
        for x in range(n):
            for y in range(x+1,n):
                if nums[x] == target - nums[y]:
                    return x,y
                    break
                else:
                    continue
    def twosum2(self):
        nums = self.nums
        target = self.target
        
        n = len(nums)
        for x in range(n):
            value = target - nums[x]
            if value in nums:
                y = nums.index(value)
                
                if x == y:
                    continue
                else:
                    return x, y
                    break
            else:
                continue
    
    def twosum3(self):
        nums = self.nums
        target = self.target
        
        for k, i in enumerate(nums):
            if target - i in nums[k + 1:]:
                return [k, nums[k + 1:].index(target - i) + k + 1]
    
    def twosum4(self):
        nums = self.nums
        target = self.target
        
        n = len(nums)
        dic = {}
        for x in range(n):
            value = target - nums[x]
            if nums[x] in dic:
                return dic[nums[x]],x
            else:
                dic[value] = x

if __name__ == "__main__":
                
    nums = [2, 7, 5, 11]
    target = 9

    tmp = TwoSum(nums,target)
    TNsum = tmp.twosum2()
    print("sum of the two number ",TNsum)
