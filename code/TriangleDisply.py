def TriangleDisplay(str):
    str += ' '
    result = []
    length = len(str)
    for i in range(1, length):
        result.append(str[-i:-1])
    for i in range(length):
        result.append([i:-1])
    return result

if __name__ == "__main__":

    for each in triangleDisplay(u"我和我的小伙伴们都惊呆了"):
    print(each)
