# Python3.6 实现将一个字符串中的空格替换成 "%20".
"""
例如当前的字符串是 We Are Happy, 替换之后的字符串为 We%20AreHappy
"""

def ReplaceSpace(str):
    """
    Input:
        str: 输入的字符串
    Output:
        strReplace: 输出的替换了空格的字符串
    """
    strlen = list(str)
    strReplace = []
    for item in strlen:
        if item == ' ':
            strReplace.append('%')
            strReplace.append('2')
            strReplace.append('0')
        else:
            strReplace.append(item)
    return "".join(strReplace)



def ReplaceSpace2(str):
    """
    Input:
        str: 输入的字符串
    Output:
        strReplace: 输出的替换了空格的字符串
    """

    strReplace = ''
    if type(str) != str:
        return
    for s in str:
        if s == ' ':
            strReplace = strReplace + '%20'
        else:
            strReplace = strReplace + s
    return strReplace

def ReplaceSpace3(str):
    """
    Input:
        str: 输入的字符串
    Output:
        strReplace: 输出的替换了空格的字符串
    """
    if type(str) != str:
        return
    strReplace = str.replace(' ', '%20')
    return strReplace



if __name__ == "__main__":
    str = "We Are Happy"
    tmp = ReplaceSpace(str)
    print(tmp)

    tmp2 = ReplaceSpace2(str)
    print(tmp2)
    tmp3 = ReplaceSpace3(str)
    print(tmp3)
