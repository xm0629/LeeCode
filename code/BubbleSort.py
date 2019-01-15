# python3.6 实现冒泡排序


def BubbleSort(nums):
    """
    Input:
        nums 输入的一个乱序 list 
    Output:
        nums: 从小(大)到大(小)排序之后的新 list
    """
    for num in range(len(nums)-1, 0, -1):
        for i in range(num):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

# 改进的冒泡排序, 加入一个判断, 如果循环中没有发生交换，跳出本次循环

def modiBubbleSort(nums):
    """
    Input:
        nums: 输入的一个乱序 list 
    Output:
        nums: 从小(大)到大(小)排序之后的新 list
    """
    exchange = True
    N = len(nums) - 1
    while N >= 1 and exchange:
        exchange = False
        for i in range(N):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                exchange = True
        N -= 1
    return nums




if __name__ == "__main__":
    nums = [3, 4, 2, 6, 1, 9]
    tmp = BubbleSort(nums)
    print(tmp)
    modi_tmp = modiBubbleSort(nums)
    print(modi_tmp)

