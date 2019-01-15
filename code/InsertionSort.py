# python3.6 实现插入排序 

def InsertionSort(nums):
    """
    Input:
        nums 输入的一个乱序 list 
    Output:
        nums: 从小(大)到大(小)排序之后的新 list
    """
    for index, value in enumerate(nums):
        while index > 0 and nums[index-1] > value:
            nums[index] = nums[index-1]
            index -= 1
        nums[index] = value
    return nums


def InsertionSort2(nums):
    """
    Input:
        nums 输入的一个乱序 list 
    Output:
        nums: 从小(大)到大(小)排序之后的新 list
    """

    for index in range(1, len(nums)):
        currentvalue = nums[index]

        while index > 0 and nums[index-1] > currentvalue:
            nums[index] = nums[index-1]
            index -= 1
        nums[index] = currentvalue
    return nums


if __name__ == "__main__":
    nums = [3, 4, 2, 6, 1, 9]
    tmp = InsertionSort(nums)
    print(tmp) 
    tmp2 = InsertionSort2(nums)
    print(tmp2)
