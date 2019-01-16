# Python3.6 实现 Fibonacci 数列

import numpy as np


def Fibonacci(n):
    """
    Input:
        n: 输入一个整数
    Output:
        Fibonacci 数列的第 n 项
    """

    Fibonacci = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            Fibonacci[i%2] = Fibonacci[0] + Fibonacci[1]
        return Fibonacci[n%2]



def Fibonacci2(n):
    """
    # 使用递归的方法实现
    Input:
        n: 输入一个整数
    Output:
        Fibonacci 
    """

    Fibonacci = []
    for i in range(n):
        if i == 0 or i == 1:
            Fibonacci.append(1)
        else:
            result = Fibonacci[i-2] + Fibonacci[i-1]
            Fibonacci.append(result)
    return Fibonacci


if __name__ == "__main__":
    tmp = Fibonacci(3)
    print(tmp)

    tmp2 = Fibonacci2(20)
    print(tmp2)
