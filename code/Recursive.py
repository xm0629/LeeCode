# python3.6 实现递归的操作

import numpy as np

# 递归求和
def RecursiveSum(nums):
    """
    Input:
        nums: 输入的数组list
    Output:
        sum: 数组递归求和
    """
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + RecursiveSum(nums[1:])

# 递归求阶乘
def RecursiveFactorial(n):
    """
    Input:
        n: 输入的一个整数
    Output:
        Factorial: 递归求阶乘
    """

    if n <= 1:
        return 1
    else:
        return n * RecursiveFactorial(n-1)



# 递归实现进制转换 
def RecursivetoStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
      return RecursivetoStr(n//base, base) + convertString[n%base]

# 递归实现Hanoi塔
def RecursiveHanoi(fromPole, withPole, toPole, diskNum):
    if diskNum <= 1:
        print("moving disk from %s to %s" % (fromPole, toPole))
    else:
        RecursiveHanoi(fromPole, toPole, withPole, diskNum-1)
        print("moving disk from %s to %s" % (fromPole, toPole))
        RecursiveHanoi(withPole, fromPole, toPole, diskNum-1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    tmp = RecursiveSum(nums)
    print(tmp)
    n = 10
    tmp1 = RecursiveFactorial(n)
    print(tmp1)
    tmp2 = RecursivetoStr(1453, 16)
    print(1453)
    tmp3 = RecursiveHanoi('A', 'B', 'C', 3)
    print(tmp3)

