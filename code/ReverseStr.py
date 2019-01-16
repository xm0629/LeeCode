# Python3.6 实现字符串反转

import numpy as np



class ReverseStr(object):
    """
    字符串反转
    Input:
        string: 输入的字符串
    Output: 
        ReverseStr: 反转的字符串
    """
    def __init__(self, string):
        self.string = string

    def getReverseStr1(self):
        return self.string[::-1]

    def getReverseStr2(self):
        string = self.string

        if not string or len(string) < 2:
            return string
        strlist = list(string)
        start, end = 0, len(string) - 1
        while start < end:
            strlist[start], strlist[end] = strlist[end], strlist[start]
            start += 1
            end -= 1
        return "".join(strlist)


if __name__ == "__main__":
    string = "Hello World!"
    tmp = ReverseStr(string)
    print(tmp.getReverseStr1())
    print(tmp.getReverseStr2())
